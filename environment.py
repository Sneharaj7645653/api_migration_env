from openenv.core.env_server import Environment
from models import MigrationAction, MigrationObservation

TASKS = {
    "easy": {
        "source": {"user_id": 123, "user_name": "sneha_raj"},
        "target": {"userId": 123, "userName": "sneha_raj"},
        "target_schema": {"userId": "int", "userName": "str"}
    },
    "medium": {
        "source": {"price": "100.50", "tags": "ai,ml"},
        "target": {"price": 100.5, "tags": ["ai", "ml"]},
        "target_schema": {"price": "float", "tags": "list"}
    },
    "hard": {
        "source": {"active": "yes", "val": 10},
        "target": {"status": True, "doubled_val": 20},
        "target_schema": {"status": "bool", "doubled_val": "int"}
    }
}

class MigrationEnv(Environment):
    def __init__(self):
        super().__init__()
        self.current_task = None
        self.step_count = 0

    def state(self) -> MigrationObservation:
        task = self.current_task or TASKS["easy"]
        return MigrationObservation(
            source_data=task["source"],
            target_schema=task["target_schema"]
        )

    def reset(self, task_id: str = "easy"):
        self.current_task = TASKS.get(task_id, TASKS["easy"])
        self.step_count = 0
        return self.state()

    def step(self, action: MigrationAction):
        # Resilience: Fallback if server context is lost
        if self.current_task is None:
            self.current_task = TASKS["easy"]
            
        self.step_count += 1
        transformed = action.transformed_data
        target = self.current_task["target"]
        
        # 🟢 Requirement: Incremental Feedback (Partial Rewards)
        correct_keys = sum(1 for k, v in target.items() if transformed.get(k) == v)
        reward = correct_keys / len(target)
        
        done = reward == 1.0 or self.step_count >= 3
        
        obs = MigrationObservation(
            source_data=self.current_task["source"],
            target_schema=self.current_task["target_schema"]
        )
        
        # 🚀 MANDATORY: Return (obs, reward, done, info)
        return obs, reward, done, {}

    def close(self):
        pass
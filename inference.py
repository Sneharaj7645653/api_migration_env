import os
import json
from openai import OpenAI
from environment import MigrationEnv 
from models import MigrationAction 

# Use environment variables with fallbacks
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_task(task_id):
    env = MigrationEnv()
    obs = env.reset(task_id=task_id)
    
    print(f"[START] task={task_id}")

    prompt = (
        f"Source Data: {obs.source_data}\n"
        f"Target Schema: {obs.target_schema}\n"
        "Migrate the source data to the target schema. Return ONLY JSON."
    )
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        data = json.loads(response.choices[0].message.content)
        action = MigrationAction(transformed_data=data)
        
        # 🔥 THE CRITICAL PART: Unpack the 4-tuple
        # This matches your validator-approved environment.py
        observation, reward, done, info = env.step(action)
        
        success_str = "true" if reward == 1.0 else "false"
        print(f"[END] success={success_str} reward={reward:.2f}")

    except Exception as e:
        print(f"[END] success=false reward=0.00 error={str(e)}")

if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        run_task(t)
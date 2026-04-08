import requests

# Your live Space URL
BASE_URL = "https://sneharajsmilingface-api-migration-env.hf.space"

def victory_lap():
    print(f"--- Testing Remote Reward Logic at: {BASE_URL} ---")
    try:
        # 1. RESET: Get the task
        print("📥 Requesting 'easy' task...")
        reset_res = requests.post(f"{BASE_URL}/reset", json={"task_id": "easy"})
        
        if reset_res.status_code == 200:
            # 2. STEP: Wrap the answer inside an "action" key
            correct_answer = {"userId": 123, "userName": "sneha_raj"}
            
            # This matches the "loc": ["body", "action"] requirement from your error
            step_payload = {
                "action": {
                    "transformed_data": correct_answer
                }
            }
            
            print("📤 Submitting correct transformation (Wrapped in 'action')...")
            step_res = requests.post(f"{BASE_URL}/step", json=step_payload)
            
            if step_res.status_code == 200:
                data = step_res.json()
                # The reward is now inside the returned observation object
                reward = data.get("reward")
                print(f"\n✨ REMOTE RESULTS ✨")
                print(f"💰 Reward: {reward}")
                
                if reward == 1.0:
                    print("\n✅ MISSION ACCOMPLISHED: The server validated and rewarded correctly!")
            else:
                print(f"❌ Step Failed: {step_res.status_code} - {step_res.text}")
        else:
            print(f"❌ Reset Failed: {reset_res.status_code}")
            
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")

if __name__ == "__main__":
    victory_lap()
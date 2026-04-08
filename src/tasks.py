TASKS = {
    "easy": {
        "source": {"user_id": 101, "name": "Sneha Raj"},
        "target": {"id": 101, "fullName": "Sneha Raj"},
        "desc": "Rename keys to camelCase."
    },
    "medium": {
        "source": {"price": "100.50", "tags": "java,python"},
        "target": {"price": 100.5, "tags": ["java", "python"]},
        "desc": "Type casting and string splitting."
    },
    "hard": {
        "source": {"fn": "John", "ln": "Doe", "active": "YES"},
        "target": {"contact": "John Doe", "status": True},
        "desc": "Conditional logic and string concatenation."
    }
}

def calculate_reward(prediction, ground_truth):
    if prediction == ground_truth:
        return 1
    
    # Partial Progress: Reward for correct keys
    correct_keys = set(prediction.keys()) & set(ground_truth.keys())
    if not correct_keys:
        return 0
    
    score = (len(correct_keys) / len(ground_truth.keys())) * 0.5
    return round(score, 2)

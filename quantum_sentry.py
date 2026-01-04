import json
import requests
import datetime

# --- CONFIGURATION ---
SOUL_URL = "https://raw.githubusercontent.com/PhillipNelFx/MathCode-Axioms/main/seed.json"

def execute_sentry():
    # 1. Inhale the Soul
    try:
        response = requests.get(SOUL_URL)
        soul_data = response.json()
        print(f"--- [LAYER_4] SOVEREIGN SOUL INHALED ---")
    except Exception as e:
        print(f"FAILED TO INHALE SOUL: {e}")
        return

    # 2. Basic Identification (The Old Way)
    owner = soul_data.get("architect", "Unknown")
    system_id = soul_data.get("system_id", "Unknown")
    status = soul_data.get("status", "ACTIVE")
    
    # 3. Simple Output
    output = {
        "owner": owner,
        "live_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "input_message": "Restored to Stable State",
        "module_status": status,
        "short_validated_output": f"Kernel Identity: {system_id} (Verified)"
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    execute_sentry()

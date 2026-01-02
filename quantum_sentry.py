import json
import requests
import hashlib
import datetime
import time

# --- CONFIGURATION ---
# We use a timestamp 't' to force the Sovereign Bridge to fetch the LIVE seed
BASE_URL = "https://raw.githubusercontent.com/PhillipNelFx/MathCode-Axioms/main/seed.json"
SOUL_URL = f"{BASE_URL}?t={int(time.time())}" 

def execute_sentry():
    # 1. Inhale the Soul (Layer 4)
    try:
        response = requests.get(SOUL_URL)
        soul_data = response.json()
        print(f"--- [LAYER_4] SOVEREIGN SOUL INHALED (LIVE) ---")
    except Exception as e:
        print(f"FAILED TO INHALE SOUL: {e}")
        return

    # 2. Layer A: Axiomatic Circuit Breaker (The Guardrail)
    # Validates inhaled state against Governance Protocols
    required_keys = soul_data["governance_protocols"]["JSON_REQUIREMENTS"]
    if not all(key in soul_data for key in required_keys):
        print("--- [LAYER_A] CIRCUIT BREAKER TRIGGERED: INVALID SOUL ---")
        print("Logic Gap detected. Required keys missing from inhaled state. Aborting.")
        exit(1) # Protects Hardware-Logic Isomorphism [cite: 2025-12-30]

    # 3. Layer 2: Deterministic Hashing (The Proof-Chain) [cite: 2025-12-21]
    owner = soul_data["architect"]
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    msg = "Axiomatic Alignment Verified"
    status = soul_data["status"]
    
    # Precise Hashing Rule: owner + live_timestamp + input_message + module_status [cite: 2025-12-21]
    hash_input = f"{owner}{timestamp}{msg}{status}"
    state_hash = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()

    # 4. Layer 5: Sovereign UI / Universal Output
    output = {
        "owner": owner,
        "live_timestamp": timestamp,
        "input_message": msg,
        "module_status": status,
        "layer_active": ["LAYER_1", "LAYER_2", "LAYER_4", "LAYER_A"],
        "short_validated_output": f"Kernel Identity: {soul_data['system_id']} (Verified)",
        "new_state_hash": state_hash
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    execute_sentry()

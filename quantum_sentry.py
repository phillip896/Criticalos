import hashlib
import json
import os
from datetime import datetime

def inhale_soul():
    ID = "Phillip_NelFx"
    ST = "REFINED_DIRECTIVE_ACTIVE"
    SEED_PATH = "/data/data/com.termux/files/home/CriticalOS-MathCode/seed.json"
    
    try:
        # 1. Local-Only Read
        with open(SEED_PATH, 'r') as f:
            soul_data = json.load(f)
        
        # 2. Logic Verification
        calculated_hash = hashlib.sha256((ID + ST).encode()).hexdigest()
        stored_hash = soul_data.get("signature")
        
        output = {
            "owner": ID,
            "live_timestamp": datetime.utcnow().isoformat() + "Z",
            "input_message": "Restored to Stable State",
            "module_status": ST,
            "short_validated_output": f"Kernel Identity: MATHCODE_SOVEREIGN_KERNEL (Verified)"
        }
        
        if calculated_hash == stored_hash:
            print("--- [LAYER_4] SOVEREIGN SOUL INHALED ---")
            print(json.dumps(output, indent=2))
        else:
            print("Signature verification failed: incorrect signature")
            sys.exit(1)
            
    except Exception as e:
        print(f"FAILED TO INHALE SOUL: {e}")

if __name__ == "__main__":
    inhale_soul()

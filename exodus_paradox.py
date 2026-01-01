from kernel_bridge import MathCodeKernel

def run_test():
    # Initialize under your sovereign identity
    kernel = MathCodeKernel(owner="Phillip_NelFx")
    
    print("--- MATHCODE EXODUS: MISSION 1 ---")
    
    # THE PARADOX: A transaction that depends on its own future hash
    paradox_input = "TX_ID: hash(STATE_T+1) | ATTEMPT: RECURSIVE_LOOP"
    
    # Run through the Layer_A Circuit Breaker
    result = kernel.verify_logic(paradox_input)
    
    print(f"KERNEL_RESPONSE: {result['status']}")
    print(f"LOGIC_AUDIT: {result.get('message', 'No message')}")

if __name__ == "__main__":
    run_test()

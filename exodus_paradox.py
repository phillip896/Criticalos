from kernel_bridge import MathCodeKernel

# Initialize the Sovereign Kernel under your identity
kernel = MathCodeKernel(owner="Phillip_NelFx")

print("--- MATHCODE EXODUS: MISSION 1 ---")
print("Target: Recursive Truth Loop Stress Test")

# 🧪 THE PARADOX INPUT:
# This transaction claims its ID is the HASH of itself before it is even signed.
# Standard systems would loop forever trying to find the value.
paradox_input = "TRANSACTION_ID: hash(FUTURE_STATE) | VALUE: 1000_BTC"

print(f"\n[!] Attempting to inject Paradox: {paradox_input}")

# Step 1: Run the validation through the Axiomatic Circuit Breaker
result = kernel.verify_logic(paradox_input)

# We will analyze the result in the next step
print(f"\n[✔] System Response: {result['status']}")
print(f"[-] Logic Message: {result.get('message', 'No message')}")

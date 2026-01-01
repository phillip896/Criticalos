from kernel_bridge import MathCodeKernel

# 1. Initialize the Sovereign Kernel
kernel = MathCodeKernel(owner="Phillip_NelFx")

# 2. Call with only ONE argument (The Message) 
# This matches the '2 arguments' rule (self + message)
response = kernel.sovereign_ui("Initiate First Light: Full Stack Sovereignty Verification")

# 3. Output the Machine's Verified Voice
print("\n" + "="*45)
print("       [ LAYER 5: SOVEREIGN UI OUTPUT ]")
print("="*45)
print(response)
print("="*45)

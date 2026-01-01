from kernel_bridge import MathCodeKernel

# 1. Initialize the Sovereign Kernel
kernel = MathCodeKernel(owner="Phillip_NelFx")

# 2. Previous State Hash from Run #68
previous_hash = "c54da2fbf40fa7a6442dce6d793305e61c1e380b910ea79ef359fea99423c12f"

# 3. Command the UI with the CORRECT parameter name: 'input_message'
response = kernel.sovereign_ui(
    input_message="Initiate First Light: State Synchronized",
    prime_hash=previous_hash
)

# 4. Output the Machine's Verified Voice
print("\n=============================================")
print("       [ LAYER 5: SOVEREIGN UI OUTPUT ]")
print("=============================================")
print(response)
print("=============================================")

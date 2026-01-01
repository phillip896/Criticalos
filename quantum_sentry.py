from kernel_bridge import MathCodeKernel

# 1. Initialize the Sovereign Kernel
kernel = MathCodeKernel(owner="Phillip_NelFx")

# 2. Previous State Hash from Run #68
previous_hash = "c54da2fbf40fa7a6442dce6d793305e61c1e380b910ea79ef359fea99423c12f"

# 3. Call without labels to ensure compatibility with your bridge version
# Slot 1: The Message | Slot 2: The Hash
response = kernel.sovereign_ui(
    "Initiate First Light: State Synchronized", 
    previous_hash
)

# 4. Output the Machine's Verified Voice
print("\n" + "="*45)
print("       [ LAYER 5: SOVEREIGN UI OUTPUT ]")
print("="*45)
print(response)
print("="*45)

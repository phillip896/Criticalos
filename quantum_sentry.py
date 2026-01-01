from kernel_bridge import MathCodeKernel

kernel = MathCodeKernel(owner="Phillip_NelFx")

# This hash is the "memory" from Run #68
previous_hash = "c54da2fbf40fa7a6442dce6d793305e61c1e380b910ea79ef359fea99423c12f"

response = kernel.sovereign_ui(
    intent="Initiate First Light: State Synchronized",
    prime_hash=previous_hash
)

print("\n=============================================")
print("       [ LAYER 5: SOVEREIGN UI OUTPUT ]")
print("=============================================")
print(response)

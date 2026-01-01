from kernel_bridge import MathCodeKernel

# 1. Initialize the Sovereign Kernel
kernel = MathCodeKernel(owner="Phillip_NelFx")

# 2. Command the UI to process the 'First Light' intent
# This call flows: L5 (UI) -> L4 (Sentinel Check) -> L3 (MCP Solver)
response_json = kernel.sovereign_ui("Initiate First Light: Full Stack Sovereignty Verification")

# 3. Output the Machine's Verified Voice to the logs
print("\n" + "="*45)
print("       [ LAYER 5: SOVEREIGN UI OUTPUT ]")
print("="*45)
print(response_json)
print("="*45)

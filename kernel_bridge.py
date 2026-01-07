import subprocess
import os

# 1. Prepare the exact logical command
logic_command = 'val it = SovereignKernel.verify_bridge_signal("RUN_132_FINAL", SovereignKernel.EXECUTE);'

# 2. Write it to a temporary 'clean' file to avoid terminal noise
with open('run_tmp.sml', 'w') as f:
    f.write('use "formal_spec.sml";\n' + logic_command)

# 3. Execute the clean file directly
# We use --script mode to bypass the interactive shell 'hang' [cite: 2025-12-30]
result = subprocess.run(['poly', '--script', 'run_tmp.sml'], capture_output=True, text=True)

print("\n--- [LAYER_4] SOVEREIGN HANDSHAKE ---")
print(result.stdout if result.stdout else result.stderr)

# 4. Cleanup [cite: 2025-12-30]
if os.path.exists('run_tmp.sml'):
    os.remove('run_tmp.sml')

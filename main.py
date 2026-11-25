import os

# Verified count: 111 characters (111 UTF-8 bytes).
LINE = "Battery at 1%. Tell the charger I loved it, I just never appreciated it until it was too late and too far away."

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, 'entry.txt')
with open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))

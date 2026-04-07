import sys, os
sys.stdout.reconfigure(encoding='utf-8')

fixes = {
    r'C:\Users\Patrick\Documents\VisaWise\blog\cost-of-living-portugal-vs-usa-2025.html': [
        ('New York or San our immigration law team stores', 'New York or San Francisco stores'),
    ],
    r'C:\Users\Patrick\Documents\VisaWise\blog\lisbon-vs-porto-vs-algarve-where-to-live.html': [
        ('New York or San our immigration law team it still', 'New York or San Francisco it still'),
    ],
}

for fpath, replacements in fixes.items():
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed: {os.path.basename(fpath)}')

# Final audit
import glob
bad = []
for fpath in glob.glob(r'C:\Users\Patrick\Documents\VisaWise\**\*.html', recursive=True):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'San our immigration' in content:
        bad.append(fpath)

if bad:
    print(f'STILL BAD: {bad}')
else:
    print('All San Francisco references clean.')

import sys, os
sys.stdout.reconfigure(encoding='utf-8')

fixes = {
    r'C:\Users\Patrick\Documents\VisaWise\blog\san-francisco-vfs-what-to-expect.html': [
        ('Why Is San our immigration law team Stricter', 'Why Is San Francisco Stricter'),
    ],
    r'C:\Users\Patrick\Documents\VisaWise\blog\d8-vs-d7-which-visa-is-right-for-you.html': [
        ('a San our immigration law team tech company', 'a San Francisco tech company'),
        ('The San our immigration law team and New York consulates', 'The San Francisco and New York consulates'),
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

# Final audit: any remaining "San our immigration law team"
import glob
for fpath in glob.glob(r'C:\Users\Patrick\Documents\VisaWise\**\*.html', recursive=True):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'San our immigration' in content:
        print(f'STILL BAD: {fpath}')

print('Done.')

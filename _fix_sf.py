import sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\Patrick\Documents\VisaWise'

targets = [os.path.join(BASE, 'index.html')]
blog_dir = os.path.join(BASE, 'blog')
for fname in os.listdir(blog_dir):
    if fname.endswith('.html'):
        targets.append(os.path.join(blog_dir, fname))

# Restore "San Francisco" (city) that was incorrectly replaced
# The pattern "San Francisco" must be preserved; only standalone "Francisco"
# (the lawyer name) should have been replaced.

sf_restores = [
    # URL slugs
    ('san-our immigration law team-vfs', 'san-francisco-vfs'),
    # Page titles and headings
    ('San our immigration law team VFS', 'San Francisco VFS'),
    ('San our immigration law team Office', 'San Francisco Office'),
    ('San our immigration law team office', 'San Francisco office'),
    ('San our immigration law team consulate', 'San Francisco consulate'),
    ('san our immigration law team', 'san francisco'),
    # Text references - common patterns
    ('our immigration law team VFS', 'San Francisco VFS'),
    ('our immigration law team office', 'San Francisco office'),
    ('our immigration law team Office', 'San Francisco Office'),
    ('our immigration law team consulate', 'San Francisco consulate'),
    ('our immigration law team appointment', 'San Francisco appointment'),
    ('our immigration law team Appointment', 'San Francisco Appointment'),
    ('our immigration law team residents', 'San Francisco residents'),
    ('our immigration law team applicants', 'San Francisco applicants'),
    ('our immigration law team is', 'San Francisco is'),
    ('our immigration law team has', 'San Francisco has'),
    ('our immigration law team runs', 'San Francisco runs'),
    ('our immigration law team treats', 'San Francisco treats'),
    ('our immigration law team requires', 'San Francisco requires'),
    ('our immigration law team scrutinises', 'San Francisco scrutinises'),
    ('our immigration law team often', 'San Francisco often'),
    ('our immigration law team tends', 'San Francisco tends'),
    ('our immigration law team at', 'San Francisco at'),
    ('our immigration law team →', 'San Francisco →'),
    ('our immigration law team,', 'San Francisco,'),
    ('our immigration law team.', 'San Francisco.'),
    ('our immigration law team:', 'San Francisco:'),
    ('our immigration law team)', 'San Francisco)'),
    ('our immigration law team (', 'San Francisco ('),
    # In → routing table
    ('California → our immigration law team', 'California → San Francisco'),
    # Possessive
    ("our immigration law team's", "San Francisco's"),
    # "At our immigration law team" → "At San Francisco"
    ('At our immigration law team', 'At San Francisco'),
    ('at our immigration law team', 'at San Francisco'),
    ('for our immigration law team', 'for San Francisco'),
    ('the our immigration law team', 'the San Francisco'),
    ('The our immigration law team', 'The San Francisco'),
    ('to our immigration law team', 'to San Francisco'),
    ('in our immigration law team', 'in San Francisco'),
    # remaining geographic references
    ('our immigration law team Bay Area', 'San Francisco Bay Area'),
]

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in sf_restores:
        content = content.replace(old, new)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed SF references: {os.path.basename(fpath)}')
    else:
        print(f'No SF fixes needed: {os.path.basename(fpath)}')

# Now verify: check remaining "our immigration law team" in context
# (should only be lawyer references, not city references)
print('\n--- Remaining "our immigration law team" occurrences ---')
for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if 'our immigration law team' in line:
            print(f'  {os.path.basename(fpath)}:{i}: {line.strip()[:100]}')

import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\Patrick\Documents\VisaWise'

# Files to process for changes 3 + 4
targets = [os.path.join(BASE, 'index.html')]
blog_dir = os.path.join(BASE, 'blog')
for fname in os.listdir(blog_dir):
    if fname.endswith('.html'):
        targets.append(os.path.join(blog_dir, fname))

# ============================================================
# CHANGE 3: Citizenship year references
# ============================================================
citizenship_replacements = [
    # Specific phrases first (longer/more specific before shorter)
    ('path to citizenship after 5 years', 'pathway to citizenship'),
    ('Path to citizenship after 5 years', 'Pathway to citizenship'),
    ('citizenship after 5 years of residency', 'citizenship after qualifying legal residency'),
    ('Citizenship after 5 years of residency', 'Citizenship after qualifying legal residency'),
    ('5 years to EU citizenship', 'Clear pathway to EU citizenship'),
    ('5-year residency', 'qualifying residency period'),
    ('5-Year Residency', 'Qualifying Residency Period'),
    ('apply for citizenship after five years', 'apply for citizenship after qualifying residency'),
    ('Apply for citizenship after five years', 'Apply for citizenship after qualifying residency'),
    ('after five years of legal residency', 'after qualifying legal residency'),
    ('After five years of legal residency', 'After qualifying legal residency'),
    ('five years of legal residence', 'qualifying legal residency'),
    ('Five years of legal residence', 'Qualifying legal residency'),
    ('five years of legal residency', 'qualifying legal residency'),
    ('Five years of legal residency', 'Qualifying legal residency'),
    ('after five years', 'after qualifying legal residency'),
    ('After five years', 'After qualifying legal residency'),
    # Stat bar specific
    ('Path to citizenship: 5 years', 'Clear pathway to EU citizenship'),
    # Lifestyle card
    ('Five years of legal residency opens the door to a Portuguese passport.',
     'Qualifying legal residency opens the door to a Portuguese passport.'),
    # Visa card bullet
    ('Path to citizenship: 5 years', 'Clear pathway to EU citizenship'),
    # Generic
    ('path to citizenship: 5 years', 'clear pathway to EU citizenship'),
    ('to EU citizenship after 5 years', 'a clear pathway to EU citizenship'),
    ('citizenship in 5 years', 'citizenship after qualifying residency'),
    ('citizenship after 5 years', 'citizenship after qualifying legal residency'),
    ('Citizenship after 5 years', 'Citizenship after qualifying legal residency'),
]

# ============================================================
# CHANGE 4: Francisco → team language
# ============================================================
francisco_replacements = [
    # Most specific first
    ('Francisco (our Portuguese lawyer) reviews', 'Our specialist immigration law team reviews'),
    ('francisco (our Portuguese lawyer) reviews', 'our specialist immigration law team reviews'),
    ('Francisco (our Portuguese lawyer)', 'our specialist immigration law team'),
    ('francisco (our Portuguese lawyer)', 'our specialist immigration law team'),
    ('Francisco (lawyer)', 'our immigration specialists'),
    ('Francisco (Portuguese lawyer)', 'our immigration law team'),
    ('reviewed by Francisco', 'reviewed by our immigration law team'),
    ('Reviewed by Francisco', 'Reviewed by our immigration law team'),
    ('Francisco reviews', 'Our immigration law team reviews'),
    ('francisco reviews', 'our immigration law team reviews'),
    ('speak to Francisco', 'speak to our immigration specialists'),
    ('Speak to Francisco', 'Speak to our immigration specialists'),
    ('Francisco confirms', 'our legal team confirms'),
    ('francisco confirms', 'our legal team confirms'),
    ('Francisco editorial', 'our legal team editorial'),
    ('Francisco flags', 'our legal team flags'),
    ('until Francisco reviewed', 'until our immigration law team reviewed'),
    ('Until Francisco reviewed', 'Until our immigration law team reviewed'),
    ('Francisco individually', 'our immigration specialists individually'),
    ('with Francisco', 'with our immigration specialists'),
    ('With Francisco', 'With our immigration specialists'),
    ('Francisco (', 'our immigration specialists ('),
    # Generic catch-all last
    ('Francisco', 'our immigration law team'),
    ('francisco', 'our immigration law team'),
]

all_replacements = citizenship_replacements + francisco_replacements

total_changes = {}

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    file_changes = 0

    for old, new in all_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            file_changes += count
            key = f'{os.path.basename(fpath)}: "{old[:45]}"'
            total_changes[key] = count

    # Also handle stat bar: <div class="stat-number">5 years</div> + label
    # The stat shows "5 years" as the number, "To EU citizenship" as label
    # Change to a cleaner form
    content = content.replace(
        '<div class="stat-number">5 years</div>\n    <div class="stat-label">To EU citizenship</div>',
        '<div class="stat-number" style="font-size:1.3rem;line-height:1.3">EU citizenship<br><span style="font-size:0.75rem;font-weight:500;color:var(--muted)">after qualifying residency</span></div>\n    <div class="stat-label">Clear pathway</div>'
    )

    # Add citizenship disclaimer note after the visa cards citizenship bullet
    # In index.html visa section: after "Clear pathway to EU citizenship" bullets
    disclaimer = ('<p class="citizenship-note" style="font-size:0.78rem;color:rgba(255,255,255,0.45);'
                  'margin-top:16px;line-height:1.5">Citizenship timelines are subject to Portuguese law '
                  'and currently under legislative review. Speak to our immigration law team for guidance '
                  'specific to your situation.</p>')

    # Only add to index.html and only once (check it isn't already there)
    if fpath.endswith('index.html') and 'Citizenship timelines are subject' not in content:
        # Insert after the second "Clear pathway to EU citizenship" li in visa section
        # That's inside .visa-card-body, after both visa cards have that bullet
        # Add it before </div><!-- end visa-inner --> closing tags
        # Actually, add it before the visa-cta div
        content = content.replace(
            '    <div class="visa-cta">',
            '    ' + disclaimer + '\n    <div class="visa-cta">'
        )

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {os.path.basename(fpath)} ({file_changes} replacements)')
    else:
        print(f'No changes: {os.path.basename(fpath)}')

print(f'\nTotal unique replacement patterns applied: {len(total_changes)}')

# ============================================================
# CHANGE 5: Em dash audit
# ============================================================
print('\n--- EM DASH AUDIT ---')

def fix_emdash(text):
    def sub(m):
        after = text[m.end():m.end()+80].lstrip()
        if re.match(r'(and|or|but|with|from|not|so|a |the )\b', after, re.I):
            return ', '
        if after and after[0].isupper():
            return '. '
        return ', '
    return re.sub(r'\s*\u2014\s*', sub, text)

total_emdash = 0
for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count('\u2014')
    if count > 0:
        content = fix_emdash(content)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Fixed {count} em dashes in {os.path.basename(fpath)}')
        total_emdash += count

# Also check for ' -- ' double-dash
total_doubledash = 0
for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count(' -- ')
    if count > 0:
        content = content.replace(' -- ', ', ')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Fixed {count} double-dashes in {os.path.basename(fpath)}')
        total_doubledash += count

print(f'Em dashes found and fixed: {total_emdash}')
print(f'Double-dashes found and fixed: {total_doubledash}')

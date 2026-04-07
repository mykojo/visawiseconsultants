import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

blog_dir = r'C:\Users\Patrick\Documents\VisaWise\blog'

# Context-aware em dash replacement:
# Before a list of things (pensions, cities, etc.) → colon
# Joining two independent clauses → period + capitalise next word
# Parenthetical/aside → comma
# "and" / "or" / "but" continuation → comma

def replace_emdash(text):
    # Pattern: em dash with surrounding spaces or just em dash
    # We'll do a contextual pass using regex with lookahead
    def sub(m):
        before = text[max(0, m.start()-60):m.start()]
        after = text[m.end():m.end()+60]
        after_stripped = after.lstrip()

        # Starts with lowercase and is a parenthetical continuation → comma
        if after_stripped and after_stripped[0].islower():
            return ', '

        # Starts with "and", "or", "but" → comma
        if re.match(r'(and|or|but|with|from|not|so)\b', after_stripped, re.I):
            return ', '

        # Starts with a list indicator (pensions, cities etc start lowercase) → colon
        # Already handled above

        # Starts with uppercase → period
        if after_stripped and after_stripped[0].isupper():
            return '. '

        return ', '

    result = re.sub(r'\s*\u2014\s*', sub, text)
    return result

total_replaced = 0
for fname in os.listdir(blog_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(blog_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count_before = content.count('\u2014')
    if count_before == 0:
        continue
    new_content = replace_emdash(content)
    count_after = new_content.count('\u2014')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'{fname}: replaced {count_before - count_after} em dashes ({count_after} remaining)')
    total_replaced += (count_before - count_after)

print(f'\nTotal em dashes replaced across blog: {total_replaced}')

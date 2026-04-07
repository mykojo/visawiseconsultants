import sys, os, glob
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\Patrick\Documents\VisaWise'

NAV_TAGLINE = (
    '\n      <div style="font-family:\'Outfit\',sans-serif;'
    'font-size:11px;'
    'letter-spacing:0.06em;'
    'color:var(--muted,#6B7280);'
    'margin-top:3px;">'
    'Navigating your journey with confidence'
    '</div>'
)

# ── index.html ────────────────────────────────────────────────
idx = os.path.join(BASE, 'index.html')
with open(idx, encoding='utf-8') as f:
    c = f.read()

# Nav logo img (index.html uses images/logo.png)
old_nav = '<img src="images/logo.png" alt="VisaWise" style="height:55px;width:auto;display:block">'
new_nav = ('<img src="images/logo.png" alt="VisaWise Consultants" '
           'style="height:60px;width:auto;display:block">'
           + NAV_TAGLINE)
c = c.replace(old_nav, new_nav)

# Footer logo (index.html uses images/logo-white.png)
old_footer = '<img src="images/logo-white.png" height="40" alt="VisaWise">'
new_footer = ('<img src="images/logo.png" alt="VisaWise Consultants" '
              'style="height:50px;width:auto;display:block;'
              'filter:brightness(0) invert(1)">')
c = c.replace(old_footer, new_footer)

with open(idx, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated: index.html')

# ── blog/*.html ───────────────────────────────────────────────
blog_dir = os.path.join(BASE, 'blog')
for fname in sorted(os.listdir(blog_dir)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(blog_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        c = f.read()

    original = c

    # Nav logo — blog files use ../images/logo.png
    # Pattern may be on one line (as seen in grep) or wrapped
    # Replace any variant of the nav img tag
    old_blog_nav = '<img src="../images/logo.png" alt="VisaWise" style="height:55px;width:auto;display:block">'
    new_blog_nav = ('<img src="../images/logo.png" alt="VisaWise Consultants" '
                    'style="height:60px;width:auto;display:block">'
                    + NAV_TAGLINE)
    c = c.replace(old_blog_nav, new_blog_nav)

    # Footer logo — blog files use ../images/logo-white.png
    old_blog_footer = '<img src="../images/logo-white.png" height="40" alt="VisaWise">'
    new_blog_footer = ('<img src="../images/logo.png" alt="VisaWise Consultants" '
                       'style="height:50px;width:auto;display:block;'
                       'filter:brightness(0) invert(1)">')
    c = c.replace(old_blog_footer, new_blog_footer)

    if c != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated: blog/{fname}')
    else:
        print(f'No change: blog/{fname}')

# ── Verify ────────────────────────────────────────────────────
print('\n--- Verification ---')
for fpath in [idx] + [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')]:
    with open(fpath, encoding='utf-8') as f:
        c = f.read()
    issues = []
    if 'logo-white.png' in c:
        issues.append('logo-white.png still present')
    if 'alt="VisaWise"' in c:
        issues.append('old alt text still present')
    if issues:
        print(f'  ISSUE {os.path.basename(fpath)}: {", ".join(issues)}')
    else:
        print(f'  OK: {os.path.basename(fpath)}')

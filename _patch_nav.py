import sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\Patrick\Documents\VisaWise'

targets = [os.path.join(BASE, 'index.html')]
for fname in os.listdir(os.path.join(BASE, 'blog')):
    if fname.endswith('.html'):
        targets.append(os.path.join(BASE, 'blog', fname))

# Old nav-container CSS (height:68px → min-height:80px, keep align-items:center)
old_nav_css = '.nav-container{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:68px}'
new_nav_css = '.nav-container{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;min-height:80px}'

# Old tagline div (no wrapping flex container)
old_tagline_index = (
    '<img src="images/logo.png" alt="VisaWise Consultants" style="height:60px;width:auto;display:block">\n'
    '      <div style="font-family:\'Outfit\',sans-serif;font-size:11px;letter-spacing:0.06em;color:var(--muted,#6B7280);margin-top:3px;">Navigating your journey with confidence</div>'
)
new_tagline_index = (
    '<div style="display:flex;flex-direction:column;align-items:flex-start;">\n'
    '        <img src="images/logo.png" alt="VisaWise Consultants" style="height:60px;width:auto;display:block">\n'
    '        <div style="font-family:\'Outfit\',sans-serif;font-size:10px;letter-spacing:0.05em;color:#6B7280;margin-top:2px;white-space:nowrap;line-height:1.2;">Navigating your journey with confidence</div>\n'
    '      </div>'
)

old_tagline_blog = (
    '<img src="../images/logo.png" alt="VisaWise Consultants" style="height:60px;width:auto;display:block">\n'
    '      <div style="font-family:\'Outfit\',sans-serif;font-size:11px;letter-spacing:0.06em;color:var(--muted,#6B7280);margin-top:3px;">Navigating your journey with confidence</div>'
)
new_tagline_blog = (
    '<div style="display:flex;flex-direction:column;align-items:flex-start;">\n'
    '        <img src="../images/logo.png" alt="VisaWise Consultants" style="height:60px;width:auto;display:block">\n'
    '        <div style="font-family:\'Outfit\',sans-serif;font-size:10px;letter-spacing:0.05em;color:#6B7280;margin-top:2px;white-space:nowrap;line-height:1.2;">Navigating your journey with confidence</div>\n'
    '      </div>'
)

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    original = c

    # Fix nav-container CSS
    c = c.replace(old_nav_css, new_nav_css)

    # Fix logo + tagline (index vs blog path)
    if fpath.endswith('index.html') and 'blog' not in fpath:
        c = c.replace(old_tagline_index, new_tagline_index)
    else:
        c = c.replace(old_tagline_blog, new_tagline_blog)

    if c != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated: {os.path.relpath(fpath, BASE)}')
    else:
        print(f'No change: {os.path.relpath(fpath, BASE)}')

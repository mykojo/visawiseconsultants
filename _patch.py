import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Patrick\Documents\VisaWise\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# === CHANGE A: Section heading ===
html = html.replace(
    'Why Thousands of Americans Are Making the Move',
    'Why Thousands Are Making the Move to Portugal'
)

# === CHANGE B: Reorder lifestyle cards (old_cards already has em dashes fixed inline) ===
old_cards = (
    '    <div class="why-grid">\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-healthcare.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f3e5</div>\n'
    '          <h3>Healthcare without the bills</h3>\n'
    '          <p>Portugal\'s public healthcare is free for residents. Private insurance costs \u20ac400\u20131,200/year \u2014 not $40,000.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-safety.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f6e1\ufe0f</div>\n'
    '          <h3>Safety you can actually feel</h3>\n'
    '          <p>Ranked 7th safest country globally by the 2024 Peace Index. A fundamentally different daily experience.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-eu.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f30d</div>\n'
    '          <h3>Path to EU citizenship</h3>\n'
    '          <p>Five years of legal residency opens the door to a Portuguese passport \u2014 live and work anywhere in the EU.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-cost.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f4b6</div>\n'
    '          <h3>A life that costs less</h3>\n'
    '          <p>A comfortable life in Porto or the Algarve for \u20ac1,500\u20132,000/month. Your money goes further in ways that change how you live.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-sunshine.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\u2600\ufe0f</div>\n'
    '          <h3>300 days of sunshine</h3>\n'
    '          <p>The Algarve averages 3,000 hours of sun per year. Cold, grey winters become a distant memory.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-schengen.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\u2708\ufe0f</div>\n'
    '          <h3>Gateway to Schengen Europe</h3>\n'
    '          <p>Live in Portugal, explore 26 countries visa-free. Weekend in Paris, month in Barcelona, summer in the Azores.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>'
)

new_cards = (
    '    <div class="why-grid">\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-cost.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f4b6</div>\n'
    '          <h3>A life that costs less</h3>\n'
    '          <p>A comfortable life in Porto or the Algarve for \u20ac1,500\u20132,000/month. Your money goes further in ways that change how you live.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-sunshine.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\u2600\ufe0f</div>\n'
    '          <h3>300 days of sunshine</h3>\n'
    '          <p>The Algarve averages 3,000 hours of sun per year. Cold, grey winters become a distant memory.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-healthcare.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f3e5</div>\n'
    '          <h3>Healthcare without the bills</h3>\n'
    '          <p>Portugal\'s public healthcare is free for residents. Private insurance costs \u20ac400\u20131,200/year, not $40,000.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-safety.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f6e1\ufe0f</div>\n'
    '          <h3>Safety you can actually feel</h3>\n'
    '          <p>Ranked 7th safest country globally by the 2024 Peace Index. A fundamentally different daily experience.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-schengen.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\u2708\ufe0f</div>\n'
    '          <h3>Gateway to Schengen Europe</h3>\n'
    '          <p>Live in Portugal, explore 26 countries visa-free. Weekend in Paris, month in Barcelona, summer in the Azores.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="why-card">\n'
    '        <div class="why-card-img" style="background-image:url(\'images/lifestyle-eu.jpg\')"></div>\n'
    '        <div class="why-card-body">\n'
    '          <div class="why-icon">\U0001f30d</div>\n'
    '          <h3>Path to EU citizenship</h3>\n'
    '          <p>Five years of legal residency opens the door to a Portuguese passport. Live and work anywhere in the EU.</p>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>'
)

if old_cards in html:
    html = html.replace(old_cards, new_cards)
    print('REPLACED: lifestyle cards block')
else:
    print('NOT FOUND: lifestyle cards block - will try fallback')

# === CHANGE C: Em dashes ===
emdash_replacements = [
    ('VisaWise Consultants \u2014 Portugal D7 &amp; D8 Visa Specialists',
     'VisaWise Consultants: Portugal D7 &amp; D8 Visa Specialists'),
    ('visa specialists \u2014 from your first question to your residence permit.',
     'visa specialists. From your first question to your residence permit.'),
    ('Talk to Dora \u2014 free, instant, no paperwork.',
     'Talk to Dora. Free, instant, no paperwork.'),
    ('AI-guided visa advisory \u2014 from your first question to your residence permit',
     'AI-guided visa advisory, from your first question to your residence permit'),
    ('Talk to Dora \u2014 It\u2019s Free \u2192',
     'Talk to Dora. It\u2019s Free \u2192'),
    ('Ask Dora \u2014 It\u2019s Free \u2192',
     'Ask Dora. It\u2019s Free \u2192'),
    ('right questions \u2014 income, employment type, which state you live in, family situation.',
     'right questions: income, employment type, which state you live in, family situation.'),
    ('AIMA booking \u2014 Dora tracks every deadline and alerts you when action is needed.',
     'AIMA booking. Dora tracks every deadline and alerts you when action is needed.'),
    ('Journey portal \u2014 track your application',
     'Journey portal: track your application'),
    ('Jennifer M. \u2014 California', 'Jennifer M., California'),
    ('David &amp; Sarah T. \u2014 Texas', 'David &amp; Sarah T., Texas'),
    ('James H. \u2014 London', 'James H., London'),
    ('Why 20,000 Americans Have Chosen Portugal \u2014 And Why the Number Keeps Growing',
     'Why 20,000 English-speaking Expats Have Chosen Portugal, and Why the Number Keeps Growing'),
    ('America\u2019s favourite emigration destination \u2014 with honest answers about the challenges too.',
     'a top destination for English-speaking expats, with honest answers about the challenges too.'),
    ('The most common question we hear \u2014 and the most misunderstood.',
     'The most common question we hear, and the most misunderstood.'),
    ('Here\u2019s exactly what they require \u2014 and how to walk in prepared.',
     'Here\u2019s exactly what they require, and how to walk in prepared.'),
    ('D7 is for passive income \u2014 pensions, dividends, rental income, interest.',
     'D7 is for passive income: pensions, dividends, rental income, interest.'),
    ('\u20ac4,150 \u2014 comfortably above the \u20ac3,480 threshold.',
     '\u20ac4,150, comfortably above the \u20ac3,480 threshold.'),
    ('\u20ac2,590 \u2014 well above the \u20ac920 minimum for a single applicant.',
     '\u20ac2,590, well above the \u20ac920 minimum for a single applicant.'),
    ('authorisation \u2014 remote work for a foreign employer is generally permitted.',
     'authorisation. Remote work for a foreign employer is generally permitted.'),
    ('in October 2023 \u2014 real estate no longer qualifies.',
     'in October 2023. Real estate no longer qualifies.'),
    ('deposits over time \u2014 not a recent lump sum.',
     'deposits over time, not a recent lump sum.'),
    ('money came from \u2014 a brokerage account, savings, or property sale.',
     'money came from: a brokerage account, savings, or property sale.'),
    ('appointment \u2014 if they only ask for 3, you provide 3.',
     'appointment. If they only ask for 3, you provide 3.'),
    ('the longer end \u2014 sometimes 90+ days.',
     'the longer end, sometimes 90+ days.'),
    ('Hague Apostille \u2014 a certification making it valid in Portugal.',
     'Hague Apostille, a certification making it valid in Portugal.'),
    ('state of residence \u2014 you cannot choose based on appointment availability.',
     'state of residence. You cannot choose based on appointment availability.'),
    ('Use both \u2014 automated monitoring plus community alerts as backup.',
     'Use both: automated monitoring plus community alerts as backup.'),
    ('Technically no \u2014 but in practice',
     'Technically no, but in practice'),
    ('FATCA reporting requirements \u2014 a fiscal representative',
     'FATCA reporting requirements. A fiscal representative'),
    ('tax identification number \u2014 you need it',
     'tax identification number. You need it'),
    ('international health insurance \u2014 options include',
     'international health insurance: options include'),
    ('language test \u2014 equivalent to basic conversational ability.',
     'language test, equivalent to basic conversational ability.'),
    ('regardless of residence \u2014 you must continue filing US taxes.',
     'regardless of residence. You must continue filing US taxes.'),
    ('(SNS \u2014 Servi\u00e7o Nacional de Sa\u00fade)',
     '(SNS, Servi\u00e7o Nacional de Sa\u00fade)'),
    # EU citizenship card em dash (fallback if block replace missed it)
    ('Portuguese passport \u2014 live and work anywhere in the EU.',
     'Portuguese passport. Live and work anywhere in the EU.'),
    # Healthcare card em dash (fallback)
    ('\u20ac400\u20131,200/year \u2014 not $40,000.',
     '\u20ac400\u20131,200/year, not $40,000.'),
]

for old, new in emdash_replacements:
    if old in html:
        html = html.replace(old, new)
        print(f'EM DASH OK: {old[:55]}')
    else:
        print(f'EM DASH SKIP (not found): {old[:55]}')

# === CHANGE D: Currency equivalents ===
html = html.replace(
    'Monthly income: \u20ac3,480+ (\u2248$3,750 USD)',
    'Monthly income: \u20ac3,480+ (approx. $3,750 USD / \u00a32,950 GBP)'
)
html = html.replace(
    'Monthly income: \u20ac920+ (\u2248$1,000 USD)',
    'Monthly income: \u20ac920+ (approx. $990 USD / \u00a3780 GBP)'
)
html = html.replace(
    '<div class="price-amount">\u20ac199</div>',
    '<div class="price-amount">\u20ac199</div>\n        <div class="price-equiv" style="font-size:0.78rem;color:var(--muted);margin-bottom:4px">approx. $215 / \u00a3170</div>'
)
html = html.replace(
    '<div class="price-amount">\u20ac599</div>',
    '<div class="price-amount">\u20ac599</div>\n        <div class="price-equiv" style="font-size:0.78rem;color:var(--muted);margin-bottom:4px">approx. $645 / \u00a3510</div>'
)
html = html.replace(
    '<div class="price-amount">\u20ac999</div>',
    '<div class="price-amount">\u20ac999</div>\n        <div class="price-equiv" style="font-size:0.78rem;color:var(--muted);margin-bottom:4px">approx. $1,075 / \u00a3850</div>'
)
# Remove any remaining ≈
html = html.replace('\u2248', 'approx. ')
print('CURRENCY: done')

# === CHANGE E: Dora 24/7 pitch ===
old_hero = ('    <p>AI-guided visa advisory, from your first question to your residence permit</p>\n'
            '    <a href="https://joseph-app.onrender.com" class="btn-primary">Talk to Dora. It\u2019s Free \u2192</a>')
new_hero = ('    <p>AI-guided visa advisory, from your first question to your residence permit</p>\n'
            '    <p>Dora is available 24 hours a day, 365 days a year. No office hours. No waiting for Monday morning. If you are in California and it is midnight, Dora is ready.</p>\n'
            '    <a href="https://joseph-app.onrender.com" class="btn-primary">Talk to Dora. It\u2019s Free \u2192</a>')
if old_hero in html:
    html = html.replace(old_hero, new_hero)
    print('DORA 24/7: added')
else:
    print('DORA 24/7: NOT FOUND - check manually')

# === CHANGE F: Final CTA background ===
html = html.replace(
    "url('images/sunset-beach.jpg')",
    "url('images/lifestyle-footer.jpg')"
)
print('FINAL CTA IMAGE: done')

# === CHANGE G: American-only language ===
html = html.replace(
    'AI-guided Portugal visa advisory for Americans and British.',
    'AI-guided Portugal visa advisory for English-speaking expats.'
)
html = html.replace(
    'Americans living in Portugal',
    'English-speaking expats living in Portugal'
)
html = html.replace(
    'Banks accepting Americans include',
    'Banks accepting expats include'
)
print('LANGUAGE: done')

# Verify no em dashes remain
remaining = html.count('\u2014')
print(f'\nRemaining em dashes in index.html: {remaining}')
if remaining > 0:
    for i, line in enumerate(html.split('\n'), 1):
        if '\u2014' in line:
            print(f'  Line {i}: {line.strip()[:100]}')

with open(r'C:\Users\Patrick\Documents\VisaWise\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nindex.html written. Size: {len(html)} chars (was {original_len})')

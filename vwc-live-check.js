const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1280, height: 900 }
  });

  await page.goto('https://visawiseconsultants.onrender.com');
  await page.waitForTimeout(5000);

  // Take full page screenshot
  await page.screenshot({
    path: 'vwc-live-check.png',
    fullPage: false
  });

  // Check for em dashes
  const bodyText = await page.innerText('body');
  const emDashes = (bodyText.match(/\u2014/g) || []).length;

  // Check logo
  const logoSrc = await page.$eval(
    'nav img, header img',
    el => el.src
  ).catch(() => 'logo not found');

  // Check for Francisco
  const hasFrancisco = bodyText.includes('Francisco');

  // Check for 5 year citizenship
  const hasFiveYear = bodyText.includes('five years') ||
                      bodyText.includes('5 years') ||
                      bodyText.includes('5-year');

  // Check section order - find pricing and blog
  const sections = await page.$$eval(
    'section, div[id]',
    els => els.map(el => el.id || el.className).filter(Boolean).slice(0, 20)
  );

  console.log('Em dashes found:', emDashes);
  console.log('Logo src:', logoSrc);
  console.log('Francisco still present:', hasFrancisco);
  console.log('5-year citizenship still present:', hasFiveYear);
  console.log('Page sections:', sections);

  await browser.close();
})();

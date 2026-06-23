// Regenerates the per-section page files from index.html (canonical source).
// Run this after any edit to index.html: `node build-pages.js`
const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, 'index.html');
const DEFAULT_TAB = 'garage';

const PAGES = [
  { file: 'dashboard.html',  href: '/dashboard',  tab: 'garage',      title: 'Dashboard' },
  { file: 'market.html',     href: '/market',     tab: 'market',      title: 'Market' },
  { file: 'auction.html',    href: '/auction',    tab: 'auction',     title: 'Auction' },
  { file: 'race.html',       href: '/race',       tab: 'race',        title: 'Race' },
  { file: 'challenges.html', href: '/challenges', tab: 'challenges',  title: 'Challenges' },
  { file: 'leaderboard.html',href: '/leaderboard',tab: 'leaderboard', title: 'Leaderboard' },
  { file: 'crew.html',       href: '/crew',       tab: 'crew',        title: 'Crew' },
  { file: 'chat.html',       href: '/chat',       tab: 'chat',        title: 'Chat' },
  { file: 'profile.html',    href: '/profile',    tab: 'profile',     title: 'Profile' },
  { file: 'admin.html',      href: '/admin',      tab: 'admin',       title: 'Admin' },
  { file: 'modforms.html',   href: '/modforms',   tab: 'modforms',    title: 'Mod Forms' },
];

const template = fs.readFileSync(SRC, 'utf8');

function hrefFor(tab) {
  const page = PAGES.find(p => p.tab === tab);
  return page ? page.href : null;
}

for (const page of PAGES) {
  let out = template;

  if (page.tab !== DEFAULT_TAB) {
    out = out.replace(
      `class="section active" id="tab-${DEFAULT_TAB}"`,
      `class="section" id="tab-${DEFAULT_TAB}"`
    );
    out = out.replace(
      `class="section" id="tab-${page.tab}"`,
      `class="section active" id="tab-${page.tab}"`
    );

    const defaultHref = hrefFor(DEFAULT_TAB);
    const targetHref = hrefFor(page.tab);
    out = out.replace(
      `class="side-tab active" href="${defaultHref}"`,
      `class="side-tab" href="${defaultHref}"`
    );
    out = out.replace(
      new RegExp(`class="side-tab" (id="[^"]+" )?href="${targetHref}"`),
      (m, idAttr) => `class="side-tab active" ${idAttr || ''}href="${targetHref}"`
    );
  }

  out = out.replace(
    /<title>.*?<\/title>/,
    `<title>REDLINE: Vice Streets — ${page.title}</title>`
  );

  fs.writeFileSync(path.join(__dirname, page.file), out);
  console.log('Wrote', page.file);
}

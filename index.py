python3 << 'PYEOF'
html = r'''


<meta>
<meta>
<title>REDLINE</title>
<link>
<link>
<style>
:root{
  --bg:#08080f;--bg2:#0c0c16;--bg3:#10101a;
  --panel:#13131e;--panel2:#171724;--panel3:#1c1c2c;
  --border:#1a1a2e;--border2:#222238;--border3:#2a2a48;
  --red:#c41e1e;--red2:#e03030;--red3:rgba(196,30,30,.14);--red4:rgba(196,30,30,.07);
  --amber:#b86e18;--amber2:#e08c28;--amber3:rgba(184,110,24,.12);
  --green:#167832;--green2:#1ea844;--green3:rgba(22,120,50,.14);
  --blue:#163878;--blue2:#2e6acc;--blue3:rgba(22,56,120,.14);
  --purple:#4a1e7e;--purple2:#7a3ecc;--purple3:rgba(74,30,126,.14);
  --steel:#3a4a6a;--steel2:#6a8ab8;--steel3:rgba(58,74,106,.14);
  --text:#dcdcec;--text2:#9898b8;--text3:#585878;--text4:#303050;
  --disp:'Rajdhani',sans-serif;
  --mono:'JetBrains Mono',monospace;
  --body:'Inter',sans-serif;
  --r:8px;--r2:12px;--r3:18px;
  --shadow:0 4px 24px rgba(0,0,0,.5);
  --glow-red:0 0 24px rgba(196,30,30,.25);
}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--body);font-size:14px;line-height:1.5;overflow-x:hidden;}
::-webkit-scrollbar{width:4px;height:4px;}
::-webkit-scrollbar-track{background:var(--bg2);}
::-webkit-scrollbar-thumb{background:var(--border3);border-radius:2px;}
::selection{background:var(--red3);color:var(--red2);}

/* ─── TYPOGRAPHY ─── */
h1,h2,h3{font-family:var(--disp);font-weight:700;letter-spacing:.5px;}
.sec-title{font-family:var(--disp);font-size:28px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--text);margin-bottom:2px;}
.sec-sub{font-family:var(--mono);font-size:10px;letter-spacing:2px;color:var(--text3);text-transform:uppercase;margin-bottom:20px;}
.mono{font-family:var(--mono);}
.disp{font-family:var(--disp);}

/* ─── AUTH ─── */
#auth-screen{
  display:flex;align-items:center;justify-content:center;
  min-height:100vh;
  background:
    radial-gradient(ellipse at 20% 10%,rgba(196,30,30,.1) 0%,transparent 55%),
    radial-gradient(ellipse at 80% 90%,rgba(74,30,126,.08) 0%,transparent 55%),
    var(--bg);
}
.auth-wrap{width:100%;max-width:420px;padding:24px;}
.auth-brand{text-align:center;margin-bottom:36px;}
.auth-wordmark{
  font-family:var(--disp);font-size:58px;font-weight:700;
  letter-spacing:8px;line-height:1;
  background:linear-gradient(135deg,var(--red2),var(--amber2));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  filter:drop-shadow(0 0 30px rgba(196,30,30,.35));
}
.auth-tagline{font-family:var(--mono);font-size:10px;letter-spacing:4px;color:var(--text3);margin-top:8px;text-transform:uppercase;}
.auth-dots{display:flex;justify-content:center;gap:6px;margin-top:12px;}
.auth-dot{width:5px;height:5px;border-radius:50%;background:var(--border2);}
.auth-dot:nth-child(2){background:var(--red2);}
.auth-card{
  background:var(--panel);
  border:1px solid var(--border2);
  border-radius:var(--r3);
  overflow:hidden;
  box-shadow:var(--shadow);
}
.auth-tabs{display:flex;border-bottom:1px solid var(--border);}
.auth-tab{
  flex:1;padding:15px;
  font-family:var(--disp);font-size:14px;font-weight:600;
  letter-spacing:1.5px;text-transform:uppercase;
  border:none;background:transparent;color:var(--text3);
  cursor:pointer;transition:all .2s;
}
.auth-tab.active{color:var(--red2);background:var(--red4);border-bottom:2px solid var(--red2);}
.auth-tab:hover:not(.active){color:var(--text2);}
.auth-body{padding:28px;}
.form-grp{margin-bottom:18px;}
.form-lbl{
  display:block;font-family:var(--mono);font-size:9px;
  letter-spacing:2px;color:var(--text3);text-transform:uppercase;margin-bottom:7px;
}
.form-inp{
  width:100%;padding:12px 15px;
  background:var(--bg3);border:1px solid var(--border2);
  border-radius:var(--r);color:var(--text);
  font-family:var(--body);font-size:14px;outline:none;
  transition:border .2s,box-shadow .2s;
}
.form-inp:focus{border-color:var(--red2);box-shadow:0 0 0 3px var(--red4);}
.form-inp::placeholder{color:var(--text4);}
.form-inp option{background:var(--bg2);}
.auth-msg{
  padding:11px 15px;border-radius:var(--r);
  font-size:12px;margin-bottom:16px;display:none;line-height:1.5;
}
.auth-msg.err{background:var(--red3);border:1px solid rgba(196,30,30,.25);color:#ff9999;}
.auth-msg.ok{background:var(--green3);border:1px solid rgba(22,120,50,.25);color:#99ffbb;}
.auth-msg.info{background:var(--steel3);border:1px solid rgba(58,74,106,.25);color:var(--steel2);}

/* ─── BUTTONS ─── */
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:6px;
  padding:10px 20px;border:none;border-radius:var(--r);
  font-family:var(--disp);font-size:13px;font-weight:600;letter-spacing:.5px;
  cursor:pointer;transition:all .15s;white-space:nowrap;text-decoration:none;
}
.btn:disabled{opacity:.35;cursor:not-allowed;transform:none!important;filter:none!important;}
.btn-red{background:linear-gradient(135deg,var(--red),var(--red2));color:#fff;box-shadow:0 2px 12px rgba(196,30,30,.25);}
.btn-red:hover:not(:disabled){filter:brightness(1.12);transform:translateY(-1px);box-shadow:0 4px 20px rgba(196,30,30,.35);}
.btn-gold{background:linear-gradient(135deg,var(--amber),var(--amber2));color:#fff;box-shadow:0 2px 12px rgba(184,110,24,.2);}
.btn-gold:hover:not(:disabled){filter:brightness(1.1);transform:translateY(-1px);}
.btn-ghost{background:transparent;border:1px solid var(--border2);color:var(--text2);}
.btn-ghost:hover:not(:disabled){border-color:var(--border3);color:var(--text);background:var(--panel2);}
.btn-green{background:linear-gradient(135deg,var(--green),var(--green2));color:#fff;}
.btn-green:hover:not(:disabled){filter:brightness(1.1);transform:translateY(-1px);}
.btn-steel{background:var(--steel3);border:1px solid rgba(58,74,106,.3);color:var(--steel2);}
.btn-steel:hover:not(:disabled){background:var(--steel);color:#fff;}
.btn-purple{background:var(--purple3);border:1px solid rgba(74,30,126,.3);color:var(--purple2);}
.btn-purple:hover:not(:disabled){background:var(--purple);color:#fff;}
.btn-blue{background:var(--blue3);border:1px solid rgba(22,56,120,.3);color:var(--blue2);}
.btn-blue:hover:not(:disabled){background:var(--blue);color:#fff;}
.btn-sm{padding:5px 12px;font-size:11px;}
.btn-lg{padding:14px 28px;font-size:15px;width:100%;}
.btn-icon{padding:8px;width:34px;height:34px;border-radius:50%;}

/* ─── LAYOUT ─── */
#game{display:none;flex-direction:column;min-height:100vh;}

/* ─── HUD ─── */
.hud{
  position:sticky;top:0;z-index:100;height:56px;
  display:flex;align-items:center;gap:0;padding:0 16px;
  background:rgba(8,8,15,.96);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border);
}
.hud-logo{
  font-family:var(--disp);font-size:24px;font-weight:700;
  letter-spacing:4px;color:var(--red2);
  text-shadow:0 0 20px rgba(196,30,30,.4);
  margin-right:20px;flex-shrink:0;cursor:pointer;
}
.nav-bar{display:flex;gap:1px;flex:1;overflow-x:auto;scrollbar-width:none;}
.nav-bar::-webkit-scrollbar{display:none;}
.nav-btn{
  padding:8px 15px;font-family:var(--disp);font-size:12px;
  font-weight:600;letter-spacing:1px;color:var(--text3);
  background:transparent;border:none;cursor:pointer;
  border-radius:var(--r);white-space:nowrap;
  transition:all .15s;position:relative;
}
.nav-btn.active{color:var(--red2);background:var(--red4);}
.nav-btn.active::after{content:'';position:absolute;bottom:-1px;left:8px;right:8px;height:2px;background:var(--red2);border-radius:2px;}
.nav-btn:hover:not(.active){color:var(--text);background:var(--panel2);}
.hud-right{display:flex;align-items:center;gap:8px;flex-shrink:0;margin-left:12px;}
.hud-pill{
  display:flex;align-items:center;gap:5px;
  padding:5px 11px;background:var(--panel2);
  border:1px solid var(--border);border-radius:20px;
  font-family:var(--mono);font-size:11px;cursor:default;
}
.hud-cash{color:var(--amber2);font-weight:700;}
.hud-lv{color:var(--steel2);}
.av-wrap{position:relative;}
.av-btn{
  width:36px;height:36px;border-radius:50%;
  background:linear-gradient(135deg,var(--red),var(--purple2));
  border:2px solid var(--border2);color:#fff;
  font-family:var(--disp);font-size:15px;font-weight:700;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:box-shadow .2s;
}
.av-btn:hover{box-shadow:0 0 0 3px var(--red3);}

/* ─── HUD DROPDOWN ─── */
.hud-menu{
  position:absolute;top:calc(100% + 10px);right:0;
  background:var(--panel);border:1px solid var(--border2);
  border-radius:var(--r2);min-width:210px;overflow:hidden;
  display:none;z-index:200;box-shadow:0 8px 40px rgba(0,0,0,.5);
}
.hud-menu.open{display:block;}
.menu-head{padding:15px 18px;background:var(--panel2);border-bottom:1px solid var(--border);}
.menu-uname{font-family:var(--disp);font-size:16px;font-weight:700;margin-bottom:3px;}
.menu-itm{
  display:flex;align-items:center;gap:9px;
  padding:11px 18px;font-size:13px;color:var(--text2);
  cursor:pointer;transition:all .15s;
  border:none;background:transparent;width:100%;text-align:left;
}
.menu-itm:hover{background:var(--panel2);color:var(--text);}
.menu-div{height:1px;background:var(--border);margin:4px 0;}

/* ─── TICKER ─── */
.ticker{
  background:var(--panel);border-bottom:1px solid var(--border);
  height:30px;overflow:hidden;position:relative;
}
.ticker::before,.ticker::after{
  content:'';position:absolute;top:0;bottom:0;width:80px;z-index:2;pointer-events:none;
}
.ticker::before{left:0;background:linear-gradient(to right,var(--panel),transparent);}
.ticker::after{right:0;background:linear-gradient(to left,var(--panel),transparent);}
.ticker-inner{
  display:flex;height:100%;align-items:center;
  animation:tickScroll 70s linear infinite;width:max-content;
}
.ticker-inner:hover{animation-play-state:paused;}
@keyframes tickScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.tick-item{
  flex-shrink:0;padding:0 22px;font-family:var(--mono);font-size:10px;
  display:flex;align-items:center;gap:8px;white-space:nowrap;
  border-right:1px solid var(--border);
}
.tick-up{color:var(--green2);}
.tick-dn{color:var(--red2);}
.tick-flat{color:var(--text3);}
.tick-name{color:var(--steel2);}
.tick-price{color:var(--amber2);font-weight:700;}

/* ─── SECTIONS ─── */
.section{display:none;padding:28px 20px;max-width:1440px;margin:0 auto;width:100%;}
.section.active{display:block;}
.sec-hdr{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px;flex-wrap:wrap;gap:12px;}
.sec-hdr-r{display:flex;gap:8px;align-items:center;flex-wrap:wrap;}

/* ─── CARDS ─── */
.card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:18px;position:relative;overflow:hidden;}
.card-sm{padding:12px;}
.card-lg{padding:24px;}
.card-hover{transition:border .2s,transform .2s,box-shadow .2s;}
.card-hover:hover{border-color:var(--border3);transform:translateY(-2px);box-shadow:var(--shadow);}

/* ─── BADGES ─── */
.badge{
  display:inline-flex;align-items:center;
  padding:2px 8px;border-radius:4px;
  font-family:var(--mono);font-size:9px;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;
}
.badge-common{background:rgba(90,90,130,.15);color:#8888b0;border:1px solid rgba(90,90,130,.2);}
.badge-rare{background:var(--blue3);color:var(--blue2);border:1px solid rgba(22,56,120,.25);}
.badge-epic{background:var(--purple3);color:var(--purple2);border:1px solid rgba(74,30,126,.25);}
.badge-legendary{background:var(--amber3);color:var(--amber2);border:1px solid rgba(184,110,24,.25);}
.badge-mythic{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.25);}
.badge-green{background:var(--green3);color:var(--green2);border:1px solid rgba(22,120,50,.25);}
.badge-red{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.25);}
.badge-steel{background:var(--steel3);color:var(--steel2);border:1px solid rgba(58,74,106,.25);}
.badge-gold{background:var(--amber3);color:var(--amber2);border:1px solid rgba(184,110,24,.25);}

/* ─── ROLE BADGES ─── */
.role-badge{
  display:inline-flex;align-items:center;padding:2px 8px;
  border-radius:4px;font-family:var(--mono);font-size:9px;
  font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
}
.role-owner{background:rgba(74,30,126,.2);color:var(--purple2);border:1px solid rgba(74,30,126,.35);}
.role-admin{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.3);}
.role-moderator{background:var(--amber3);color:var(--amber2);border:1px solid rgba(184,110,24,.3);}
.role-player{background:var(--steel3);color:var(--steel2);border:1px solid rgba(58,74,106,.3);}
.role-npc{background:var(--panel2);color:var(--text3);border:1px solid var(--border2);}

/* ─── RARITY STRIPS ─── */
.rar-strip{position:absolute;bottom:0;left:0;right:0;height:3px;}
.rar-common{background:rgba(90,90,130,.5);}
.rar-rare{background:linear-gradient(90deg,var(--blue),var(--blue2));}
.rar-epic{background:linear-gradient(90deg,var(--purple),var(--purple2));}
.rar-legendary{background:linear-gradient(90deg,var(--amber),var(--amber2));}
.rar-mythic{background:linear-gradient(90deg,var(--red),var(--red2),var(--amber2));}

/* ─── GRIDS ─── */
.g2{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.ga{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;}
.ga-lg{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px;}
@media(max-width:900px){
  .g2,.g3,.g4{grid-template-columns:1fr;}
  .garage-layout{grid-template-columns:1fr!important;}
}
@media(max-width:640px){
  .ga{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));}
  .ga-lg{grid-template-columns:1fr;}
  .hide-xs{display:none!important;}
}

/* ─── CAR CARD ─── */
.car-card{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:16px;cursor:pointer;
  position:relative;overflow:hidden;
  transition:all .2s;
}
.car-card:hover{border-color:var(--red2);transform:translateY(-3px);box-shadow:0 8px 32px rgba(196,30,30,.12);}
.car-card.selected{border-color:var(--red2);background:var(--panel2);box-shadow:0 0 0 2px rgba(196,30,30,.2),0 8px 32px rgba(196,30,30,.12);}
.car-emoji{font-size:46px;line-height:1;margin:8px 0 10px;display:block;filter:drop-shadow(0 2px 10px rgba(0,0,0,.5));}
.car-name{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.5px;margin-bottom:3px;}
.car-brand{font-family:var(--mono);font-size:9px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;}
.car-tag{
  position:absolute;top:10px;right:10px;
  background:var(--red);color:#fff;
  font-family:var(--mono);font-size:8px;font-weight:700;
  letter-spacing:1.5px;padding:3px 8px;border-radius:4px;
}
.car-fav{position:absolute;top:10px;left:10px;font-size:14px;}
.price-tag{font-family:var(--disp);font-size:20px;font-weight:700;color:var(--amber2);}
.delta{font-family:var(--mono);font-size:9px;}
.delta-up{color:var(--green2);}
.delta-dn{color:var(--red2);}

/* ─── STAT BARS ─── */
.stat-row{display:flex;align-items:center;gap:8px;margin-bottom:9px;}
.stat-lbl{font-family:var(--mono);font-size:9px;letter-spacing:1px;color:var(--text3);width:64px;flex-shrink:0;text-transform:uppercase;}
.stat-bg{flex:1;height:5px;background:var(--bg3);border-radius:3px;overflow:hidden;}
.stat-fill{height:100%;border-radius:3px;transition:width .6s cubic-bezier(.2,.8,.3,1);}
.stat-val{font-family:var(--mono);font-size:10px;color:var(--text2);width:56px;text-align:right;flex-shrink:0;}

/* ─── DEMAND BAR ─── */
.dem-wrap{margin-bottom:10px;}
.dem-hdr{display:flex;justify-content:space-between;font-family:var(--mono);font-size:9px;color:var(--text3);margin-bottom:4px;}
.dem-bar{height:3px;background:var(--bg3);border-radius:2px;overflow:hidden;}
.dem-fill{height:100%;border-radius:2px;transition:width .6s;}

/* ─── RACE SECTION ─── */
.race-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;}
.race-card{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:20px;cursor:pointer;
  position:relative;overflow:hidden;
  transition:all .2s;display:flex;flex-direction:column;
}
.race-card::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,transparent 50%,rgba(196,30,30,.04));
  pointer-events:none;
}
.race-card:hover{border-color:var(--red2);transform:translateY(-3px);box-shadow:0 10px 36px rgba(196,30,30,.14);}
.race-emoji{font-size:38px;line-height:1;margin-bottom:10px;display:block;}
.race-name{font-family:var(--disp);font-size:20px;font-weight:700;letter-spacing:.5px;margin:6px 0 5px;}
.race-desc{font-size:12px;color:var(--text2);line-height:1.55;margin-bottom:16px;flex:1;}
.race-foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:auto;}
.race-reward{font-family:var(--disp);font-size:18px;font-weight:700;color:var(--amber2);}
.race-xp{font-family:var(--mono);font-size:9px;color:var(--text3);margin-top:2px;}
.diff-pip{
  display:inline-flex;align-items:center;gap:4px;
  padding:3px 9px;border-radius:4px;
  font-family:var(--mono);font-size:8px;font-weight:700;letter-spacing:2px;
}
.pip-easy{background:var(--green3);color:var(--green2);border:1px solid rgba(22,120,50,.25);}
.pip-med{background:var(--amber3);color:var(--amber2);border:1px solid rgba(184,110,24,.25);}
.pip-hard{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.25);}
.pip-elite{background:var(--purple3);color:var(--purple2);border:1px solid rgba(74,30,126,.25);}

/* ─── RACE ARENA ─── */
#race-arena{
  display:none;position:fixed;inset:0;z-index:300;
  flex-direction:column;align-items:center;justify-content:flex-start;
  padding:24px 20px;overflow-y:auto;
  background:rgba(4,4,10,.96);backdrop-filter:blur(12px);
}
.arena-hdr{width:100%;max-width:720px;display:flex;justify-content:space-between;align-items:center;margin-bottom:28px;}
.arena-title{font-family:var(--disp);font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;}
.arena-badge{
  padding:5px 16px;border-radius:20px;
  font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:2px;
}
.ab-ready{background:var(--steel3);color:var(--steel2);border:1px solid rgba(58,74,106,.3);}
.ab-countdown{background:var(--amber3);color:var(--amber2);border:1px solid rgba(184,110,24,.3);}
.ab-racing{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.3);animation:blink 1s infinite;}
.ab-victory{background:var(--green3);color:var(--green2);border:1px solid rgba(22,120,50,.3);}
.ab-defeat{background:var(--red3);color:var(--red2);border:1px solid rgba(196,30,30,.3);}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.5}}
.track-wrap{width:100%;max-width:720px;margin-bottom:20px;}
.track-lane{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:16px 18px;
  position:relative;overflow:hidden;margin-bottom:10px;
}
.track-lines{
  position:absolute;inset:0;
  background:repeating-linear-gradient(90deg,transparent,transparent 38px,rgba(255,255,255,.015) 38px,rgba(255,255,255,.015) 39px);
  pointer-events:none;
}
.lane-lbl{font-family:var(--mono);font-size:9px;letter-spacing:1.5px;color:var(--text3);text-transform:uppercase;margin-bottom:9px;}
.lane-track{height:10px;background:var(--bg3);border-radius:5px;position:relative;overflow:hidden;}
.lane-fill{height:100%;width:0%;border-radius:5px;transition:width 2.6s cubic-bezier(.08,.82,.17,1);}
.lf-player{background:linear-gradient(90deg,#8b0000,var(--red2),var(--amber2));}
.lf-opp{background:linear-gradient(90deg,#1a2a4a,var(--steel),var(--blue2));}
.lane-car{
  position:absolute;top:50%;transform:translateY(-50%);
  font-size:28px;z-index:5;line-height:1;
  filter:drop-shadow(0 0 10px rgba(196,30,30,.6));
  transition:left 2.6s cubic-bezier(.08,.82,.17,1);
  left:2%;
}
.lane-score{font-family:var(--mono);font-size:10px;color:var(--text3);margin-top:7px;text-align:right;}
.phase-num{
  font-family:var(--disp);font-size:96px;font-weight:700;
  color:var(--red2);text-align:center;line-height:1;
  text-shadow:0 0 60px rgba(196,30,30,.5);
  animation:phaseIn .35s ease;
  display:none;
}
.phase-go{color:var(--green2);text-shadow:0 0 60px rgba(22,168,68,.5);}
@keyframes phaseIn{from{transform:scale(1.8);opacity:0}to{transform:scale(1);opacity:1}}
.scoreboard{
  display:none;width:100%;max-width:720px;
  grid-template-columns:1fr 60px 1fr;
  gap:12px;align-items:center;margin-bottom:20px;
}
.score-box{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:16px;text-align:center;
  transition:all .3s;
}
.score-box.winner{border-color:var(--green2);background:rgba(22,120,50,.07);box-shadow:0 0 20px rgba(22,168,68,.1);}
.score-box.loser{border-color:var(--red2);background:rgba(196,30,30,.05);}
.score-vs{font-family:var(--disp);font-size:28px;font-weight:700;color:var(--text3);text-align:center;}
.score-name{font-family:var(--mono);font-size:9px;color:var(--text3);letter-spacing:1px;text-transform:uppercase;margin-bottom:5px;}
.score-val{font-family:var(--disp);font-size:34px;font-weight:700;}
.result-wrap{width:100%;max-width:720px;border-radius:var(--r2);padding:28px;text-align:center;}
.result-win{background:linear-gradient(135deg,rgba(22,120,50,.12),rgba(22,120,50,.04));border:1px solid rgba(22,168,68,.3);}
.result-lose{background:linear-gradient(135deg,rgba(196,30,30,.09),rgba(196,30,30,.03));border:1px solid rgba(196,30,30,.2);}
.result-title{font-family:var(--disp);font-size:42px;font-weight:700;letter-spacing:4px;text-transform:uppercase;margin-bottom:20px;}
.result-rewards{display:flex;justify-content:center;gap:28px;margin-bottom:16px;flex-wrap:wrap;}
.rew-itm{text-align:center;}
.rew-val{font-family:var(--disp);font-size:26px;font-weight:700;}
.rew-lbl{font-family:var(--mono);font-size:9px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-top:3px;}
.result-tip{
  margin-top:14px;padding:11px 16px;
  background:var(--panel2);border:1px solid var(--border);
  border-radius:var(--r);font-family:var(--mono);
  font-size:11px;color:var(--text2);text-align:left;line-height:1.6;
}
.result-actions{display:flex;gap:10px;justify-content:center;margin-top:18px;flex-wrap:wrap;}

/* ─── GARAGE ─── */
.garage-layout{display:grid;grid-template-columns:1fr 340px;gap:20px;align-items:start;}
.sb{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:22px;
  position:sticky;top:76px;max-height:calc(100vh - 96px);overflow-y:auto;
}
.sb-emoji{font-size:68px;text-align:center;display:block;margin:10px 0 14px;filter:drop-shadow(0 4px 18px rgba(196,30,30,.2));}
.sb-name{font-family:var(--disp);font-size:23px;font-weight:700;letter-spacing:.5px;text-align:center;margin-bottom:6px;}
.upg-tab{
  padding:6px 13px;font-family:var(--mono);font-size:10px;
  font-weight:700;letter-spacing:1px;
  border:1px solid var(--border2);background:transparent;
  color:var(--text3);border-radius:var(--r);cursor:pointer;transition:all .15s;
}
.upg-tab.active{border-color:var(--red2);color:var(--red2);background:var(--red4);}
.upg-item{
  display:flex;justify-content:space-between;align-items:center;
  padding:13px;background:var(--panel2);
  border:1px solid var(--border);border-radius:var(--r);
  margin-bottom:8px;gap:10px;
  transition:border .15s;
}
.upg-item:hover{border-color:var(--border3);}
.upg-name{font-family:var(--disp);font-size:13px;font-weight:600;letter-spacing:.3px;margin-bottom:3px;}
.upg-meta{font-family:var(--mono);font-size:9px;color:var(--text3);}
.upg-dots{display:flex;gap:4px;margin-top:6px;}
.upg-dot{width:9px;height:9px;border-radius:50%;background:var(--border3);border:1px solid var(--border2);}
.upg-dot.on{background:var(--red2);border-color:var(--red);box-shadow:0 0 6px rgba(196,30,30,.4);}

/* ─── MARKET ─── */
.filter-bar{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:16px;}
.f-btn{
  padding:6px 14px;font-family:var(--mono);font-size:10px;font-weight:600;
  letter-spacing:1px;border:1px solid var(--border2);
  background:transparent;color:var(--text3);
  border-radius:20px;cursor:pointer;transition:all .15s;white-space:nowrap;
}
.f-btn.active{border-color:var(--red2);color:var(--red2);background:var(--red4);}
.f-btn:hover:not(.active){border-color:var(--border3);color:var(--text);}
.mkt-ctrl{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:16px;}
.srch{
  padding:9px 15px;background:var(--panel2);
  border:1px solid var(--border2);border-radius:var(--r);
  color:var(--text);font-family:var(--body);font-size:13px;
  outline:none;transition:border .2s;min-width:200px;
}
.srch:focus{border-color:var(--red2);}
.srch::placeholder{color:var(--text4);}
.sort-sel{
  padding:9px 14px;background:var(--panel2);
  border:1px solid var(--border2);border-radius:var(--r);
  color:var(--text);font-family:var(--mono);font-size:11px;
  outline:none;cursor:pointer;
}
.sort-sel option{background:var(--bg2);}

/* ─── AUCTION ─── */
.auc-card{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r2);padding:20px;
  position:relative;overflow:hidden;
  transition:all .2s;
}
.auc-card:hover{border-color:var(--border3);}
.auc-timer{
  font-family:var(--mono);font-size:11px;font-weight:700;
  padding:3px 11px;border-radius:20px;
  background:var(--steel3);color:var(--steel2);
  border:1px solid rgba(58,74,106,.25);
}
.auc-timer.urgent{
  background:var(--red3);color:var(--red2);
  border-color:rgba(196,30,30,.3);animation:blink 1s infinite;
}
.auc-price{font-family:var(--disp);font-size:28px;font-weight:700;color:var(--amber2);margin:8px 0 3px;}
.auc-bids{font-family:var(--mono);font-size:10px;color:var(--text3);}
.auc-event{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:2px;color:var(--amber2);margin-bottom:10px;}
.winning-tag{
  position:absolute;top:12px;right:12px;
  background:var(--green3);border:1px solid rgba(22,120,50,.3);
  color:var(--green2);font-family:var(--mono);
  font-size:8px;font-weight:700;letter-spacing:1px;
  padding:3px 8px;border-radius:4px;
}
.bid-row{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--border);font-size:12px;}
.bid-amt{font-family:var(--mono);color:var(--amber2);font-weight:700;}

/* ─── LEADERBOARD ─── */
.lb-tabs{display:flex;gap:7px;margin-bottom:18px;flex-wrap:wrap;}
.lb-tab{
  padding:8px 18px;font-family:var(--mono);font-size:10px;
  font-weight:700;letter-spacing:1px;
  border:1px solid var(--border2);background:transparent;
  color:var(--text3);border-radius:var(--r);cursor:pointer;transition:all .15s;
}
.lb-tab.active{border-color:var(--amber2);color:var(--amber2);background:var(--amber3);}
.lb-tbl{width:100%;border-collapse:collapse;}
.lb-tbl th{
  font-family:var(--mono);font-size:9px;letter-spacing:2px;
  color:var(--text3);text-transform:uppercase;
  padding:9px 14px;border-bottom:1px solid var(--border);text-align:left;
}
.lb-tbl td{padding:13px 14px;border-bottom:1px solid var(--border);font-size:13px;}
.lb-tbl tr:hover td{background:var(--panel2);}
.lb-tbl tr.me td{background:rgba(196,30,30,.04);}
.lb-rank{font-family:var(--disp);font-size:20px;font-weight:700;width:50px;}
.lb-val{font-family:var(--mono);font-size:13px;font-weight:700;color:var(--amber2);text-align:right;}

/* ─── PROFILE ─── */
.prof-hero{
  background:linear-gradient(135deg,rgba(196,30,30,.07),rgba(74,30,126,.05));
  border:1px solid var(--border);border-radius:var(--r3);
  padding:30px;margin-bottom:22px;
  display:flex;gap:22px;align-items:center;flex-wrap:wrap;
}
.prof-av{
  width:76px;height:76px;border-radius:50%;flex-shrink:0;
  background:linear-gradient(135deg,var(--red),var(--purple2));
  display:flex;align-items:center;justify-content:center;
  font-family:var(--disp);font-size:34px;font-weight:700;color:#fff;
  box-shadow:0 0 0 3px rgba(196,30,30,.2),0 4px 20px rgba(0,0,0,.4);
}
.prof-name{font-family:var(--disp);font-size:30px;font-weight:700;letter-spacing:1px;margin-bottom:5px;}
.xp-wrap{height:7px;background:var(--bg3);border-radius:4px;margin:9px 0 4px;overflow:hidden;}
.xp-fill{height:100%;background:linear-gradient(90deg,var(--red),var(--amber2));border-radius:4px;transition:width .8s ease;}
.prof-sg{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:12px;margin-top:18px;}
.prof-stat{background:var(--panel);border:1px solid var(--border);border-radius:var(--r);padding:14px;text-align:center;}
.ps-v{font-family:var(--disp);font-size:26px;font-weight:700;color:var(--amber2);}
.ps-l{font-family:var(--mono);font-size:9px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-top:3px;}

/* ─── ACHIEVEMENTS ─── */
.ach-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px;}
.ach-card{
  background:var(--panel);border:1px solid var(--border);
  border-radius:var(--r);padding:14px;
  display:flex;gap:12px;align-items:flex-start;
  transition:all .2s;
}
.ach-card.earned{border-color:rgba(184,110,24,.35);background:var(--amber3);}
.ach-icon{font-size:30px;line-height:1;flex-shrink:0;}
.ach-name{font-family:var(--disp);font-size:14px;font-weight:700;letter-spacing:.3px;margin-bottom:3px;}
.ach-desc{font-family:var(--mono);font-size:9px;color:var(--text3);line-height:1.5;}

/* ─── CHALLENGES ─── */
.ch-item{
  display:flex;gap:14px;align-items:center;
  padding:15px;background:var(--panel);
  border:1px solid var(--border);border-radius:var(--r2);
  margin-bottom:9px;
}
.ch-icon{font-size:30px;flex-shrink:0;}
.ch-info{flex:1;}
.ch-name{font-family:var(--disp);font-size:15px;font-weight:700;letter-spacing:.3px;margin-bottom:2px;}
.ch-prog{height:4px;background:var(--bg3);border-radius:2px;overflow:hidden;margin-top:7px;}
.ch-fill{height:100%;background:linear-gradient(90deg,var(--red),var(--amber2));border-radius:2px;transition:width .5s;}

/* ─── DAILY BANNER ─── */
.daily-wrap{
  position:fixed;bottom:-140px;left:50%;transform:translateX(-50%);z-index:400;
  background:var(--panel);
  border:1px solid rgba(184,110,24,.4);
  border-radius:var(--r2);padding:22px 26px;
  width:calc(100% - 32px);max-width:450px;
  box-shadow:0 -4px 48px rgba(0,0,0,.6);
  transition:bottom .45s cubic-bezier(.2,.8,.3,1);
}
.daily-wrap.show{bottom:24px;}
.daily-title{font-family:var(--disp);font-size:20px;font-weight:700;letter-spacing:1px;color:var(--amber2);margin-bottom:2px;}
.daily-amt{
  font-family:var(--disp);font-size:42px;font-weight:700;color:var(--amber2);
  text-shadow:0 0 24px rgba(184,110,24,.4);line-height:1.1;
}
.daily-days{display:flex;gap:7px;margin:12px 0;}
.d-day{
  width:34px;height:34px;border-radius:50%;
  border:1px solid var(--border2);
  display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:10px;font-weight:700;color:var(--text3);
}
.d-day.done{background:var(--green3);border-color:rgba(22,120,50,.4);color:var(--green2);}
.d-day.today{background:var(--amber3);border-color:rgba(184,110,24,.4);color:var(--amber2);}

/* ─── MODALS ─── */
.modal-ov{
  display:none;position:fixed;inset:0;z-index:500;
  background:rgba(0,0,0,.75);backdrop-filter:blur(5px);
  align-items:flex-end;justify-content:center;padding:0;
}
@media(min-width:640px){.modal-ov{align-items:center;padding:20px;}}
.modal{
  background:var(--panel);border:1px solid var(--border2);
  border-radius:var(--r3) var(--r3) 0 0;
  width:100%;max-width:520px;max-height:92vh;
  overflow-y:auto;padding:26px;position:relative;
}
@media(min-width:640px){.modal{border-radius:var(--r3);}}
.modal-title{font-family:var(--disp);font-size:24px;font-weight:700;letter-spacing:.5px;margin-bottom:18px;}
.modal-x{
  position:absolute;top:22px;right:22px;
  background:transparent;border:none;color:var(--text3);
  font-size:22px;cursor:pointer;line-height:1;padding:2px;
  transition:color .15s;
}
.modal-x:hover{color:var(--text);}

/* ─── ADMIN ─── */
.admin-layout{display:grid;grid-template-columns:210px 1fr;gap:22px;align-items:start;}
@media(max-width:768px){.admin-layout{grid-template-columns:1fr;}}
.admin-nav{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:12px;position:sticky;top:76px;}
.adm-btn{
  display:flex;align-items:center;gap:9px;
  padding:10px 14px;border-radius:var(--r);
  font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.5px;
  color:var(--text3);cursor:pointer;transition:all .15s;
  border:none;background:transparent;width:100%;text-align:left;
}
.adm-btn.active{color:var(--red2);background:var(--red4);}
.adm-btn:hover:not(.active){color:var(--text);background:var(--panel2);}
.adm-sg{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin-bottom:22px;}
.adm-sc{background:var(--panel2);border:1px solid var(--border);border-radius:var(--r);padding:16px;text-align:center;}
.adm-sv{font-family:var(--disp);font-size:30px;font-weight:700;margin-bottom:3px;}
.adm-sl{font-family:var(--mono);font-size:9px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;}
.adm-tbl{width:100%;border-collapse:collapse;font-size:12px;}
.adm-tbl th{font-family:var(--mono);font-size:9px;letter-spacing:1.5px;color:var(--text3);text-transform:uppercase;padding:8px 11px;border-bottom:1px solid var(--border);text-align:left;white-space:nowrap;}
.adm-tbl td{padding:10px 11px;border-bottom:1px solid var(--border);vertical-align:middle;}
.adm-tbl tr:hover td{background:var(--panel2);}
.adm-srch{padding:8px 13px;background:var(--bg3);border:1px solid var(--border2);border-radius:var(--r);color:var(--text);font-family:var(--mono);font-size:11px;outline:none;transition:border .2s;}
.adm-srch:focus{border-color:var(--red2);}
.live-feed{background:var(--panel2);border:1px solid var(--border);border-radius:var(--r);padding:14px;max-height:320px;overflow-y:auto;}
.live-row{display:flex;gap:10px;padding:7px 0;border-bottom:1px solid var(--border);align-items:baseline;}
.live-time{font-family:var(--mono);font-size:9px;color:var(--text4);flex-shrink:0;width:48px;}
.log-act{color:var(--red2);font-weight:600;}
.adm-ctrl-card{padding:16px;background:var(--panel2);border:1px solid var(--border);border-radius:var(--r);margin-bottom:10px;}
.adm-ctrl-title{font-family:var(--disp);font-size:14px;font-weight:700;letter-spacing:.3px;margin-bottom:3px;}
.adm-ctrl-sub{font-size:11px;color:var(--text2);margin-bottom:10px;}

/* ─── TOASTS ─── */
#toast-wrap{position:fixed;top:68px;right:18px;z-index:600;display:flex;flex-direction:column;gap:9px;pointer-events:none;max-width:340px;}
.toast{
  padding:13px 17px;border-radius:var(--r);font-size:13px;
  pointer-events:auto;box-shadow:0 4px 24px rgba(0,0,0,.4);
  animation:toastIn .3s cubic-bezier(.2,.8,.3,1);
  transition:opacity .35s,transform .35s;line-height:1.45;
}
@keyframes toastIn{from{transform:translateX(110%);opacity:0}to{transform:translateX(0);opacity:1}}
.t-success{background:var(--green3);border:1px solid rgba(22,120,50,.3);color:#aaffcc;}
.t-error{background:var(--red3);border:1px solid rgba(196,30,30,.3);color:#ffaaaa;}
.t-info{background:var(--steel3);border:1px solid rgba(58,74,106,.3);color:var(--steel2);}
.t-gold{background:var(--amber3);border:1px solid rgba(184,110,24,.3);color:var(--amber2);}

/* ─── XP POP ─── */
.xp-pop{
  position:fixed;left:50%;transform:translateX(-50%);
  top:72px;z-index:700;pointer-events:none;
  font-family:var(--disp);font-size:22px;font-weight:700;
  color:var(--amber2);text-shadow:0 0 20px rgba(184,110,24,.5);
  animation:xpFloat 1.5s ease forwards;
}
@keyframes xpFloat{0%{opacity:0;transform:translateX(-50%) translateY(0)}15%{opacity:1}80%{opacity:1}100%{opacity:0;transform:translateX(-50%) translateY(-70px)}}

/* ─── NPC FEED ─── */
.npc-feed{position:fixed;bottom:90px;left:18px;z-index:100;max-width:290px;display:flex;flex-direction:column;gap:7px;pointer-events:none;}
.feed-item{
  padding:9px 13px;background:rgba(8,8,15,.92);
  border:1px solid var(--border);border-radius:var(--r);
  font-family:var(--mono);font-size:10px;color:var(--text2);
  backdrop-filter:blur(8px);
  animation:feedIn .3s ease;transition:opacity .3s;
}
.feed-item.fade{opacity:0;}
@keyframes feedIn{from{transform:translateX(-16px);opacity:0}to{transform:translateX(0);opacity:1}}

/* ─── MISC ─── */
.divider{height:1px;background:var(--border);margin:18px 0;}
.empty{text-align:center;padding:52px 20px;color:var(--text3);}
.empty-icon{font-size:52px;margin-bottom:14px;}
.loading{display:flex;align-items:center;justify-content:center;padding:52px;flex-direction:column;gap:14px;}
.spinner{width:34px;height:34px;border:3px solid var(--border2);border-top-color:var(--red2);border-radius:50%;animation:spin .7s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.pulse-dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:5px;vertical-align:middle;}
.section-divider{font-family:var(--mono);font-size:9px;letter-spacing:2.5px;color:var(--text3);text-transform:uppercase;margin:22px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--border);}
.info-row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--border);align-items:center;font-size:13px;}
.info-lbl{font-family:var(--mono);font-size:10px;color:var(--text3);}
.info-val{font-family:var(--mono);font-size:12px;color:var(--text);}
</style>





  
    
      REDLINE
      Street Racing · Live Economy · Auctions
      
        
      
    
    
      
        <button>Sign In</button>
        <button>Register
      
      
        
        
          <label>Username</label><input>
          <label>Password<input>
          <button>Start Engine 🚗
        
        
          <label>Username<input>
          <label>Email<input>
          <label>Password<input>
          <button>Create Account →
        
      
    
  





  
  <header>
    RL
    
      🏁 Race
      🔧 Garage
      🏪 Market
      🔨 Auction
      ⚡ Challenges
      🏆 Board
      🛡️ Admin
    
    
      
        $
        0
      
      
        LV
        1
      
      
        R
        
          
            Driver
            
          
          👤 Profile
          🎁 Daily Bonus
          🛡️ Admin Panel
          
          ⏻ Sign Out
        
      
    
  </header>

  
  
    ◆Loading market...
  

  
  
    
      
        Race Events
        Pick an event · Race · Earn cash
      
      
        
          🚗
          No Car
        
      
    
    
  

  
  
    
      
        My Garage
        0 cars owned
      
      
        <button>❤️ Favourite
        <button>🔑 Set Active
        <button>🔨 Auction
      
    
    
      
      
        
          
            🚗
            —
            —
          
          
          
            POWER BOOST+0 hp
          
          
            RATING—
          
          
          Upgrades
          
            <button>Engine
            <button>Performance
          
          
        
      
    
  

  
  
    
      
        Car Market
        Live prices · Dynamic demand
      
    
    
      <input>
      <select>
        Sort: Demand
        Price ↑
        Price ↓
        Power
        Top Speed
      </select>
    
    
      <button>All
      <button>Hypercar
      <button>Sports
      <button>Muscle
      <button>EV
      <button>SUV/Truck
    
    
  

  
  
    
      
        Live Auctions
        Bid · Buyout · Win
      
      
        <button>↺ Refresh
        <button>+ List Car
      
    
    
      <button>All
      <button>⏰ Ending Soon
      <button>🏆 Hypercar Night
      <button>🎌 JDM Night
      <button>💪 Muscle Madness
    
    
  

  
  
    Challenges
    Daily · Weekly · Achievements
    
      
        📅 Daily Challenges
        
        📆 Weekly Missions
        
      
      
        🏅 Achievements
        
      
    
  

  
  
    Leaderboard
    Top drivers · Live rankings
    
      <button>🏆 Most Wins
      <button>💰 Richest
      <button>🔥 Streaks
      <button>🚗 Garage
    
    
      
      
      
      
    
  

  
  
    Profile
    Stats · History · Daily Bonus
    
      
        R
        
          
            Driver
            
          
          
            Level 1 · 0 Rep · 0🔥 Streak
          
          
          
            0 / 1000 XP
          
        
      
      
        0Wins
        0Losses
        $0Cash
        0Best Streak
      
      
        
          Performance
          
        
        
          Daily Bonus
          
        
      
      
        Race History
        
      
    
  

  
  
    
      
        Admin Panel
        System Controls · 
      
    
    
      
        <button>📊 Overview
        <button>👥 Users
        <button>🤖 NPCs
        <button>📈 Market
        <button>🔨 Auctions
        <button>💰 Economy
        <button>🏁 Races
        <button>📋 Logs
        <button>📢 Broadcast
        <button>⚙️ Settings
      
      
    
  





  
    🎁 Daily Bonus!
    <button>×
  
  $0
  Day 1
  
  <button>Claim Bonus →




  
    Race
    READY
  
  
    YOU
    
      
      YOU
      
        
        🚗
      
      
    
    OPPONENT
    
      
      OPP
      
        
        🏎️
      
      
    
  
  3
  
    
      YOU
      —
      🚗
    
    VS
    
      OPP
      —
      🏎️
    
  
  




  <button>×


  
    <button>×
    Place Bid
    
    
      
        CURRENT BID
        $0
      
      
        YOUR CASH
        $0
      
    
    
      <label>Bid Amount (min $0)
      <input>
    
    
      Buyout: N/A
    
    Recent Bids
    
    
      <button>Cancel
      <button>⚡ Place Bid
    
  


  
    <button>×
    List for Auction
    
    <label>Starting Price ($)<input>
    <label>Buyout Price (optional)<input>
    <label>Duration
      <select>
        2 Hours4 Hours
        6 Hours12 Hours24 Hours
      
    
    <label>Event Type
      <select>
        Standard
        🏆 Hypercar Night
        🎌 JDM Night
        💪 Muscle Madness
      
    
    
      <button>Cancel
      <button>🔨 List Now
    
  


  
    <button>×
    User Detail
    
  







<script>
<script></script>
<script>
<script>
firebase.initializeApp({apiKey:"AIzaSyDAPdNjRs8TkDymnNyYIdc3YpgtVbthvMc",authDomain:"redline-b4422.firebaseapp.com",projectId:"redline-b4422",storageBucket:"redline-b4422.firebasestorage.app",messagingSenderId:"725052073743",appId:"1:725052073743:web:c8ebd165a59f2fd9bbc07a"});
const auth=firebase.auth(),db=firebase.firestore();
auth.setPersistence(firebase.auth.Auth.Persistence.LOCAL);

// ══ STATE ══
let CU=null,P=null,PCars=[],AllCars=[],MktPrices={};
let selCar=null,racing=false,mktFilter='all',auctFilter='all';
let bidAuction=null,sellPCar=null,upgCat='engine',curAdmSec='overview';
let auctUnsubs=[],npcAccounts=[];

// ══ CONSTANTS ══
const DAILY=[5000,8000,12000,18000,25000,35000,75000];
const NPC_ADJ=['Ghost','Turbo','Nitro','Drag','Drift','Speed','Apex','Boost','Rev','Smoke','Burn','Flat'];
const NPC_NOUN=['Racer','King','Hunter','Wolf','Fox','Hawk','Storm','Legend','Devil','Phantom'];

const CARS=[
{n:'McLaren 720S',b:'McLaren',cl:'Hypercar',r:'Legendary',e:'🦋',p:280000,ts:212,ac:96,ha:94,br:92,pw:720,wt:2829,d:'Aeroblade aero. 0-60 in 2.8s.'},
{n:'McLaren P1',b:'McLaren',cl:'Hypercar',r:'Mythic',e:'🟠',p:1400000,ts:218,ac:97,ha:95,br:94,pw:903,wt:3075,d:'Hybrid hypercar. F1 tech on the road.'},
{n:'McLaren Senna',b:'McLaren',cl:'Hypercar',r:'Mythic',e:'🔶',p:1000000,ts:208,ac:98,ha:97,br:96,pw:789,wt:2641,d:'Track weapon. Downforce king.'},
{n:'Bugatti Chiron',b:'Bugatti',cl:'Hypercar',r:'Mythic',e:'🔵',p:3000000,ts:304,ac:96,ha:88,br:90,pw:1500,wt:4398,d:'Quad-turbo W16. 1500hp.'},
{n:'Bugatti Veyron',b:'Bugatti',cl:'Hypercar',r:'Legendary',e:'💙',p:1500000,ts:268,ac:95,ha:85,br:88,pw:1001,wt:4162,d:'The original 1000hp street car.'},
{n:'Koenigsegg Jesko',b:'Koenigsegg',cl:'Hypercar',r:'Mythic',e:'🟡',p:3000000,ts:300,ac:99,ha:96,br:95,pw:1600,wt:3131,d:'300mph capable. 1600hp.'},
{n:'Koenigsegg Agera RS',b:'Koenigsegg',cl:'Hypercar',r:'Mythic',e:'⚪',p:2500000,ts:278,ac:98,ha:95,br:94,pw:1341,wt:3075,d:'World record holder.'},
{n:'Pagani Huayra',b:'Pagani',cl:'Hypercar',r:'Mythic',e:'🎨',p:2700000,ts:238,ac:94,ha:90,br:90,pw:730,wt:2822,d:'Twin-turbo V12 art piece.'},
{n:'Rimac Nevera',b:'Rimac',cl:'Hypercar',r:'Mythic',e:'⚡',p:2400000,ts:258,ac:100,ha:93,br:95,pw:1914,wt:4740,d:'Fastest production EV. 0-60 in 1.85s.'},
{n:'Ferrari SF90 Stradale',b:'Ferrari',cl:'Hypercar',r:'Legendary',e:'🔴',p:620000,ts:211,ac:99,ha:95,br:93,pw:986,wt:3461,d:"Ferrari's most powerful road car."},
{n:'Ferrari LaFerrari',b:'Ferrari',cl:'Hypercar',r:'Mythic',e:'🐎',p:2000000,ts:217,ac:98,ha:96,br:94,pw:950,wt:2767,d:'Hybrid F-car. Ultra-rare.'},
{n:'Lamborghini Aventador SVJ',b:'Lamborghini',cl:'Hypercar',r:'Legendary',e:'🐂',p:500000,ts:217,ac:96,ha:93,br:91,pw:770,wt:3363,d:'V12 NA screamer. 770hp.'},
{n:'Lamborghini Huracan STO',b:'Lamborghini',cl:'Hypercar',r:'Epic',e:'🏆',p:330000,ts:193,ac:95,ha:96,br:93,pw:631,wt:2932,d:'Track-bred V10.'},
{n:'Porsche 918 Spyder',b:'Porsche',cl:'Hypercar',r:'Mythic',e:'🕷️',p:850000,ts:214,ac:97,ha:95,br:94,pw:887,wt:3715,d:'Hybrid V8. Nurburgring record.'},
{n:'Porsche 911 GT3 RS',b:'Porsche',cl:'Sports',r:'Epic',e:'💛',p:250000,ts:184,ac:96,ha:99,br:97,pw:518,wt:3153,d:'NA flat-six track weapon.'},
{n:'Porsche 911 Turbo S',b:'Porsche',cl:'Sports',r:'Epic',e:'🏆',p:220000,ts:205,ac:98,ha:94,br:93,pw:640,wt:3516,d:'AWD monster. 2.6s 0-60.'},
{n:'Nissan GT-R Nismo',b:'Nissan',cl:'Sports',r:'Epic',e:'🇯🇵',p:200000,ts:196,ac:95,ha:92,br:91,pw:600,wt:3803,d:'Godzilla. AWD legend.'},
{n:'Toyota Supra MK5',b:'Toyota',cl:'Sports',r:'Rare',e:'🟠',p:65000,ts:155,ac:88,ha:85,br:84,pw:382,wt:3370,d:'B58 inline-6. Born to be modded.'},
{n:'Toyota Supra MK4',b:'Toyota',cl:'Sports',r:'Epic',e:'🏁',p:120000,ts:177,ac:90,ha:88,br:86,pw:320,wt:3197,d:'2JZ legend.'},
{n:'Nissan Silvia S15',b:'Nissan',cl:'Sports',r:'Rare',e:'⬜',p:45000,ts:155,ac:82,ha:86,br:80,pw:247,wt:2767,d:'JDM drift icon.'},
{n:'Mazda RX-7 FD',b:'Mazda',cl:'Sports',r:'Epic',e:'🔴',p:95000,ts:156,ac:87,ha:88,br:85,pw:276,wt:2723,d:'Rotary soul.'},
{n:'Honda NSX Type R',b:'Honda',cl:'Sports',r:'Legendary',e:'⬜',p:450000,ts:174,ac:90,ha:95,br:93,pw:324,wt:2712,d:'Pure analog perfection.'},
{n:'Honda Civic Type R',b:'Honda',cl:'Sports',r:'Common',e:'🔴',p:45000,ts:169,ac:85,ha:88,br:85,pw:315,wt:2998,d:'Hot hatch king.'},
{n:'Subaru WRX STI',b:'Subaru',cl:'Sports',r:'Rare',e:'🔵',p:50000,ts:155,ac:82,ha:84,br:82,pw:310,wt:3388,d:'Rally-bred AWD.'},
{n:'Mitsubishi Evo X',b:'Mitsubishi',cl:'Sports',r:'Rare',e:'⬜',p:48000,ts:155,ac:83,ha:85,br:82,pw:291,wt:3263,d:'The last Evo.'},
{n:'Mazda MX-5',b:'Mazda',cl:'Sports',r:'Common',e:'🎌',p:30000,ts:136,ac:74,ha:82,br:78,pw:181,wt:2381,d:'Lightweight roadster.'},
{n:'Nissan 370Z',b:'Nissan',cl:'Sports',r:'Common',e:'🔵',p:35000,ts:155,ac:80,ha:82,br:80,pw:332,wt:3232,d:'VQ37 NA fun.'},
{n:'Dodge Hellcat Redeye',b:'Dodge',cl:'Muscle',r:'Epic',e:'👁️',p:95000,ts:203,ac:92,ha:74,br:76,pw:797,wt:4473,d:'797hp supercharged Hemi.'},
{n:'Dodge Viper ACR',b:'Dodge',cl:'Muscle',r:'Legendary',e:'🐍',p:135000,ts:177,ac:92,ha:98,br:97,pw:645,wt:3374,d:'V10 analog monster.'},
{n:'Ford Mustang GT500',b:'Ford',cl:'Muscle',r:'Epic',e:'🐍',p:80000,ts:180,ac:90,ha:84,br:83,pw:760,wt:4225,d:'Most powerful Ford ever made.'},
{n:'Chevrolet Corvette Z06',b:'Chevrolet',cl:'Muscle',r:'Epic',e:'🏎️',p:120000,ts:196,ac:93,ha:95,br:93,pw:670,wt:3366,d:'LT6 flat-plane V8.'},
{n:'Chevrolet Corvette C8',b:'Chevrolet',cl:'Muscle',r:'Rare',e:'🏁',p:75000,ts:194,ac:90,ha:90,br:88,pw:495,wt:3366,d:'Mid-engine revolution.'},
{n:'Tesla Model S Plaid',b:'Tesla',cl:'EV',r:'Epic',e:'⚡',p:120000,ts:200,ac:100,ha:80,br:85,pw:1020,wt:4766,d:'1020hp tri-motor. 1.99s 0-60.'},
{n:'Tesla Roadster',b:'Tesla',cl:'EV',r:'Legendary',e:'🚀',p:250000,ts:250,ac:100,ha:85,br:88,pw:1000,wt:2756,d:'Sub-1s 0-60 claimed.'},
{n:'Porsche Taycan Turbo S',b:'Porsche',cl:'EV',r:'Epic',e:'🟡',p:190000,ts:161,ac:97,ha:89,br:91,pw:750,wt:5060,d:'Most athletic EV chassis.'},
{n:'Lucid Air Sapphire',b:'Lucid',cl:'EV',r:'Legendary',e:'💎',p:250000,ts:205,ac:99,ha:83,br:87,pw:1234,wt:5182,d:'1234hp. Range meets speed.'},
{n:'Lamborghini Urus',b:'Lamborghini',cl:'SUV/Truck',r:'Legendary',e:'🐂',p:260000,ts:190,ac:90,ha:88,br:86,pw:657,wt:4850,d:'Fastest production SUV.'},
{n:'Jeep Trackhawk',b:'Jeep',cl:'SUV/Truck',r:'Rare',e:'🦅',p:85000,ts:180,ac:88,ha:72,br:74,pw:707,wt:5363,d:'Hellcat-powered Jeep.'},
{n:'Ford Raptor R',b:'Ford',cl:'SUV/Truck',r:'Rare',e:'🦅',p:100000,ts:115,ac:82,ha:66,br:68,pw:700,wt:5950,d:'Off-road king.'},
{n:'Ram TRX',b:'Ram',cl:'SUV/Truck',r:'Rare',e:'🛻',p:95000,ts:118,ac:80,ha:64,br:68,pw:702,wt:6350,d:'Hellcat in a truck.'}
];

const UPGRADES=[
{n:'Air Intake L1',cat:'engine',key:'intake',lvl:1,cost:2000,pb:15,hb:0,sb:5},
{n:'Air Intake L2',cat:'engine',key:'intake',lvl:2,cost:4500,pb:30,hb:0,sb:8},
{n:'Turbo Kit L1',cat:'engine',key:'turbo',lvl:1,cost:8000,pb:60,hb:0,sb:15},
{n:'Turbo Kit L2',cat:'engine',key:'turbo',lvl:2,cost:18000,pb:120,hb:0,sb:25},
{n:'Turbo Kit L3',cat:'engine',key:'turbo',lvl:3,cost:35000,pb:200,hb:0,sb:40},
{n:'Supercharger L1',cat:'engine',key:'sc',lvl:1,cost:12000,pb:80,hb:0,sb:18},
{n:'Supercharger L2',cat:'engine',key:'sc',lvl:2,cost:25000,pb:150,hb:0,sb:30},
{n:'Engine Swap',cat:'engine',key:'eswap',lvl:1,cost:30000,pb:100,hb:0,sb:20},
{n:'Street Tires',cat:'performance',key:'tires',lvl:1,cost:1500,pb:0,hb:8,sb:3},
{n:'Track Tires',cat:'performance',key:'tires',lvl:2,cost:5000,pb:0,hb:18,sb:6},
{n:'Race Slicks',cat:'performance',key:'tires',lvl:3,cost:12000,pb:0,hb:30,sb:10},
{n:'Big Brake Kit',cat:'performance',key:'brakes',lvl:1,cost:3000,pb:0,hb:10,sb:0},
{n:'Coilover Kit',cat:'performance',key:'susp',lvl:1,cost:5000,pb:0,hb:15,sb:5},
{n:'Race Suspension',cat:'performance',key:'susp',lvl:2,cost:12000,pb:0,hb:28,sb:8},
{n:'ECU Tune L1',cat:'performance',key:'ecu',lvl:1,cost:3000,pb:25,hb:5,sb:8},
{n:'ECU Tune L2',cat:'performance',key:'ecu',lvl:2,cost:7000,pb:50,hb:8,sb:15},
{n:'ECU Tune L3',cat:'performance',key:'ecu',lvl:3,cost:15000,pb:80,hb:12,sb:22}
];

const RACES=[
{id:'drag',n:'Drag Strip',d:'Raw HP from 0 to ¼ mile. Launch control and torque decide it.',e:'🏁',diff:'easy',rw:10000,xp:150,opp:520,oe:'🚗',on:'Street Racer',f:s=>s.pw*0.5+s.ac*8},
{id:'street',n:'Street Sprint',d:'Short burst through traffic. Pure acceleration wins.',e:'🏙️',diff:'easy',rw:10000,xp:150,opp:540,oe:'🚕',on:'City Drifter',f:s=>s.ac*10+s.pw*0.3},
{id:'circuit',n:'Road Circuit',d:'Mixed straights and technical corners. Balance required.',e:'🔄',diff:'medium',rw:25000,xp:300,opp:1100,oe:'🏎️',on:'Circuit Pro',f:s=>s.ha*8+s.pw*0.4+s.ts*2},
{id:'highway',n:'Highway Pull',d:'Top speed endurance. No corners. Power is everything.',e:'🛣️',diff:'medium',rw:25000,xp:300,opp:1050,oe:'🚗',on:'Highway King',f:s=>s.pw*0.7+s.ts*4},
{id:'ev',n:'EV Battle',d:'Electric torque vs combustion. Tesla/Rimac/Lucid get +500.',e:'⚡',diff:'medium',rw:25000,xp:300,opp:900,oe:'⚡',on:'Volt Striker',f:(s,c)=>s.pw*0.3+s.ac*8+(['Rimac Nevera','Tesla Model S Plaid','Tesla Roadster','Lucid Air Sapphire'].includes(c?.n)?500:0)},
{id:'offroad',n:'Off-Road Rally',d:'Dirt, rocks, jumps. SUVs get a massive +600 bonus.',e:'🌲',diff:'hard',rw:75000,xp:600,opp:1400,oe:'🚙',on:'Dirt Devil',f:(s,c)=>s.pw*0.4+s.ha*5+(c?.cl==='SUV/Truck'?600:0)},
{id:'drift',n:'Drift Battle',d:'Angle, smoke, style. Handling is everything here.',e:'💨',diff:'hard',rw:75000,xp:600,opp:1500,oe:'🚗',on:'Smoke King',f:s=>s.ha*15+s.pw*0.15},
{id:'midnight',n:'Midnight Run',d:'Full endurance at speed. Every single stat counts.',e:'🌙',diff:'elite',rw:200000,xp:1500,opp:2500,oe:'🏎️',on:'Ghost Racer',f:s=>(s.pw+s.ts*3+s.ha*10+s.ac*6)*0.5}
];

const TIPS={drag:'Stack turbo and supercharger upgrades.',circuit:'Balance handling + power.',street:'Max acceleration upgrades.',highway:'Raw power and top speed builds.',offroad:'SUV/Truck class gets +600 bonus!',drift:'Stack every handling upgrade.',midnight:'Balanced build wins here.',ev:'Tesla/Rimac/Lucid get a +500 bonus!'};

const ACHS=[
{id:'first_race',n:'First Race',d:'Complete your first race',ic:'🏁',ch:p=>p.wins+p.losses>=1,rw:1000},
{id:'win5',n:'5 Wins',d:'Win 5 races',ic:'🏆',ch:p=>p.wins>=5,rw:5000},
{id:'win25',n:'25 Wins',d:'Win 25 races',ic:'🥇',ch:p=>p.wins>=25,rw:25000},
{id:'win100',n:'Century Club',d:'Win 100 races',ic:'💯',ch:p=>p.wins>=100,rw:100000},
{id:'streak5',n:'On Fire',d:'Win 5 races in a row',ic:'🔥',ch:p=>p.best_streak>=5,rw:10000},
{id:'streak10',n:'Unstoppable',d:'Win 10 races in a row',ic:'⚡',ch:p=>p.best_streak>=10,rw:50000},
{id:'rich',n:'Millionaire',d:'Have $1,000,000 cash',ic:'💰',ch:p=>p.cash>=1000000,rw:10000},
{id:'cars3',n:'Collector',d:'Own 3 cars',ic:'🚗',ch:(p,n)=>n>=3,rw:5000},
{id:'cars10',n:'Fleet Owner',d:'Own 10 cars',ic:'🏎️',ch:(p,n)=>n>=10,rw:50000},
{id:'daily7',n:'Week Warrior',d:'7-day login streak',ic:'📅',ch:p=>p.daily_streak>=7,rw:25000},
{id:'lv10',n:'Veteran',d:'Reach Level 10',ic:'⭐',ch:p=>p.level>=10,rw:20000},
{id:'rep500',n:'Street Legend',d:'Earn 500 reputation',ic:'👑',ch:p=>p.rep>=500,rw:50000}
];

// ══ HELPERS ══
const fc=n=>{if(!n&&n!==0)return'0';n=Math.round(n);if(n>=1000000)return(n/1000000).toFixed(1)+'M';if(n>=1000)return(n/1000).toFixed(1)+'k';return n.toLocaleString();};
const fcf=n=>Math.round(n||0).toLocaleString();
const rcls=r=>({Common:'badge-common',Rare:'badge-rare',Epic:'badge-epic',Legendary:'badge-legendary',Mythic:'badge-mythic'}[r]||'badge-common');
const rarCls=r=>({Common:'rar-common',Rare:'rar-rare',Epic:'rar-epic',Legendary:'rar-legendary',Mythic:'rar-mythic'}[r]||'rar-common');
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const timeAgo=d=>{if(!d)return'?';const s=Math.floor((Date.now()-d)/1000);if(s<60)return s+'s ago';if(s<3600)return Math.floor(s/60)+'m ago';if(s<86400)return Math.floor(s/3600)+'h ago';return Math.floor(s/86400)+'d ago';};
const fmtCD=e=>{const s=Math.max(0,Math.floor((e-Date.now())/1000));if(!s)return'ENDED';const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),sec=s%60;return h?h+'h '+m+'m':m?m+'m '+String(sec).padStart(2,'0')+'s':sec+'s';};

function toast(msg,cls='t-info'){
  const t=document.createElement('div');t.className='toast '+cls;t.textContent=msg;
  document.getElementById('toast-wrap').appendChild(t);
  setTimeout(()=>{t.style.opacity='0';t.style.transform='translateX(110%)';setTimeout(()=>t.remove(),400);},3400);
}
function xpPop(msg){
  const el=document.createElement('div');el.className='xp-pop';el.textContent=msg;
  document.body.appendChild(el);setTimeout(()=>el.remove(),1600);
}
function openModal(id){document.getElementById(id).style.display='flex';}
function closeModal(id){document.getElementById(id).style.display='none';}
function feed(msg){
  const f=document.getElementById('npc-feed');if(!f)return;
  const item=document.createElement('div');item.className='feed-item';item.textContent=msg;
  f.appendChild(item);
  while(f.children.length>4)f.removeChild(f.firstChild);
  setTimeout(()=>{item.classList.add('fade');setTimeout(()=>item.remove(),300);},9000);
}
function roleBadge(role){
  const L={owner:'👑 Owner',admin:'🛡️ Admin',moderator:'⚔️ Mod',player:'🏎️ Player',npc:'🤖 NPC'};
  return `<span class="role-badge role-${role||'player'}">${L[role]||'Player'}</span>`;
}
function statsHTML(pw,ts,ac,ha,br,wt){
  return [
    ['POWER',Math.min(100,pw/20),'var(--red2)',pw+'hp'],
    ['TOP SPEED',Math.min(100,ts/2.6),'var(--amber2)',ts+'mph'],
    ['ACCEL',ac,'var(--steel2)',ac+'/100'],
    ['HANDLING',ha,'var(--green2)',ha+'/100'],
    ['BRAKING',br,'var(--purple2)',br+'/100'],
    ['WEIGHT',Math.min(100,100-wt/80),'var(--blue2)',wt.toLocaleString()+'lb']
  ].map(([l,w,c,v])=>`<div class="stat-row"><div class="stat-lbl">${l}</div><div class="stat-bg"><div class="stat-fill" style="width:${w}%;background:${c}"></div></div><div class="stat-val">${v}</div></div>`).join('');
}

// ══ AUTH ══
function authTab(t,el){
  document.querySelectorAll('.auth-tab').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('auth-login').style.display=t==='login'?'':'none';
  document.getElementById('auth-signup').style.display=t==='signup'?'':'none';
  setAMsg('');
}
function setAMsg(msg,type='err'){
  const el=document.getElementById('auth-msg');
  el.textContent=msg;el.style.display=msg?'block':'none';
  el.className='auth-msg '+(type==='ok'?'ok':type===''?'info':'err');
}
async function doLogin(){
  const user=document.getElementById('l-user').value.trim();
  const pass=document.getElementById('l-pass').value;
  if(!user||!pass){setAMsg('Username and password required');return;}
  setAMsg('Starting engine...','');
  try{
    const snap=await db.collection('profiles').where('username','==',user).limit(1).get();
    if(snap.empty){setAMsg('No account with that username');return;}
    const prof=snap.docs[0].data();
    if(prof.is_banned){setAMsg('Account suspended: '+(prof.ban_reason||'Contact support'));return;}
    if(prof.is_npc){setAMsg('That is an NPC account');return;}
    await auth.signInWithEmailAndPassword(prof.email,pass);
  }catch(e){setAMsg(e.message);}
}
async function doSignup(){
  const username=document.getElementById('s-user').value.trim();
  const email=document.getElementById('s-email').value.trim();
  const pass=document.getElementById('s-pass').value;
  if(!username||!email||!pass){setAMsg('All fields required');return;}
  if(pass.length<6){setAMsg('Password must be 6+ characters');return;}
  if(!/^[a-zA-Z0-9_]{3,20}$/.test(username)){setAMsg('Username: 3-20 chars, letters/numbers/_ only');return;}
  setAMsg('Building your profile...','');
  try{
    const taken=await db.collection('profiles').where('username','==',username).limit(1).get();
    if(!taken.empty){setAMsg('Username already taken');return;}
    const cred=await auth.createUserWithEmailAndPassword(email,pass);
    const uid=cred.user.uid;
    await db.collection('profiles').doc(uid).set({uid,username,email,cash:50000,level:1,xp:0,wins:0,losses:0,streak:0,best_streak:0,rep:0,role:'player',is_banned:false,ban_reason:null,is_npc:false,daily_streak:0,last_daily:null,achievements:[],created_at:firebase.firestore.FieldValue.serverTimestamp()});
    await giveStarterCar(uid);
    setAMsg('Welcome to REDLINE! 🏎️','ok');
  }catch(e){setAMsg(e.message);}
}
async function doLogout(){
  try{await logAct('logout',{});}catch{}
  await auth.signOut();
}

// ══ AUTH STATE ══
auth.onAuthStateChanged(async user=>{
  if(user){
    CU=user;
    document.getElementById('auth-screen').style.display='none';
    document.getElementById('game').style.display='flex';
    await boot();
  }else{
    CU=null;P=null;PCars=[];
    document.getElementById('auth-screen').style.display='flex';
    document.getElementById('game').style.display='none';
    auctUnsubs.forEach(u=>u());auctUnsubs=[];
    ['_mktTick','_auctTick','_cdTick','_npcTick'].forEach(k=>clearInterval(window[k]));
  }
});

// ══ BOOT ══
async function boot(){
  AllCars=CARS;
  await Promise.all([loadProfile(),seedMarket()]);
  await Promise.all([loadPCars(),loadMktPrices()]);
  renderHUD();renderRaces();renderGarage();
  setupAuctListener();startMktTicker();checkDaily();
  startNPC();checkAchs();
  logAct('login',{}).catch(()=>{});
}
async function loadProfile(){
  const doc=await db.collection('profiles').doc(CU.uid).get();
  if(doc.exists){P={id:CU.uid,...doc.data()};}
  else{
    const username=CU.email.split('@')[0];
    P={id:CU.uid,username,email:CU.email,cash:50000,level:1,xp:0,wins:0,losses:0,streak:0,best_streak:0,rep:0,role:'player',is_banned:false,is_npc:false,daily_streak:0,last_daily:null,achievements:[]};
    await db.collection('profiles').doc(CU.uid).set(P);
  }
}
async function loadPCars(){
  const snap=await db.collection('player_cars').where('player_id','==',CU.uid).get();
  PCars=snap.docs.map(d=>({id:d.id,...d.data()}));
  PCars.forEach(pc=>{pc.car=CARS.find(c=>c.n===pc.car_name)||null;});
}
async function loadMktPrices(){
  const snap=await db.collection('market_prices').get();
  MktPrices={};
  snap.docs.forEach(d=>{const mp=d.data();MktPrices[mp.car_name]={id:d.id,...mp};});
  CARS.forEach(c=>{if(!MktPrices[c.n])MktPrices[c.n]={car_name:c.n,current_price:c.p,base_price:c.p,demand_score:50};});
}
async function seedMarket(){
  const snap=await db.collection('market_prices').limit(1).get();
  if(!snap.empty)return;
  const batch=db.batch();
  CARS.forEach(c=>batch.set(db.collection('market_prices').doc(),{car_name:c.n,current_price:c.p,base_price:c.p,demand_score:50,updated_at:firebase.firestore.FieldValue.serverTimestamp()}));
  await batch.commit();
}
async function giveStarterCar(uid){
  const car=CARS.find(c=>c.n==='Toyota Supra MK5');if(!car)return;
  await db.collection('player_cars').add({player_id:uid,car_name:car.n,car_class:car.cl,car_emoji:car.e,purchase_price:0,is_active:true,is_fav:false,pb:0,hb:0,sb:0,upgrades:{},acquired_at:firebase.firestore.FieldValue.serverTimestamp()});
}
async function logAct(action,details){
  if(!CU||!P)return;
  await db.collection('activity_logs').add({user_id:CU.uid,username:P.username,action,details:details||{},created_at:firebase.firestore.FieldValue.serverTimestamp()});
}

// ══ DAILY ══
function checkDaily(){
  if(!P)return;
  const last=P.last_daily?.toDate?.()??null;
  if(last&&last.toDateString()===new Date().toDateString())return;
  showDailyBanner();
}
function showDailyBanner(){
  if(!P)return;
  const streak=Math.min(P.daily_streak||0,DAILY.length-1);
  const amt=DAILY[streak];
  document.getElementById('daily-amt').textContent='$'+fcf(amt);
  document.getElementById('daily-streak-txt').textContent=`Day ${streak+1} streak · Come back tomorrow!`;
  const days=['M','T','W','T','F','S','S'];
  document.getElementById('daily-days').innerHTML=days.map((d,i)=>`<div class="d-day ${i<streak?'done':i===streak?'today':''}">${i<streak?'✓':d}</div>`).join('');
  document.getElementById('daily-wrap').classList.add('show');
}
async function claimDaily(){
  if(!P||!CU)return;
  const last=P.last_daily?.toDate?.()??null;

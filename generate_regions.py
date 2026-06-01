# -*- coding: utf-8 -*-
"""국민설비 지역별 랜딩페이지 생성기.
템플릿 + 지역데이터 -> regions/<slug>.html 자동 생성.
지역 추가/수정 시 REGIONS 에 항목만 넣고 다시 실행하면 됨.
"""
import os

# ===== 설정 =====
CDN = "https://cdn.jsdelivr.net/gh/hihiood/gukmin-landing@main/images/"
PHONE = "010-7417-2111"
# 지역 카테고리 허브 도메인 (v1=신뢰형이 올라간 drain2111 을 허브로 사용)
BASE = "https://drain2111.isweb.co.kr"
HUB_URL = BASE + "/"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regions")

# ===== 지역 데이터 =====
# slug, name(짧은), full(구/시), cluster, intro(지역 맞춤 한 줄), dongs(실제 동)
REGIONS = [
 # 서울 강남권
 {"slug":"gangnam","name":"강남","full":"강남구","cluster":"서울 강남권",
  "intro":"역삼·삼성·대치·논현 등 사무실과 음식점이 밀집한 강남구는 주방 싱크대·상가 하수구 막힘이 잦은 지역입니다. 국민설비가 강남구 전역으로 24시간 즉시 출동합니다.",
  "dongs":["역삼동","삼성동","대치동","청담동","신사동","논현동","압구정동","도곡동","개포동","일원동","수서동","세곡동"]},
 {"slug":"seocho","name":"서초","full":"서초구","cluster":"서울 강남권",
  "intro":"반포·잠원 아파트 단지와 서초동 오피스가 많은 서초구는 노후 배관 누수와 변기 막힘 문의가 많습니다. 서초구 전동 빠르게 출동합니다.",
  "dongs":["서초동","반포동","잠원동","방배동","양재동","내곡동","우면동"]},
 {"slug":"songpa","name":"송파","full":"송파구","cluster":"서울 강남권",
  "intro":"잠실·문정·가락 등 대규모 아파트와 상가가 공존하는 송파구는 하수구 역류·정화조 민원이 잦습니다. 송파구 위례까지 24시간 대응합니다.",
  "dongs":["잠실동","문정동","가락동","송파동","석촌동","방이동","오금동","거여동","마천동","풍납동","장지동"]},
 # 서울 강북권
 {"slug":"mapo","name":"마포","full":"마포구","cluster":"서울 강북권",
  "intro":"합정·망원·연남 등 카페·음식점이 빼곡한 마포구는 기름때 싱크대 막힘이 특히 많습니다. 마포구 전역 고압세척으로 즉시 해결합니다.",
  "dongs":["공덕동","아현동","도화동","용강동","대흥동","염리동","신수동","서교동","합정동","망원동","연남동","상암동"]},
 {"slug":"yongsan","name":"용산","full":"용산구","cluster":"서울 강북권",
  "intro":"한남·이태원 주택가와 노후 건물이 섞인 용산구는 오래된 하수관 막힘·누수 진단 수요가 높습니다. 용산구 어디든 빠르게 출동합니다.",
  "dongs":["한남동","이태원동","청파동","원효로동","효창동","용문동","이촌동","한강로동","보광동","후암동"]},
 {"slug":"seongdong","name":"성동","full":"성동구","cluster":"서울 강북권",
  "intro":"성수동 상가·공장과 왕십리 주거가 함께 있는 성동구는 업소 배수구·하수구 막힘이 잦습니다. 성동구 전동 24시간 대응합니다.",
  "dongs":["성수동","왕십리","행당동","응봉동","금호동","옥수동","마장동","사근동","송정동","용답동"]},
 # 경기 남부
 {"slug":"bundang","name":"분당","full":"성남시 분당구","cluster":"경기 남부",
  "intro":"정자·서현·판교 등 IT기업과 고층 아파트가 많은 분당은 주방·욕실 배관 막힘과 누수탐지 문의가 많습니다. 분당 전역 30분 내 출동합니다.",
  "dongs":["정자동","서현동","수내동","이매동","야탑동","판교동","백현동","분당동","구미동","금곡동"]},
 {"slug":"suwon","name":"수원","full":"수원시","cluster":"경기 남부",
  "intro":"영통·광교 신도시와 구도심이 공존하는 수원은 하수구 막힘·정화조·누수까지 다양한 출동이 이어집니다. 수원시 전역 24시간 대응합니다.",
  "dongs":["영통동","매탄동","권선동","인계동","우만동","정자동","광교","호매실동","망포동","세류동"]},
 {"slug":"bucheon","name":"부천","full":"부천시","cluster":"경기 남부",
  "intro":"중동·상동 상권과 다세대 주택이 밀집한 부천은 변기·싱크대 막힘과 하수구 역류 문의가 많습니다. 부천시 전동 즉시 출동합니다.",
  "dongs":["중동","상동","원미동","심곡동","소사동","역곡동","송내동","오정동","약대동","춘의동"]},
 # 경기북부·인천
 {"slug":"goyang","name":"고양","full":"고양시","cluster":"경기북부·인천",
  "intro":"일산 신도시와 행신·화정 주거지가 넓게 퍼진 고양시는 아파트 하수구·누수 출동이 많습니다. 고양시 일산동·서구 전역 대응합니다.",
  "dongs":["일산동","정발산동","마두동","백석동","화정동","행신동","능곡동","주엽동","대화동","탄현동","식사동"]},
 {"slug":"uijeongbu","name":"의정부","full":"의정부시","cluster":"경기북부·인천",
  "intro":"의정부동·신곡·민락 등 주거 밀집지가 많은 의정부는 노후 배관 막힘과 변기 역류 문의가 잦습니다. 의정부시 전역 24시간 출동합니다.",
  "dongs":["의정부동","호원동","가능동","신곡동","장암동","민락동","송산동","금오동","녹양동"]},
 {"slug":"incheon","name":"인천","full":"인천시","cluster":"경기북부·인천",
  "intro":"부평·구월 구도심과 송도·청라 신도시가 함께 있는 인천은 하수구 막힘·정화조·누수탐지 수요가 폭넓습니다. 인천시 전역 즉시 출동합니다.",
  "dongs":["부평동","구월동","논현동","송도동","청라동","계산동","주안동","서창동","만수동","검단"]},
]

SERVICES = [
 ("work-sink.jpg","싱크대 막힘","음식물·기름때로 막힌 주방 배관을 분해 없이 고압세척으로 뚫습니다."),
 ("work-floor-drain.jpg","변기·화장실 막힘","변기·세면대·욕실 바닥 역류를 오물 없이 신속하게 처리합니다."),
 ("work-grate.jpg","하수구·배수구 막힘","마당·베란다·옥외 하수구 역류와 악취를 원인까지 찾아 해결합니다."),
 ("work-camera.jpg","누수탐지","청음·열화상 장비로 벽체·바닥·수도배관 누수 위치를 파괴 없이 찾아 보수합니다."),
 ("work-cctv.jpg","CCTV 관로탐지","배관 속을 카메라로 직접 확인해 막힘 위치와 원인을 정밀 진단합니다."),
 ("work-grease.jpg","정화조·맨홀","정화조 청소·맨홀 준설·오수 처리까지 위생적으로 작업합니다."),
]

TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%%NAME%% 하수구막힘·싱크대막힘·변기막힘·누수탐지 | 국민설비 %%NAME%% 24시 출동</title>
<meta name="description" content="%%FULL%% 하수구막힘·싱크대막힘·변기막힘·누수탐지 즉시 해결! 국민설비가 %%NAME%% 전역으로 24시간 연중무휴 출동합니다. 고압세척·CCTV 관로탐지·누수탐지 전문, 정찰견적. ☎ %%PHONE%%">
<meta name="keywords" content="%%NAME%% 하수구막힘, %%NAME%% 싱크대막힘, %%NAME%% 변기막힘, %%NAME%% 누수탐지, %%NAME%% 화장실막힘, %%NAME%% 하수구뚫음, %%NAME%% 변기뚫음, %%FULL%% 하수구막힘, %%FULL%% 누수, %%NAME%% 정화조청소, %%NAME%% 설비, 하수구막힘, 싱크대막힘, 변기막힘, 누수탐지, 국민설비">
<meta name="author" content="국민설비">
<meta name="robots" content="index, follow">
<meta name="naver-site-verification" content="여기에_네이버_웹마스터_인증코드_입력">
<meta name="google-site-verification" content="여기에_구글_서치콘솔_인증코드_입력">
<link rel="canonical" href="%%CANONICAL%%">
<meta property="og:type" content="website">
<meta property="og:url" content="%%CANONICAL%%">
<meta property="og:title" content="%%NAME%% 하수구막힘·싱크대막힘·변기막힘·누수탐지 24시 출동 | 국민설비">
<meta property="og:description" content="%%FULL%% 24시간 즉시출동! 하수구·싱크대·변기 막힘과 누수탐지 해결. 고압세척·CCTV·누수탐지 전문. ☎ %%PHONE%%">
<meta property="og:image" content="%%CDN%%hero2.jpg">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="국민설비">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%9A%B0%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Plumber","name":"국민설비 %%NAME%%","image":"%%CDN%%hero2.jpg","telephone":"+82-%%PHONE_INTL%%","priceRange":"₩₩",
"description":"%%FULL%% 하수구막힘·싱크대막힘·변기막힘·누수탐지 전문 출동 설비. 24시간 연중무휴.",
"areaServed":[%%AREA_SERVED%%],
"openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{"@type":"ListItem","position":1,"name":"국민설비","item":"%%HUB%%"},
{"@type":"ListItem","position":2,"name":"%%NAME%% 하수구막힘","item":"%%CANONICAL%%"}]}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"%%NAME%% 어디까지 출동하나요?","acceptedAnswer":{"@type":"Answer","text":"%%FULL%% 전 지역(%%DONGS_TEXT%% 등) 24시간 연중무휴 출동합니다. 평균 30분~1시간 내 도착합니다."}},
{"@type":"Question","name":"%%NAME%% 출동 비용은 어떻게 되나요?","acceptedAnswer":{"@type":"Answer","text":"막힘 정도에 따라 다르며, 출동 후 현장에서 정찰 견적을 먼저 안내드리고 동의하셔야만 작업합니다. 추가비용 임의 청구 없습니다."}},
{"@type":"Question","name":"%%NAME%%에서 누수탐지도 되나요?","acceptedAnswer":{"@type":"Answer","text":"네. %%NAME%% 전역에서 청음·열화상 장비로 벽체·바닥·수도배관 누수를 파괴 없이 찾아 보수합니다."}}]}
</script>
<style>
:root{--blue:#0b63d6;--blue-d:#073e8a;--blue-l:#e8f1fd;--ink:#0f1b2d;--gray:#5b6b80;--line:#e3e9f1;--bg:#f5f8fc}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth}
body{font-family:'Noto Sans KR',sans-serif;color:var(--ink);background:#fff;line-height:1.7;font-size:18px}
img{max-width:100%;display:block}a{text-decoration:none;color:inherit}
.wrap{max-width:1100px;margin:0 auto;padding:0 20px}
.han{font-family:'Black Han Sans',sans-serif;letter-spacing:-.5px}
.topbar{background:var(--blue-d);color:#fff;text-align:center;font-weight:700;font-size:16px;padding:10px}.topbar b{color:#ffd34d}
header{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--line);box-shadow:0 2px 12px rgba(0,0,0,.04)}
.head{display:flex;align-items:center;justify-content:space-between;padding:14px 0}
.logo{display:flex;align-items:center;gap:10px;font-size:25px}.logo .em{font-size:30px}.logo b{color:var(--blue)}
.head-call{display:flex;align-items:center;gap:14px}.head-call .num{font-family:'Black Han Sans';font-size:28px;color:var(--blue)}
.btn-call{background:var(--blue);color:#fff;font-weight:900;font-size:18px;padding:12px 22px;border-radius:50px;box-shadow:0 6px 18px rgba(11,99,214,.35)}
@media(max-width:760px){.head-call .num{display:none}}
.hero{position:relative;color:#fff;background:linear-gradient(rgba(7,40,90,.78),rgba(7,40,90,.88)),url('%%CDN%%hero2.jpg') center/cover;padding:64px 0 70px}
.hero .loc{display:inline-block;background:#ffd34d;color:#0a2a5e;font-weight:900;padding:7px 18px;border-radius:50px;font-size:17px;margin-bottom:16px}
.hero h1{font-size:50px;line-height:1.18;margin-bottom:16px}.hero h1 .hl{color:#ffd34d}
.hero p.sub{font-size:21px;font-weight:500;opacity:.96;margin-bottom:24px}
.badges{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px}
.badge{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.35);padding:9px 16px;border-radius:50px;font-weight:700;font-size:16px}
.hero-cta .big{display:inline-block;background:#ffd34d;color:#0a2a5e;font-family:'Black Han Sans';font-size:28px;padding:16px 34px;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.3)}
@media(max-width:760px){.hero h1{font-size:35px}.hero p.sub{font-size:18px}.hero-cta .big{font-size:24px;width:100%;text-align:center}}
section{padding:58px 0}
.eyebrow{color:var(--blue);font-weight:900;font-size:17px;letter-spacing:1px;text-align:center}
.title{font-size:38px;text-align:center;margin:8px 0 12px;line-height:1.25}
.lead{text-align:center;color:var(--gray);font-size:19px;max-width:780px;margin:0 auto 38px}
@media(max-width:760px){.title{font-size:28px}.lead{font-size:17px}}
.area{background:var(--blue-l)}
.dongs{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;max-width:900px;margin:0 auto}
.dong{background:#fff;border:1px solid #cfe0f7;color:var(--blue-d);font-weight:700;padding:10px 18px;border-radius:50px;font-size:17px}
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.svc{border:1px solid var(--line);border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 6px 22px rgba(15,27,45,.05)}
.svc img{height:190px;width:100%;object-fit:cover}.svc .b{padding:20px}.svc h3{font-size:24px;margin-bottom:6px}.svc p{color:var(--gray);font-size:16px}
@media(max-width:860px){.svc-grid{grid-template-columns:1fr 1fr}}@media(max-width:560px){.svc-grid{grid-template-columns:1fr}}
.why{background:var(--ink);color:#fff}.why .title{color:#fff}
.why-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.why-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:24px}
.why-card .ic{font-size:36px;margin-bottom:10px}.why-card h4{font-size:21px;margin-bottom:6px;color:#ffd34d}.why-card p{color:#c8d3e2;font-size:16px}
@media(max-width:760px){.why-grid{grid-template-columns:1fr}}
.faq-item{border:1px solid var(--line);border-radius:14px;margin-bottom:12px;overflow:hidden;background:#fff}
.faq-q{padding:18px 22px;font-weight:700;font-size:20px;cursor:pointer;display:flex;justify-content:space-between;gap:12px;align-items:center}
.faq-q .pl{color:var(--blue);font-size:26px;transition:.3s}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s;color:var(--gray);font-size:17px}.faq-a div{padding:0 22px 20px}
.faq-item.open .faq-a{max-height:320px}.faq-item.open .pl{transform:rotate(45deg)}
.cta-band{background:linear-gradient(120deg,var(--blue),var(--blue-d));color:#fff;text-align:center}
.cta-band h2{font-size:40px;margin-bottom:10px}.cta-band .num{font-family:'Black Han Sans';font-size:58px;color:#ffd34d;line-height:1.2}
.cta-band .btn-call{font-size:22px;padding:16px 36px;margin-top:14px;background:#ffd34d;color:#0a2a5e}
@media(max-width:760px){.cta-band h2{font-size:28px}.cta-band .num{font-size:42px}}
.backlink{text-align:center;padding:26px 0;background:var(--bg)}.backlink a{color:var(--blue);font-weight:700;font-size:17px}
footer{background:#08101c;color:#9fb0c4;padding:40px 0;font-size:15px}
footer b{color:#fff;font-size:20px}
.kw{color:#3d4f66;font-size:13px;line-height:1.9;margin-top:18px;border-top:1px solid #16263b;padding-top:16px}
.mobilebar{position:fixed;left:0;right:0;bottom:0;z-index:99;display:none;background:var(--blue);box-shadow:0 -4px 20px rgba(0,0,0,.3)}
.mobilebar a{display:flex;align-items:center;justify-content:center;gap:10px;color:#fff;font-family:'Black Han Sans';font-size:23px;padding:15px}
.ring{animation:ring 1s infinite;display:inline-block}@keyframes ring{0%,100%{transform:rotate(0)}25%{transform:rotate(-12deg)}75%{transform:rotate(12deg)}}
@media(max-width:760px){.mobilebar{display:block}body{padding-bottom:62px}}
</style>
</head>
<body>
<div class="topbar">📍 %%FULL%% 전지역 <b>24시간 연중무휴</b> 즉시출동 · 출동 후 정찰견적</div>
<header><div class="wrap head">
  <a class="logo" href="%%HUB%%"><span class="em">🚰</span><span class="han">국민<b>설비</b> %%NAME%%</span></a>
  <div class="head-call"><span class="num">%%PHONE%%</span><a class="btn-call" href="tel:%%PHONE%%">📞 지금 전화</a></div>
</div></header>

<section class="hero"><div class="wrap">
  <span class="loc">📍 %%NAME%% 24시 출동</span>
  <h1 class="han">%%NAME%% 하수구막힘<br><span class="hl">막히면 30분 출동</span></h1>
  <p class="sub">%%NAME%% 하수구막힘·싱크대막힘·변기막힘·누수탐지<br>전화 한 통이면 가까운 전문기사가 바로 갑니다.</p>
  <div class="badges"><span class="badge">⏱️ 평균 30분 내 도착</span><span class="badge">🛠️ 고압세척·CCTV·누수탐지</span><span class="badge">💰 정찰견적</span></div>
  <div class="hero-cta"><a class="big" href="tel:%%PHONE%%">📞 %%PHONE%%</a></div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">%%CLUSTER%%</p>
  <h2 class="title han">%%NAME%%에서 막히거나 새면, 국민설비</h2>
  <p class="lead">%%INTRO%%</p>
</div></section>

<section class="area"><div class="wrap">
  <p class="eyebrow">출동 가능 지역</p>
  <h2 class="title han">%%FULL%% 전동 출동합니다</h2>
  <p class="lead">아래 지역은 물론 %%FULL%% 인근 어디든 24시간 즉시 출동합니다.</p>
  <div class="dongs">%%DONG_BADGES%%</div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">SERVICE</p>
  <h2 class="title han">%%NAME%% 막힘·누수 전문 해결</h2>
  <p class="lead">가정집 싱크대부터 상가·건물 하수관, 보이지 않는 누수까지 %%NAME%%에서 전부 해결합니다.</p>
  <div class="svc-grid">%%SERVICES%%</div>
</div></section>

<section class="why"><div class="wrap">
  <p class="eyebrow" style="color:#ffd34d">WHY 국민설비</p>
  <h2 class="title han">%%NAME%% 주민들이 믿고 찾는 이유</h2>
  <div class="why-grid">
    <div class="why-card"><div class="ic">⚡</div><h4>%%NAME%% 30분 출동</h4><p>%%NAME%% 인근 대기 기사가 새벽·주말 없이 즉시 출동합니다.</p></div>
    <div class="why-card"><div class="ic">💳</div><h4>정찰 견적</h4><p>작업 전 금액을 먼저 안내, 동의 없이는 추가비용 없습니다.</p></div>
    <div class="why-card"><div class="ic">🔧</div><h4>전문 장비</h4><p>고압세척·CCTV·누수탐지·굴착까지 어떤 막힘도 해결.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <p class="eyebrow">FAQ</p>
  <h2 class="title han">%%NAME%% 자주 묻는 질문</h2>
  <div style="margin-top:26px">
    <div class="faq-item"><div class="faq-q">%%NAME%% 어디까지 출동하나요?<span class="pl">+</span></div><div class="faq-a"><div>%%FULL%% 전 지역(%%DONGS_TEXT%% 등)으로 24시간 연중무휴 출동하며, 평균 30분~1시간 내 도착합니다.</div></div></div>
    <div class="faq-item"><div class="faq-q">%%NAME%% 출동 비용은요?<span class="pl">+</span></div><div class="faq-a"><div>막힘 정도에 따라 다르며, 출동 후 정찰 견적을 먼저 안내드린 뒤 동의하셔야 작업합니다. 추가비용을 임의로 청구하지 않습니다.</div></div></div>
    <div class="faq-item"><div class="faq-q">%%NAME%%에서 누수탐지도 되나요?<span class="pl">+</span></div><div class="faq-a"><div>네. %%NAME%% 전역에서 청음·열화상 장비로 벽체·바닥·수도배관 누수를 파괴 없이 찾아 보수합니다.</div></div></div>
    <div class="faq-item"><div class="faq-q">밤늦게/새벽에도 %%NAME%% 출동되나요?<span class="pl">+</span></div><div class="faq-a"><div>네, 365일 24시간 운영합니다. %%NAME%% 어디든 언제든 %%PHONE%%로 전화 주세요.</div></div></div>
  </div>
</div></section>

<section class="cta-band"><div class="wrap">
  <h2 class="han">%%NAME%%에서 막혔다면, 지금 전화</h2>
  <div class="num">%%PHONE%%</div>
  <div><a class="btn-call" href="tel:%%PHONE%%">📞 %%NAME%% 24시 출동 요청</a></div>
</div></section>

<div class="backlink"><a href="%%HUB%%">← 국민설비 전체 서비스·다른 지역 보기</a></div>

<footer><div class="wrap">
  <b>🚰 국민설비 %%NAME%%</b><br>
  %%NAME%% 하수구막힘·싱크대막힘·변기막힘·누수탐지 24시 출동 · %%FULL%% 전지역<br>
  대표전화 <a href="tel:%%PHONE%%" style="color:#ffd34d;font-weight:700">%%PHONE%%</a> · 24시간 연중무휴
  <div class="kw">%%NAME%% 하수구막힘 · %%NAME%% 싱크대막힘 · %%NAME%% 변기막힘 · %%NAME%% 누수탐지 · %%NAME%% 화장실막힘 · %%NAME%% 하수구뚫음 · %%NAME%% 정화조청소 · %%FULL%% 하수구막힘 · %%DONGS_TEXT%% · 하수구막힘 · 싱크대막힘 · 변기막힘 · 누수탐지 · 국민설비</div>
</div></footer>

<div class="mobilebar"><a href="tel:%%PHONE%%"><span class="ring">📞</span> %%NAME%% 24시 %%PHONE%%</a></div>
<script>
document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')));
</script>
</body>
</html>
"""

def build_services():
    out=[]
    for img,h,p in SERVICES:
        out.append('<div class="svc"><img src="%s%s" alt="%%%%NAME%%%% %s 작업 - 국민설비"><div class="b"><h3>%s</h3><p>%s</p></div></div>'%(CDN,img,h,h,p))
    return "\n".join(out)

SERVICES_HTML = build_services()

def render(r):
    canonical = "%s/%s" % (BASE, r["slug"])
    dong_badges = "".join('<span class="dong">%s</span>'%d for d in r["dongs"])
    dongs_text = ", ".join(r["dongs"])
    area_served = ",".join('{"@type":"City","name":"%s"}'%d for d in ([r["full"]]+r["dongs"]))
    svc = SERVICES_HTML.replace("%%NAME%%", r["name"])
    html = TEMPLATE
    repl = {
        "%%NAME%%": r["name"], "%%FULL%%": r["full"], "%%CLUSTER%%": r["cluster"],
        "%%INTRO%%": r["intro"], "%%CDN%%": CDN, "%%PHONE%%": PHONE,
        "%%PHONE_INTL%%": "10-"+PHONE.split("-",1)[1], "%%CANONICAL%%": canonical,
        "%%HUB%%": HUB_URL, "%%DONG_BADGES%%": dong_badges, "%%DONGS_TEXT%%": dongs_text,
        "%%AREA_SERVED%%": area_served, "%%SERVICES%%": svc,
    }
    # SERVICES 안의 %%NAME%% 는 이미 치환됨; 나머지 토큰 치환
    for k,v in repl.items():
        html = html.replace(k,v)
    return html, canonical

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    enc="utf-8"
    made=[]
    for r in REGIONS:
        html, canonical = render(r)
        path=os.path.join(OUT_DIR, r["slug"]+".html")
        with open(path,"w",encoding=enc) as f:
            f.write(html)
        made.append((r["name"], r["slug"], canonical))
    print("생성 완료: %d개" % len(made))
    for name,slug,c in made:
        print("  %-6s -> regions/%s.html   (%s)" % (name, slug, c))

if __name__=="__main__":
    main()

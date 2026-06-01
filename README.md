# 국민설비 하수구막힘 랜딩페이지 프로젝트

하수구막힘·싱크대막힘·변기막힘·누수탐지 키워드 타겟 설비업체 랜딩페이지 + 지역별 SEO 랜딩 시스템.

---

## 📌 업체 정보
| 항목 | 내용 |
|---|---|
| 상호 | **국민설비** |
| 연락처 | **010-7417-2111** |
| 영업지역 | 수도권 (서울·경기·인천) |
| 운영 | 24시간 연중무휴 |
| 메인 키워드 | 하수구막힘 · 싱크대막힘 · 변기막힘 · 누수탐지 |

## 🌐 배포 도메인 (isweb · HTML만 업로드)
| 도메인 | 대표 디자인 | 지역 페이지 |
|---|---|---|
| https://drain2111.isweb.co.kr/ | **v1 신뢰형 (파랑)** | `regions/` 12개 |
| https://drain119.isweb.co.kr/ | **v3 프리미엄 (초록)** | `regions119/` 12개 |

> 두 도메인의 지역이 겹치지 않아 구글 중복콘텐츠 패널티 없이 노출 영역 2배.

---

## 📁 파일 구조
```
gukmin-landing/
├── v1-trust.html          # 대표 v1 (신뢰형, 파랑)   → drain2111 루트
├── v3-premium.html        # 대표 v3 (프리미엄, 초록) → drain119 루트
├── v2-urgent.html         # 긴급형 (참고용)
├── index.html             # 3개 시안 비교 페이지
├── generate_regions.py    # 지역페이지 자동 생성기
├── robots.txt / sitemap.xml
├── README.md              # (이 문서)
│
├── regions/               # drain2111용 지역 12개 (파랑)
│   gangnam seocho songpa mapo yongsan seongdong
│   bundang suwon bucheon goyang uijeongbu incheon
│
├── regions119/            # drain119용 지역 12개 (초록)
│   guro yeongdeungpo dongjak gwanak gangseo yangcheon
│   nowon gwangjin anyang ansan gimpo namyangju
│
└── images/                # 실제 작업 사진 18장
```

## 🗺️ 지역 페이지 (총 24개, 무중복)
**drain2111** (파랑): 강남·서초·송파·마포·용산·성동·분당·수원·부천·고양·의정부·인천
**drain119** (초록): 구로·영등포·동작·관악·강서·양천·노원·광진·안양·안산·김포·남양주

각 페이지: `지역명+키워드` 제목/H1/메타 + 실제 동(洞) 리스트 + 지역 맞춤 소개/FAQ + 구조화데이터(LocalBusiness·Breadcrumb·FAQ). 복붙 아님(도어웨이 패널티 회피).

---

## 🔍 SEO 적용 내역 (전 페이지 공통)
- `<title>` / `description` / `keywords` — 메인 4키워드 + 지역 조합
- Open Graph (카톡·페북 미리보기) + Twitter Card + `og:url`
- JSON-LD 구조화데이터: **Plumber**(업종·지역·24시·서비스) + **FAQPage** + (지역) **BreadcrumbList**
- `canonical`, `robots: index,follow`, `lang=ko`
- 이미지 `alt` 키워드 포함, 시맨틱 H1/H2, 모바일 반응형, 하단 고정 통화바
- 네이버/구글 인증 메타태그 자리 마련 (`여기에_..._입력`)

## 🖼️ 이미지 호스팅 (중요)
isweb엔 HTML만 올라가므로 이미지는 **GitHub 공개 repo + jsDelivr CDN** 절대주소로 참조.
- repo: **https://github.com/hihiood/gukmin-landing**
- CDN: `https://cdn.jsdelivr.net/gh/hihiood/gukmin-landing@main/images/...`
- → HTML 한 파일만 isweb에 올려도 이미지 정상 표시 + 빠른 로딩.

---

## ⚠️ 남은 작업 (To-do)
1. 🔴 **isweb 서브페이지 실제 URL 형식 확인** → `generate_regions.py`의 `SITES` base/slug 패턴 수정 후 재생성 (canonical을 실제 주소와 일치시켜야 구글 색인됨)
2. 대표페이지(v1·v3)에 **지역 링크 메뉴** 추가 (내부링크 = SEO 중요)
3. **구글 서치콘솔 / 네이버 서치어드바이저** 등록 → 인증코드를 메타태그 자리에 삽입 → sitemap 제출
4. (강력 추천) **네이버 스마트플레이스(플레이스) 등록** — 지역검색 노출의 핵심, 무료

## 🔧 지역 추가/수정 방법
1. `generate_regions.py`의 `REGIONS_2111` 또는 `REGIONS_119`에 항목 추가
   (`slug`, `name`, `full`, `cluster`, `intro`, `dongs`)
2. 실행: `python generate_regions.py`
3. `git add -A && git commit && git push` 로 CDN/백업 반영

## 💡 SEO 전략 메모
- "하수구막힘" 단독 = 전국 격전(광고·대형업체), 랜딩 1장으론 자연검색 상위 어려움.
- **"지역명+하수구막힘"** 롱테일 = 경쟁 낮고 전환율 높음 → 24개 지역 페이지로 공략.
- 네이버 지역검색은 **플레이스+블로그**가 핵심. 랜딩은 구글/광고 착지 + 신뢰 보강용.

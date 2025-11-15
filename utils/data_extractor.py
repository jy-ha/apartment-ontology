import trafilatura
import os

# 파일 저장을 위한 디렉토리 생성 (선택 사항)
output_dir = "extracted_data_dated"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------
# 1. 수집된 공식 자료 목록 (예시 데이터)
#    : 실제 온톨로지 구축을 위해 수집한 JSON 데이터를 여기에 사용합니다.
# ----------------------------------------------------
data_list = [
  {
    "date": "2025-10-02",
    "title": "[기자설명회] 서울시, 규제완화·리츠 출자지원으로 민간임대주택 공급 절벽 해소… '민간주도형'",
    "url": "https://www.discoverynews.kr/news/articleView.html?idxno=1074988"
  },
  {
    "date": "2025-10-01",
    "title": "민간 임대 활성화 나선 서울시…오피스텔 규제 완화·인허가 단축 [집슐랭]",
    "url": "https://www.sedaily.com/NewsView/2GZ0CSYLUS"
  },
  {
    "date": None,
    "title": "서울 성동구, 공동주택 건축심의 기준 대폭 완화",
    "url": "https://rknews.co.kr/detail.php?number=3822&thread=14&twrand=4134&reply_order=ban"
  },
  {
    "date": "2019-10-17",
    "title": "도시형 생활주택(단지형 다세대, 단지형 연립주택) 층수완화 심의기준_서울시 동작구",
    "url": "https://studio-oim.tistory.com/244"
  },
  {
    "date": "2025-10-01",
    "title": "서울 민간임대 활성화…건축규제 풀고 리츠 출자지원",
    "url": "http://www.seouleconews.com/news/articleView.html?idxno=86695"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 민간임대주택 활성화 대책 발표…'LTV 0%' 완화 추진",
    "url": "https://www.newsfc.co.kr/news/articleView.html?idxno=74177"
  },
  {
    "date": "2024-11-04",
    "title": "도시형 생활주택, 이르면 내달부터 면적 규제 완화 (전용 85㎡까지 확대)",
    "url": "https://www.chosun.com/economy/real_estate/2024/11/04/6H56LD3C5RGFRKWRYPB7E445QI/"
  },
  {
    "date": "2024-11-04",
    "title": "모든 도시형생활주택, '전용 85㎡'까지 지을 수 있게 된다",
    "url": "https://www.homeknock.co.kr/web-front/community/news/13145/"
  },
  {
    "date": "2025-10-01",
    "title": "빌라·오피스텔 공급 확대 추진…오세훈 '민간임대 규제와 전쟁'[부동산AtoZ]",
    "url": "https://cm.asiae.co.kr/article/2025100111331259433"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 공급절벽 '빌라·오피스텔' 규제 풀고 금융 지원 …전세사기 위험 리포트 제공",
    "url": "https://www.asiae.co.kr/article/2025100109354996366"
  },
  {
    "date": "2025-05-20",
    "title": "서울 소규모재개발·재건축 용적률 3년간 최고 300% 완화",
    "url": "https://www.housingherald.co.kr/news/articleView.html?idxno=50107"
  },
  {
    "date": "2024-08-08",
    "title": "소형 주택 구입 시 세제 혜택 확대…비아파트 시장 정상화 (단기임대 1가구 1주택 특례)",
    "url": "https://news.sbs.co.kr/news/endPage.do?news_id=N1007755827"
  },
  {
    "date": "2025-06-19",
    "title": "등록민간임대주택 렌트홈 (10년/6년 단기임대 세제혜택 요약 및 취득세/재산세 감면 내용)",
    "url": "https://www.renthome.go.kr/webportal/cont/rgstBenefitGdncView.open"
  },
  {
    "date": "2024-08-08",
    "title": "서울·수도권 42.7만호 공급: 국민 주거안정을 위한 주택공급 확대방안 | 경제정책자료 (KDI)",
    "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=255592"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 민간임대주택 공급 확대 위해 규제 완화·금융지원 추진",
    "url": "https://www.kmecnews.co.kr/news/articleView.html?idxno=43308"
  },
  {
    "date": "2025-10-01",
    "title": "서울 민간임대 공급절벽 없앤다…건축규제 풀고 리츠 출자지원 | 서울특별시 미디어재단 TBS",
    "url": "https://tbs.seoul.kr/news/newsView.do?typ_800=&idx_800=3534552&seq_800=20527444"
  },
  {
    "date": "2025-05-20",
    "title": "소규모 재건축, 용적률 300%까지…'비아파트' 공급 확대 나선 서울시",
    "url": "https://www.hankyung.com/realestate/article/202505202613i"
  },
  {
    "date": "2024-09-10",
    "title": "다가구·다세대 주택 건축규제 완화, 서울시 조례 개정 추진 내용",
    "url": "https://www.chosun.com/economy/real_estate/2024/09/10/ABCD1234EFG"
  },
  {
    "date": "2024-08-09",
    "title": "빌라 매매 활성화 위해 '신축 소형 주택' 취득세 감면 확대 방안 (정부 발표)",
    "url": "https://www.donga.com/news/article/all/20240809/120678900"
  },
  {
    "date": "2025-10-01",
    "title": "민간임대사업자 LTV 0% 규제 완화 정부 건의, 서울시의 입장 표명",
    "url": "https://www.yna.co.kr/view/AKR20251001000100000"
  },
  {
    "date": "2024-08-08",
    "title": "공공이 매입하는 비아파트 '신축 매입약정' 확대, 서울 지역 물량 집중",
    "url": "https://www.hankyung.com/realestate/article/2024080823456"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 비아파트 공급 가속화 위한 '일조사선 규정' 개선 계획",
    "url": "https://www.mk.co.kr/news/realestate/11223344"
  },
  {
    "date": "2025-10-01",
    "title": "비아파트 합산 배제 공시가액 기준 상향 정부 건의 내용 (서울시 발의)",
    "url": "https://cm.asiae.co.kr/article/2025100111331259433#cont"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 중소규모 오피스텔 심의 기준 완화로 건축 시간 단축 (30실→50실)",
    "url": "https://www.sedaily.com/NewsView/2GZ0CSYLUS#cont"
  },
  {
    "date": "2025-10-01",
    "title": "전세사기 위험 분석 리포트 제공 통한 비아파트 임차인 보호 조치 (서울시)",
    "url": "https://www.asiae.co.kr/article/2025100109354996366#protect"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 민간임대 리츠의 초기 출자금 부담 완화를 위한 금융 지원 방안",
    "url": "https://tbs.seoul.kr/news/newsView.do?typ_800=&idx_800=3534552&seq_800=20527444#fund"
  },
  {
    "date": "2024-08-08",
    "title": "서울 지역 소형 비아파트 구입 시 6년 단기임대등록 1가구 1주택 특례 적용",
    "url": "https://news.sbs.co.kr/news/endPage.do?news_id=N1007755827#tax"
  },
  {
    "date": "2024-08-08",
    "title": "공용주차장 건설 연계 소규모 정비사업 의무 주차면수 경감 정책",
    "url": "https://www.molit.go.kr/policy/capital/cap_c_03.jsp#parking"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, '등록 민간임대주택 활성화 방안' 발표 - 오피스텔 접도 조건 20m→12m 완화 (조례 개정 예정)",
    "url": "https://www.sedaily.com/NewsView/2GZ0CSYLUS"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 소규모 오피스텔 건축위원회 심의 대상 기준 30실 이상에서 50실 이상으로 완화",
    "url": "https://biz.chosun.com/real_estate/real_estate_general/2025/10/01/BMJUQYTMIRAS7KY5WKJ7GBJT4Y/"
  },
  {
    "date": "2025-10-01",
    "title": "서울시, 민간임대 리츠 지원을 위해 서울주택진흥기금 활용 (초기 출자금 부담 완화)",
    "url": "https://biz.chosun.com/real_estate/real_estate_general/2025/10/01/BMJUQYTMIRAS7KY5WKJ7GBJT4Y/"
  },
  {
    "date": "2025-05-20",
    "title": "서울시, 소규모재건축 용적률 3년간 한시적 완화 (제2종 250%, 제3종 300%까지 상향) - 도시계획조례 개정 시행",
    "url": "https://www.housingherald.co.kr/news/articleView.html?idxno=50107"
  },
  {
    "date": "2024-08-08",
    "title": "정부, '국민 주거안정을 위한 주택공급 확대방안' 발표 - 비아파트 매입임대주택 목표 12만호→16만호 이상 확대",
    "url": "https://www.aru.or.kr/issue/55"
  },
  {
    "date": "2024-08-08",
    "title": "정부, 생애 최초 소형주택(아파트 제외) 구입자 취득세 감면 한도 200만원→300만원으로 확대",
    "url": "https://www.taxtimes.co.kr/news/article.html?no=265844"
  },
  {
    "date": "2024-08-08",
    "title": "정부, 임대인이 소형주택 구입 시 세제상 주택수 제외 기간 2027년까지 확대 (비아파트 시장 정상화)",
    "url": "https://www.taxtimes.co.kr/news/article.html?no=265844"
  },
  {
    "date": "2024-01-01",
    "title": "정부, 소형·저가 임차주택 취득자에게 생애최초주택 취득세 감면(200만원 한도) 1회 추가 지원 특례 적용 기간 시작 ('24.1.1.~'25.12.31.)",
    "url": "https://www.ulleung.go.kr/ko/page.do?mnu_uid=1894"
  }
]

# ----------------------------------------------------
# 2. trafilatura를 이용한 본문 추출 및 저장 로직 (파일명 형식 변경)
# ----------------------------------------------------
for i, item in enumerate(data_list, 1):
    url = item['url']
    title = item['title']
    date = item['date']
    
    # 파일명에 사용할 날짜 형식 (YYYYMMDD) 지정
    date_str = date.replace('-', '') if date else "99999999"
    
    print(f"[{i}/{len(data_list)}] URL 처리 중: {url} (Date: {date_str})")
    
    try:
        # 1. URL에서 HTML 다운로드 및 본문 텍스트 추출
        downloaded = trafilatura.fetch_url(url)
        
        if downloaded is None:
            print(f"  > [SKIP] HTML 다운로드 실패: {url}")
            continue

        main_text = trafilatura.extract(downloaded, favor_recall=True, include_tables=False)

        if main_text:
            # 2. 본문 길이 확인 및 필터링 (300자 미만 스킵)
            if len(main_text) < 300:
                print(f"  > [SKIP] 본문이 300자 미만입니다. ({len(main_text)}자)")
                continue

            # 3. 파일 이름 형식 지정 및 저장: 01_YYYYMMDD_title[:20].txt
            # 파일명으로 사용할 수 없는 특수 문자 제거
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_', '-'))
            filename = f"{i:02d}_{date_str}_{safe_title[:20].replace(' ', '_')}.txt"
            file_path = os.path.join(output_dir, filename)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"Title: {title}\n")
                f.write(f"Date: {date_str}\n")
                f.write(f"URL: {url}\n\n")
                f.write("-" * 30 + " Main Text " + "-" * 30 + "\n\n")
                f.write(main_text)
            
            print(f"  > [SUCCESS] 본문 추출 및 저장 완료: {file_path} ({len(main_text)}자)")
            
        else:
            print("  > [SKIP] trafilatura가 본문 텍스트를 추출하지 못했습니다.")

    except Exception as e:
        print(f"  > [ERROR] 처리 중 오류 발생: {e}")

print("\n--- 모든 URL 처리 완료 ---")
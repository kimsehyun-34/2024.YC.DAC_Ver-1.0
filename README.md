# 2024.YC.DAC_Ver-1.0
Yeongju City Data Analysis Contest - 영주시 데이터분석 공모전

<div>
  <img style="float:left" src="https://img.shields.io/badge/R-276DC3?style=flat-square&amp;logo=r&amp;ogoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/QGIS-589632?style=flat-square&amp;logo=qgis&amp;logoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&amp;logo=google colab&amp;logoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/Excel-217346?style=flat-square&amp;logo=microsoft excel&amp;logoColor=white" width="auto" height="40" />
</div>

-----
# 연구 요약
- 2011년부터 2020년까지 영주시 청년 인구가 41.4%까지 감소한 상황이다.
- 2024년을 시작으로 사회와 환경적으로 문제가 되고 있는 빈집을 매입해 주민 공유시설로 조성하는 빈집 정비활용 사업을 추진하고 있다. 
- 이에 따라, 본 연구에서 청년 소멸지역으로 손꼽히는 영주시에 어떠한 청년시설이 어느 지역에 들어가야 청년 인구 증가에 효과적인지 알아보았다. 
- 2018년을 기준으로 2020년, 의성군은 청년 시설과 프로그램의 증가로 청년 인구 감소를 극복한 사례가 있으며, 이에 따라 영주시의 청년 시설을 강조하고 다중회귀, 결정트리, 랜덤포레스트 알고리즘을 활용하여 위에 언급된 문제점을 다각적 측면에서 고려하여 후보지역을 선정하고, 각 후보지에 타당한 청년시설을 함께 제안하였다.

-----

# 분석 데이터

- ### 인구 데이터
  - 행정안전부, 주민등록 인구통계
  - 경상북도 빅데이터 통합플랫폼 GB모아, 경상북도 시군구연령별 취업자 및 고용률
  
- ### 교육시설
  - 학교 - 경상북도 빅데이터 통합플랫폼 GB모아
  - 학원 - 중소벤처기업부 상권정보 누리집
  - 유치원 - 경상북도 빅데이터 통합플랫폼 GB모아
  - 도서관 - 경상북도 빅데이터 통합플랫폼 GB모아
 
- ### 문화시설
  - 유흥시설 - 문화체육관광부 문화샘터 누리집
  - 미술관 - 문화체육관광부 문화샘터 누리집

- ### 체육시설
  - 공원 - 경상북도 빅데이터 통합플랫폼 GB모아
  - 체육관 - 문화체육관광부 문화샘터 누리집
 
- ### 의료 & 복지시설
  - 병원 & 보건소 - 건강보험심사평가원 보건 의료빅데이터 개방 시스템
  - 약국 - 중소벤처기업부 상권정보 누리집
  - 복지 센터 - 경상북도 빅데이터 통합플랫폼 GB모아
 
- ### 주거 & 교통시설
  - 평당 평균 전세값 - 국토교통부, 국토교통부 실거래 공개시스템
  - 버스 정류장 - 경상북도 빅데이터 통합플랫폼 GB모아
 
- ### 편의시설
  - 커뮤니티 시설 - 중소벤처기업부 상권정보 누리집
  - 편의점 & 슈퍼마켓 - 중소벤처기업부 상권정보 누리집

-------------
# 전처리 & 분석

 - ## 다중공선성 & 다중선형휘귀
  <img style="text-align:center;" src="https://github.com/FURY312/2024.YC.DAC_Ver-1.0/blob/main/README_img/1.png" width="1000px" height="aoto"/>

 - ## Grid Search
  <img style="text-align:center;" src="https://github.com/FURY312/2024.YC.DAC_Ver-1.0/blob/main/README_img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-05-10%20153924.png" width="1000px" height="aoto"/>

-------------
# 분석결과
 - ## 영주 1, 2 동
  <img style="text-align:center;" src="https://github.com/FURY312/2024.YC.DAC_Ver-1.0/blob/main/README_img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-05-10%20153939.png" width="1000px" height="aoto"/>

 - ## 영주 풍기읍
  <img style="text-align:center;" src="https://github.com/FURY312/2024.YC.DAC_Ver-1.0/blob/main/README_img/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-05-10%20153954.png" width="1000px" height="aoto"/>

------------
# 참고문헌

 - [1] 이유재(1994). 상호작용효과를 포함한 다중회귀분석에서 주효과의 검증에 대한 연구, 경영학연구.
 - [2] 고정우, 이주림, 구자훈. (2023). 대도시 및 중소도시 입지별 혁신도시의 청년인구 유입효과 비교분석. 한국지역개발학회지, 35(2), 45-68.
 - [3] 김재환, 이민구(2018). 의사 결정 트리와 랜덤 포레스트 모델 분석, 한국정보기술학회, 한국디지털콘텐츠학회
 - [4] 박태일. "인공지능 알고리즘과 최적화 기법의 결합을 통한 비선형 회귀 알고리즘 개발." 국내석사학위논문 한국항공대학교 일반대학원, 2023. 경기도
 - [5] 이광원. (2023). 위계적 다중 회귀분석을 활용한 지방소멸 요인이 핵심생산가능인구의 순이동에 미치는 영향. 한국정책과학학회보, 27(3), 131-155, 10.31553/kpsr.2023.9.27.3.131
 - [6] 손창희, 장한두. (2019). 지방도시의 노후주거지 정비와 관리 정책에 관한 연구 - 주거환경개선사업의 도시규모별 대안을 중심으로 -. 주거환경, 17(2), 197-214.
 - [7] 조현영, 이상복, 김홍렬, 외 2인, (2012). 전국 도서관 통계 조사지표 개선 연구, 문화체육관광부.
 - [8]J. T. Park and H. S. Jang, “A Regional Comparison Study for the Variability of Employment Statistics in Korean Young Man: Focus on EconomicallyActive Population Rate, Employment Population Rate, Unemployment Rate,” Journal of Service Research and Studies, vol. 5, no. 1, pp. 35–43, Mar. 2015.

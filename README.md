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
## 연구 요약
- 2011년부터 2020년까지 영주시 청년 인구가 41.4%까지 감소한 상황이다.
- 2024년을 시작으로 사회와 환경적으로 문제가 되고 있는 빈집을 매입해 주민 공유시설로 조성하는 빈집 정비활용 사업을 추진하고 있다. 
- 이에 따라, 본 연구에서 청년 소멸지역으로 손꼽히는 영주시에 어떠한 청년시설이 어느 지역에 들어가야 청년 인구 증가에 효과적인지 알아보았다. 
- 2018년을 기준으로 2020년, 의성군은 청년 시설과 프로그램의 증가로 청년 인구 감소를 극복한 사례가 있으며, 이에 따라 영주시의 청년 시설을 강조하고 다중회귀, 결정트리, 랜덤포레스트 알고리즘을 활용하여 위에 언급된 문제점을 다각적 측면에서 고려하여 후보지역을 선정하고, 각 후보지에 타당한 청년시설을 함께 제안하였다.

-----

## 분석 데이터

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



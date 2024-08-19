## 🪄 팀원 소개
**SKN03-2nd-2Team :**   
**✨세일러문과 데스버스터즈✨**
| ![moonheesun](https://github.com/user-attachments/assets/b5d46fe6-0d89-473e-b362-259863a1ecb1) | ![cassandra](https://github.com/user-attachments/assets/a9dcf684-9ec4-4a95-a41c-b23df70fec2b) | ![kimjaesung](https://github.com/user-attachments/assets/c4a9707d-61a0-4514-9084-67ed06e0f882) | ![songyoungbin](https://github.com/user-attachments/assets/7510c205-86c5-4338-8377-7d5b4602e894) | ![jinyunhwa](https://github.com/user-attachments/assets/ba811840-9e0d-47df-a323-295fdea80184) | 
|:----------:|:----------:|:----------:|:----------:|:----------:|
| 문희선 (PM) | 박중헌 | 김재성 | 송영빈 | 진윤화 |   

# 🍿Moonvie
## Ⅰ. 프로젝트 개요
**📌프로젝트 목적📌**   
   
코로나19 팬데믹은 영화 산업에 상당한 변화를 가져왔습니다. 팬데믹 이전에는 영화관에서의 관람이 주요 소비 방식이었으나, 팬데믹 동안 많은 영화관이 문을 닫고 사람들은 집에서 콘텐츠를 소비하는 방식으로 전환되었습니다.    
그러나 여전히 상업적으로 살아남는 영화는 존재합니다. **코로나19 팬데믹 이전 이후 상업적으로 성공한 영화에 대한 데이터를 분석**함으로써,  **영화 제작자들이 팬데믹 이후 변화된 환경에서 경쟁력을 갖출 수 있도록 인사이트를 제공**하고자 합니다.
   
**📌프로젝트 내용📌**   
###   
① **계절별/특정기간별 흥행 영화장르 특징 분석**
- 월별, 분기별 관객수가 많은 영화 장르, 특징 분석
- 명절 , 크리스마스 등 특정 기간의 인기 영화 장르
- 코로나 이전과 이후 영화 관객 수, 매출 분석

   
② **기간, 장르, 지역별 인기 영화 순위**
- 기간, 장르, 지역을 선택했을 때 인기 영화 순위 그래프
- 기간, 장르, 지역에 따른 인기 영화의 상관관계 분석

③ **워드클라우드를 통한 제작사별 인기영화**
- 인기 영화 제작사와 제작사 별 인기영화 분석
- 제작사에 따른 인기 영화의 상관관계 분석

## Ⅱ. 프로젝트 요구사항

1. **영화 정보 API 샘플 데이터 확인 및 사용 여부 확정**
    - 사용 가능 여부 확인 및 주요 기능과 연관지을 수 있는지 검토
    - 오픈API에서 각 항목별로 샘플 추출 후, 주요 기능 중 가능한 기능 정리
      

2. **프론트엔드 주요 기능 화면 설계**
    - 피그마를 이용한 화면 설계
    - 디자인적 요소는 추후 고려, 우선 기능 위주로 설계
    - 필요한 화면 구성: 월별/분기별 관객수가 많은 영화, 기간별/장르별 인기도, 관객 분석
    - 담당자: 송영빈, 진윤화

3. **기간별 인기 순위 통계 & 장르별 인기 순위 통계**
- 전처리
    - RAW data는 따로 구글 드라이브에 저장
    - 제외할 행 및 컬럼 제거
    - null 값 처리 방법 결정
- 인기 순위 통계
    - 기간/장르 선택 시 인기 영화 순위 그래프
    - 장르 표현 예시: 워드 클라우드
    - 기간별 인기 순위 작품들의 장르 분석
      3. 분석 결과 정리

4. **지역별 인기 순위 통계**
- 전처리
    - RAW data는 따로 구글 드라이브에 저장
    - 제외할 행 및 컬럼 제거
    - null 값 처리 방법 결정
- 인기 순위 통계
    - 지역 선택 시 인기 영화 순위 그래프
    - 기간/장르/지역 간의 상관관계 분석
- 분석 결과 정리

5. **코로나 전후 흥행 영화 분석**

6. **화면 구축**
    - 홈
    - 인기 순위 페이지(기간별/장르별/지역별)
    - 기간/장르/지역 간의 상관관계 분석 결과 페이지
    - API 관리
    - 라우터 관리
    - 차일드 컴포넌트 관리

7. **데이터 분석**
    - 수집된 데이터셋 활용하여 주요 기능 수정 보완
    - 시즌에 따른 흥행 영화 특징 분석
    - 기간별, 장르별, 지역별 인기 순위 분석
    - 코로나 시기 구분 및 데이터 분석

8. **AWS 및 백엔드 연동 준비**



## Ⅲ. Diagram

**1. ER Diagram**
   
![image](https://github.com/user-attachments/assets/d707eb79-3319-4626-ad81-1f1da990278a)

**2. Architecture**
   
![architecture drawio](https://github.com/user-attachments/assets/0072009a-97c7-4bb3-bcfa-69865ad19b93)


## Ⅳ. 실제동작화면
<img width="566" alt="image" src="https://github.com/user-attachments/assets/0ab2e7a3-3664-414e-b585-3e94f4031736">



## Ⅴ. 컨벤션 규칙
### 1. Language-specific Default Style Extention

**Python**
- black formatter

**JavaScript**
- Formatter : Prettier
- Linter : ESLint
  
**Prettier Setting**
```
{
  "$schema": "https://json.schemastore.org/prettierrc",
  "semi": false,
  "tabWidth": 2,
  "singleQuote": true,
  "printWidth": 100,
  "trailingComma": "none"
}
```

### 2. git commit 컨벤션

- **feat** : 새로운 기능 추가
- **fix** : 버그 수정
- **docs** : 문서 수정
- **style** : (코드의 수정 없이) 스타일(style)만 변경(들여쓰기 같은 포맷이나 세미콜론을 빼먹은 경우)
- **refactor** : 코드 리펙토링
- **test** : Test 관련한 코드의 추가, 수정
- **chore** : (코드의 수정 없이) 설정 변경

### 3. Git Branch 전략

**Git Flow 전략 사용**

1. 각자 개발하는 기능별 feature branch 생성
2. 각자의 feature branch에서 작업
3. 작업이 완료된 feature 브랜치는 develop 브랜치에 Pull Request 를 통해 작업 내용을 Review 
4. develop 브랜치로 Merge
5. 일정한 주기로 main 브랜치에 Merge
6. 미처 발견되지 못한 버그들은 hotfix 브랜치에 바로 반영




## VI. 오류 해결 과정

## VII. 프로젝트 한줄평
- **문희선**
   
- **박중헌**
   
- **김재성**
다음엔 꼭 1인분 몫은 해야겠다고 생각합니다! 팀원들 고생 많았습니다!
- **진윤화**
협업시 소통의 중요성과 충돌관리의 중요성을 깨닫고, 일정 관리의 중요성을 느꼈으며, 프로그램 설계 시 구조의 중요성을 배웠습니다. 또한, 코드 작성 시 가독성을 높이는 것이 중요하다는 것을 깨달았고, Vue.js 사용 시 CLI보다 Vite가 여러 면에서 장점이 많다는 것을 알게 되었습니다.    
- **송영빈**
협업 시 git 사용법이 조금 더 익숙해지는 기회가 되었고 부족한 점이 많다는 걸 이번 프로젝트를 통해 더욱 느끼게 되었습니다. 프론트엔드, 데이터 전처리, MySQL 등등 배운점이 많기도 한 프로젝트였습니다.



## VIII. 기술 스택

<div style="display: flex; gap: 10px;">
<h3>Language</h3>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" style="height: 40px; object-fit: contain;">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" style="height: 40px; object-fit: contain;">
</div>      


<div style="display: flex; gap: 10px;">
<h3>Frontend</h3>
  <img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white" alt="Vue.js" style="height: 40px; object-fit: contain;">
  <img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=flat-square&logo=Tailwind%20CSS&logoColor=white" alt="Tailwind CSS" style="height: 40px; object-fit: contain;">
</div>      
    

<div style="display: flex; gap: 10px;">
<h3>Backend</h3>
   <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white" alt="Django" style="height: 40px; object-fit: contain;">
</div>  

<div style="display: flex; gap: 10px;">
<h3>Database</h3>
   <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" style="height: 40px; object-fit: contain;">
</div>  

<div style="display: flex; gap: 10px;">
<h3>Deployment</h3>
   <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="Amazon AWS" style="height: 40px; object-fit: contain;">
</div>  

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



## Ⅳ. 컨벤션 규칙
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




## Ⅴ. 오류 해결 과정
- Mysql user
```
use mysql;

select host, user, authentication_string from user;

CREATE USER 'moonvie'@'%'
	IDENTIFIED by 'moonvie0816@';

create user 'root'@'%'
	identified by 'asdf';

GRANT All privileges ON moonvieDB.* TO 'moonvie'@'%';
drop user 'root'@'%';

flush privileges; # 중요
```
---
- db data insert 과정 중 data type 문제 발생
        ![image](https://github.com/user-attachments/assets/11cba768-c112-4a6a-a83d-cc37654ef3bf)
   -  누적 매출액 → int 범위 벗어나는 경우 발생
 
---
- 에러명

> File "C:\projects\SKN03-2nd-2Team\moonvie-backend\.venv\Lib\site-packages\drf_yasg\**init**.py", line 2, in <module>
from pkg_resources import DistributionNotFound, get_distribution
ModuleNotFoundError: No module named 'pkg_resources'

- 에러 설명
```
  drf_yasg python라이브러리를 사용하려고 했는데 해당 에러가 발생하였다.
drf_yasg가 setuptools모듈을 사용하고 있는데 해당 모듈이 없어서 발생하는 에러이다.
```

- 해결 방법
   - setuptools를 다운받으면 간단하게 해결된다.
```
 pip install setuptools
```
---

- wordcloud가 화면 오른쪽에 치우쳐져 있고 중간으로 가지 않음
   - wordcloud가 있는 div의 class를 wordcloud로 설정하고 CSS를 통해 정렬함     
---
- wordcloud가 json 데이터를 받아오는 속도가 느리고 데이터가 많아지면 출력되지 않음
    - vuewordcloud 에서 echarts wordcloud를 바꿔서 사용하니까 데이터가 거의 바로 출력됨.
---
- 데이터 전처리 과정에서 ‘상영월’ 기준으로 중복된 데이터를 없애려고 했는데 데이터 대부분이 사라짐
    - 기준이 되는 컬럼을 ‘영화 코드’와 ‘상영월’을 기준으로 해서 정상적으로 처리함
---
- frontend 충돌 : 프론트엔드 작업 중 서로 config를 상의하지 않고 추가해서 commit 하는 과정에서 충돌이 일어남
    - 하나의 config에 맞춰 한쪽 코드를 새로 작성하여 해결함
        
        1. vue.config.js 설정 통일
        
        2. GenreTable.vue의 csv load관련 코드 수정
        
        3. MoonvieGenre.vue와 GenreTable.vue 연결
---
- 데이터를 정렬했을 때, 중복된 데이터들이 나타나는 오류가 발생함.
![image](https://github.com/user-attachments/assets/19dd6cc4-902c-4ee4-8a43-f1ffdb98c577)
   - 해당 데이터를 필터링하여, 데이터의 중복을 막음
   - 데이터가 중복 되는 이유
       - 해당 데이터셋이 각 주마다 박스오피스를 가져오기 때문에, 특정 영화가 연속적으로 박스오피스에 오를 경우 중복되는 데이터가 발생함
   - 해결 방법
      1. 영화의 이름을 담은 MovieNm변수를 생성
      2. 누적 관객수를 담은 audiAcc 변수를 생성
      3. MovieNm와 audiAcc를 담은 acc배열을 생성
      4. acc배열에서 current.movieNm와 동일한 movieNm을 가진 항목을 찾음
          1. 동일한 값이 없을 경우, acc에 current값을 return
          2. 동일한 값이 존재할때
              1. 현재 current.audiAcc의 값이 높을 경우 acc의 값을 current로 대체함
              2. acc의 auidAcc가 높을경우 acc를 리턴함
```
  // 중복된 movieNm 제거 및 audiAcc가 높은 순으로 정렬
  const uniqueData = filtered
    .reduce((acc, current) => {
      const x = acc.find((item) => item.movieNm === current.movieNm)
      if (!x) {
        return acc.concat([current])
      } else if (x.audiAcc < current.audiAcc) {
        return acc.map((item) => (item.movieNm === current.movieNm ? current : item))
      } else {
        return acc
      }
    }, [])
    .sort((a, b) => b.audiAcc - a.audiAcc)

  filteredData.value = uniqueData
}
```
   - 결과
       - 중복되는 데이터가 삭제되고 정상적으로 데이터가 출력됨
---
- cli에서 vite로 마이그레이션
    - 기존 cli에 비하여 vite의 장점이 많으므로, cli에서 vite로 마이그레이션을 함
    - 빠른 개발 서버 시작: Vite는 네이티브 ES 모듈을 사용하여 브라우저에서 직접 로드하기 때문에 개발 서버 시작 속도가 cli에 비해 빠름.
    - 빠른 빌드 속도: Vite는 ES 모듈을 기반으로 하기 때문에 초기 빌드와 재빌드 속도가 cli에 비해 빠름
    - 효율적인 핫 모듈 교체(HMR): Vite는 모듈의 변화가 있을 때 변경된 부분만 빠르게 갱신하는 HMR을 제공함
    - 간편한 설정 및 커스터마이징: Vite는 설정 파일(vite.config.js/ts)을 기본적으로 제공하며, 프로젝트 요구사항에 맞게 쉽게 커스터마이징할 수 있음.
- Bootstrap 인식 에러
    - cli에서 vite로 마이그레이션 하는 과정에서, bootstrap패키지가 package.json에서 누락되어서, 마이그레이션된 frontend에서 정상적으로 실행되지 않는 에러 발생
    - 해결 과정
        - package.json의 dependencies에 bootstrap추가
   - 이후 npm install을 실행하여 bootstrap을 설치 후 실행
   - 결과
       - 정상적으로 페이지가 출력됨
---

## VI. 프로젝트 한줄평
- **문희선**   
설계의 중요성과 더불어 개인적인 역량에 대해 깊이 반성하는 시간이었습니다. 이전보다 나날이 발전하도록 노력해야겠다는 생각이 간절히 들었습니다.   
- **박중헌**   
설계의 중요함과 팀원간의 역할 배분에 대해 고찰을 하는 시간을 가졌고 일정 관리 및 팀원관리, 소통에 대해 뼈져리게 느꼈습니다.   
- **김재성**   
다음엔 꼭 1인분 몫은 해야겠다고 생각합니다! 팀원들 고생 많았습니다!
- **진윤화**   
협업시 소통의 중요성과 충돌관리의 중요성을 깨닫고, 일정 관리의 중요성을 느꼈으며, 프로그램 설계 시 구조의 중요성을 배웠습니다. 또한, 코드 작성 시 가독성을 높이는 것이 중요하다는 것을 깨달았고, Vue.js 사용 시 CLI보다 Vite가 여러 면에서 장점이 많다는 것을 알게 되었습니다.    
- **송영빈**   
협업 시 git 사용법이 조금 더 익숙해지는 기회가 되었고 부족한 점이 많다는 걸 이번 프로젝트를 통해 더욱 느끼게 되었습니다. 프론트엔드, 데이터 전처리, MySQL 등등 배운점이 많기도 한 프로젝트였습니다.



## VII. 기술 스택

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

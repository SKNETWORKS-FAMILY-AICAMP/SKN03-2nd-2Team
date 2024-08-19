import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGenreStore = defineStore(
  // 스토어 이름 정의
  'genre',
  () => {
    const seasons = ref(['봄', '여름', '가을', '겨울'])

    const seasonsGenreData = ref({
      봄: {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      여름: {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      가을: {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      겨울: {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      }
    })
    const holidays = ref(['명절(설, 추석)', '가정의 달(5월)', '크리스마스(12월)'])

    const holidaysGenreData = ref({
      '명절(설, 추석)': {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      '가정의 달(5월)': {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      '크리스마스(12월)': {
        드라마: 4823,
        '성인물(에로)': 4112,
        '멜로/로맨스': 3502,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      }
    })

    const covid = ref(['코로나 전', '코로나 후'])

    const covidGenreData = ref({
      '코로나 전': {
        드라마: 5999,
        '성인물(에로)': 4556,
        '멜로/로맨스': 3964,
        액션: 3649,
        코미디: 1648,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      },
      '코로나 후': {
        드라마: 6700,
        '성인물(에로)': 5555,
        '멜로/로맨스': 4444,
        액션: 2433,
        코미디: 1897,
        애니메이션: 1492,
        '공포(호러)': 1417,
        스릴러: 945,
        범죄: 746,
        SF: 567,
        미스터리: 340,
        기타: 328,
        전쟁: 322,
        판타지: 290,
        어드벤처: 259,
        다큐멘터리: 232,
        가족: 186,
        사극: 138,
        '서부극(웨스턴)': 77,
        뮤지컬: 61,
        공연: 35,
        로맨스: 10,
        일상: 5,
        호러: 5
      }
    })
    return {
      seasons,
      seasonsGenreData,
      holidays,
      holidaysGenreData,
      covid,
      covidGenreData
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)

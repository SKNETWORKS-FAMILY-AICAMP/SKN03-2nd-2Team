import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGenreStore = defineStore(
  // 스토어 이름 정의
  'genre',
  () => {
    const seasons = ref(['봄', '여름', '가을', '겨울'])

    const seasonsGenreData = ref({
      봄: {
        로맨스: 10,
        코미디: 10,
        드라마: 10,
        일상: 5,
        액션: 10,
        스릴러: 10,
        호러: 5,
        판타지: 5
      },
      여름: { Action: 35, Adventure: 30, 'Sci-Fi': 20, Comedy: 15 },
      가을: { Mystery: 30, Thriller: 25, Horror: 25, Drama: 20 },
      겨울: { Fantasy: 35, Romance: 25, 'Slice of Life': 20, Drama: 20 }
    })
    const holidays = ref(['명절(설, 추석)', '가정의 달(5월)', '크리스마스(12월)'])

    const holidaysGenreData = ref({
      '명절(설, 추석)': {
        로맨스: 10,
        코미디: 10,
        드라마: 10,
        일상: 5,
        액션: 10,
        스릴러: 10,
        호러: 5,
        판타지: 5
      },
      '가정의 달(5월)': { Action: 35, Adventure: 30, 'Sci-Fi': 20, Comedy: 15 },
      '크리스마스(12월)': { Mystery: 30, Thriller: 25, Horror: 25, Drama: 20 }
    })

    const covid = ref(['코로나 전', '코로나 후'])

    const covidGenreData = ref({
      '코로나 전': {
        로맨스: 10,
        코미디: 10,
        드라마: 10,
        일상: 5,
        액션: 10,
        스릴러: 10,
        호러: 5,
        판타지: 5
      },
      '코로나 후': { Action: 35, Adventure: 30, 'Sci-Fi': 20, Comedy: 15 }
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

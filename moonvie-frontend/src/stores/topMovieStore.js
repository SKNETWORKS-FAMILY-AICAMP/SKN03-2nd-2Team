import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTopMovieStore = defineStore(
  // 스토어 이름 정의
  'topMovie',
  () => {
    const topMovies = ref([
      { movie_name: '반도', genre: '성', open_date: '2001-07-04', audience: 100, sales: 200 },
      { movie_name: '마녀', genre: '씨', open_date: '2001-07-03', audience: 33, sales: 300 }
    ])
    const startDate = ref('')
    const endDate = ref('')
    const minDate = 201701
    const maxDate = ref(0)
    const error = ref('')

    const limitInput = (dateRef) => {
      dateRef.value = dateRef.value.replace(/[^0-9]/g, '').slice(0, 6)
    }

    const validateDates = () => {
      const startYearMonth = parseInt(startDate.value)
      const endYearMonth = parseInt(endDate.value)

      if (startDate.value.length !== 6 || endDate.value.length !== 6) {
        error.value = '날짜는 YYYYMM 형식으로 6자리 숫자여야 합니다.'
        return false
      } else if (
        startYearMonth < minDate ||
        startYearMonth > maxDate.value ||
        endYearMonth < minDate ||
        endYearMonth > maxDate.value
      ) {
        error.value = `입력 가능한 날짜는 ${minDate}부터 ${maxDate.value}까지입니다.`
        return false
      } else if (startYearMonth > endYearMonth) {
        error.value = '시작 날짜가 종료 날짜보다 늦을 수 없습니다.'
        return false
      } else {
        return true
      }
    }
    return {
      topMovies,
      startDate,
      endDate,
      minDate,
      maxDate,
      error,
      limitInput,
      validateDates
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)

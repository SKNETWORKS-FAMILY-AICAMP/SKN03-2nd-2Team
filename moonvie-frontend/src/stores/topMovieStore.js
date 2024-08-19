import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTopMovieStore = defineStore(
  // 스토어 이름 정의
  'topMovie',
  () => {
    const topMovies = ref([
      {
        movie_name: '반도',
        genre: '액션',
        open_date: '2001-07-04',
        audience: 100400000,
        sales: 2321452500
      },
      {
        movie_name: '한양',
        genre: '로맨스',
        open_date: '2001-07-04',
        audience: 99030000,
        sales: 20867590
      },
      {
        movie_name: '개망',
        genre: '판타지',
        open_date: '2001-07-04',
        audience: 87000000,
        sales: 24753274
      },
      {
        movie_name: '도깨비',
        genre: '성인물',
        open_date: '2001-07-04',
        audience: 76010000,
        sales: 365461
      },
      {
        movie_name: '파멸',
        genre: '코미디',
        open_date: '2001-07-04',
        audience: 58520000,
        sales: 786786789
      },
      {
        movie_name: '증오',
        genre: '코미디',
        open_date: '2001-07-04',
        audience: 53020000,
        sales: 9476967
      },
      {
        movie_name: '배반',
        genre: '드라마',
        open_date: '2001-07-04',
        audience: 41000000,
        sales: 4756564
      },
      {
        movie_name: '경멸',
        genre: '서부극',
        open_date: '2001-07-04',
        audience: 39007654,
        sales: 4567654
      },
      {
        movie_name: '남산의 부장들',
        genre: '코미디',
        open_date: '2001-07-04',
        audience: 33202643,
        sales: 1421452421
      },
      {
        movie_name: '마녀',
        genre: '다큐멘터리',
        open_date: '2001-07-03',
        audience: 13326534,
        sales: 432563426
      }
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

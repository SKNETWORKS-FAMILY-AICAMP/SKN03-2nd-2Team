import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useTopMovieStore = defineStore(
  // 스토어 이름 정의
  'topMovie',
  () => {
    const topMovies = ref([
      '테넷',
      '반도',
      '남산의 부장들',
      '다만 악에서 구하소서',
      '에나벨',
      '파묘',
      '소리도 없이',
      '기생충',
      '아웃포스트',
      '리플레이'
    ])
    const movieInfo = ref([
      { name: '장르', subName: '', value: '성인물' },
      { name: '개봉일', subName: '', value: '2012.05.21' },
      { name: '누적 관객수', subName: '명', value: 405 },
      { name: '누적 매출액', subName: '원', value: 4050000 }
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
      } else if (
        startYearMonth < minDate ||
        startYearMonth > maxDate.value ||
        endYearMonth < minDate ||
        endYearMonth > maxDate.value
      ) {
        error.value = `입력 가능한 날짜는 ${minDate}부터 ${maxDate.value}까지입니다.`
      } else if (startYearMonth > endYearMonth) {
        error.value = '시작 날짜가 종료 날짜보다 늦을 수 없습니다.'
      } else {
        error.value = ''
        console.log('유효한 날짜:', startDate.value, endDate.value)
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
      validateDates,
      movieInfo
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)

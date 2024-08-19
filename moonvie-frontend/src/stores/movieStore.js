import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useMovieStore = defineStore(
  // 스토어 이름 정의
  'movie',
  () => {
    // 객체, 함수 선언 스코프
    const navigation = ref([
      { name: '홈', href: '/', current: true },
      { name: 'TOP Movies', href: '/top', current: false },
      { name: 'Movie Cloud', href: '/cloud', current: false },
      { name: '인기 장르', href: '/genre', current: false },
      { name: '시즌별 인기 영화', href: '/season', current: false },
      { name: '지역별 인기 영화', href: '/region', current: false },
      { name: '코로나 전후 영화 누적 매출/관객수', href: '/covid', current: false }
    ])
    const genreTabs = ref([
      { name: '계절별', current: true },
      { name: '연휴별', current: false },
      { name: '코로나 전/후', current: false }
    ])
    const covidTabs = ref([
      { name: '평균 누적 매출액', current: true },
      { name: '평균 누적 관객수', current: false }
    ])
    const currentTab = ref(0)
    const currentCovidTab = ref(0)
    const setNavCurrent = (itemName) => {
      navigation.value.forEach((item) => {
        item.current = item.name === itemName
      })
    }
    const setTabCurrent = (itemName) => {
      genreTabs.value.forEach((item) => {
        item.current = item.name === itemName
      })
      currentTab.value = genreTabs.value.findIndex((item) => item.name === itemName)
    }
    const setCovidTabCurrent = (itemName) => {
      covidTabs.value.forEach((item) => {
        item.current = item.name === itemName
      })
      currentCovidTab.value = covidTabs.value.findIndex((item) => item.name === itemName)
    }
    return {
      navigation,
      genreTabs,
      covidTabs,
      setNavCurrent,
      setTabCurrent,
      currentTab,
      currentCovidTab,
      setCovidTabCurrent
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCounterStore = defineStore(
  'counter',
  () => {
    // 객체, 함수 선언 스코프
    const honey = ref('')
    const viewMode = ref('table') // 기본값을 table로 설정

    return {
      honey,
      viewMode
      // 반환값들 (위에서 생성한 객체, 함수 등등.)
    }
  },
  {
    persist: true // 지속성-persistence store이 되게 설정 (Composition API)
  }
)

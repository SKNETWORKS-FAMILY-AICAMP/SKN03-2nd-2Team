<template>
  <div class="chart-container">
    <Chart
      :size="{ width: 600, height: 400 }"
      :data="data"
      :margin="margin"
      :direction="direction"
      :axis="axis"
    >
      <template #layers>
        <Grid strokeDasharray="2,2" />
        <Bar
          :dataKeys="['제목', '누적 관객수']"
          :barStyle="{ fill: '#FFC77D' }"
          :label="{ position: 'top', fill: 'white' }"
        />
      </template>

      <template #widgets>
        <Tooltip
          borderColor="#48CAE4"
          :config="{
            '누적 관객수': { color: '#90e0ef' }
          }"
        />
        <Legend />
      </template>
    </Chart>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Chart, Grid, Bar, Tooltip, Legend } from 'vue3-charts'

const data = ref([])
const direction = ref('horizontal')
const margin = ref({
  left: 0,
  top: 20,
  right: 20,
  bottom: 0
})

const axis = ref({
  primary: {
    type: 'band'
  },
  secondary: {
    domain: ['dataMin', 'dataMax + 100'],
    type: 'linear',
    ticks: 8
  }
})

onMounted(async () => {
  const response = await fetch('/src/assets/data/compare_data.json')
  const jsonData = await response.json()
  const sortedData = jsonData.sort((a, b) => b['누적 관객수'] - a['누적 관객수']).slice(0, 20)
  data.value = sortedData
})
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 부모 요소의 높이를 설정하여 중앙 정렬 */
}

.chart-container * {
  color: white; /* currentColor를 흰색으로 설정 */
}
</style>

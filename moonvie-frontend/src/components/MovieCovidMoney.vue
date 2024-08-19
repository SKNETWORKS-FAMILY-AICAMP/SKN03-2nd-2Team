<script setup>
import { ref } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'
import * as covidApi from '@/api/covid'

const getMoney = (req) => {
  covidApi
    .getMoneyCovid(req)
    .then((res) => {
      covidData.value = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}
getMoney()

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const generateLabels = () => {
  const labels = []
  for (let year = 2017; year <= 2024; year++) {
    const endMonth = year === 2024 ? 8 : 12
    for (let month = 1; month <= endMonth; month++) {
      labels.push(`${year}-${String(month).padStart(2, '0')}`)
    }
  }
  return labels
}

const covidData = ref([
  432, 241, 532, 235, 643, 647, 277, 575, 445, 754, 734, 375, 752, 538, 658, 675, 768, 87, 864, 785,
  658, 648, 665, 858, 658, 456, 588, 865, 453, 256, 564, 435, 232, 543, 232, 643, 754, 457, 343,
  754, 543, 456, 345, 678, 32, 845, 546, 548, 657, 653, 456, 765, 324, 765, 643, 435, 875, 653, 432,
  344, 222, 134, 98, 321, 534, 432, 222, 156, 765, 976, 687, 687, 674, 921, 128, 237, 112, 457, 237,
  232, 321, 123, 432, 211, 23, 656, 567, 908, 987, 435, 234, 123, 456, 789, 987, 654, 321, 123, 456
])
const labels = generateLabels()
const startRedIndex = labels.indexOf('2020-01')
const endRedIndex = labels.indexOf('2022-08')

const chartData = ref({
  labels: labels,
  datasets: [
    {
      label: '평균 매출액',
      backgroundColor: labels.map((label, index) =>
        index >= startRedIndex && index <= endRedIndex ? '#FF0000' : '#FFC77D'
      ),
      borderColor: labels.map((label, index) =>
        index >= startRedIndex && index <= endRedIndex ? '#FF0000' : '#FFC77D'
      ),
      borderWidth: 2,
      data: covidData.value
    }
  ]
})

const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
      labels: {
        color: '#ffffff'
      }
    },
    title: {
      display: true,
      text: '월별 평균 누적 매출액 (2017-2024)'
    }
  }
})
</script>

<template>
  <div>
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

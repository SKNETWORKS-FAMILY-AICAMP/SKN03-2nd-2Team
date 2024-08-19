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

const getPeople = (req) => {
  covidApi
    .getPeopleCovid(req)
    .then((res) => {
      covidData.value = res.data
    })
    .catch((e) => {
      console.log(e)
    })
}
getPeople()

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
const covidData = ref([])
const labels = generateLabels()
const startRedIndex = labels.indexOf('2020-01')
const endRedIndex = labels.indexOf('2022-08')

const chartData = ref({
  labels: labels,
  datasets: [
    {
      label: '평균 관객수',
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
      text: '월별 평균 누적 관객수 (2017-2024)'
    }
  }
})
</script>

<template>
  <div>
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

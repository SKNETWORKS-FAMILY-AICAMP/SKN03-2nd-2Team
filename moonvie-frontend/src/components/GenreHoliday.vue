<template>
  <div>
    <h2 class="text-3xl font-bold mb-8 text-white">연휴별 인기 장르</h2>
    <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
      <div v-for="holiday in holidays" :key="holiday" class="bg-gray-800 rounded-lg shadow-md p-6">
        <h3 class="text-xl font-semibold mb-4 text-center text-white">{{ holiday }}</h3>
        <div class="w-full h-screen">
          <Bar :data="getChartData(holiday)" :options="chartOptions" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useGenreStore } from '@/stores/genreStore'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

const genreStore = useGenreStore()
const { holidays, holidaysGenreData } = storeToRefs(genreStore)

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const chartOptions = {
  indexAxis: 'y',
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false // 범례를 숨깁니다
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        color: '#ffffff' // y축 눈금 색상을 흰색으로 설정
      }
    },
    x: {
      ticks: {
        color: '#ffffff' // x축 눈금 색상을 흰색으로 설정
      }
    }
  }
}

const getChartData = (season) => ({
  labels: Object.keys(holidaysGenreData.value[season]),
  datasets: [
    {
      data: Object.values(holidaysGenreData.value[season]),
      backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
      borderColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
      borderWidth: 1
    }
  ]
})
</script>

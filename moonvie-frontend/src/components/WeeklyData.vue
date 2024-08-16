<template>
  <div class="container mt-5">
    <h1 class="text-center">Weekly Box Office Data</h1>
    <div class="row mb-3">
      <div class="col-md-6">
        <label for="start-date" class="form-label">Start Date:</label>
        <input type="date" id="start-date" v-model="startDate" class="form-control" />
      </div>
      <div class="col-md-6">
        <label for="end-date" class="form-label">End Date:</label>
        <input type="date" id="end-date" v-model="endDate" class="form-control" />
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-md-6">
        <button @click="filterDataByDate" class="btn btn-primary w-100">검색</button>
      </div>
      <div class="col-md-6">
        <button @click="resetData" class="btn btn-secondary w-100">초기화</button>
      </div>
    </div>
    <div class="mb-3">
      <h2>출력할 열 선택</h2>
      <div class="dropdown">
        <button
          class="btn btn-secondary dropdown-toggle"
          type="button"
          id="dropdownMenuButton"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          data-bs-auto-close="outside"
        >
          열 선택
        </button>
        <div class="dropdown-menu dropdown-menu-grid p-3" aria-labelledby="dropdownMenuButton">
          <div class="row">
            <div v-for="header in headers" :key="header" class="col-6 col-md-4 dropdown-item">
              <input
                type="checkbox"
                :id="header"
                :value="header"
                v-model="selectedColumns"
                class="form-check-input me-2"
              />
              <label :for="header" class="form-check-label">{{ header }}</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <table v-if="isSearched" class="table table-striped table-bordered">
      <thead>
        <tr>
          <th v-for="header in selectedColumns" :key="header">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in filteredData" :key="row.id">
          <td v-for="header in selectedColumns" :key="header">{{ row[header] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import weeklyData from '@/assets/data/WeeklyData_0.json'

const startDate = ref('2017-01-01')
const endDate = ref(new Date().toISOString().split('T')[0]) // 오늘의 날짜를 기본값으로 설정
const selectedColumns = ref(['movieNm', 'openDt', 'audiAcc', 'showRange'])
const isSearched = ref(false)

const headers = Object.keys(weeklyData[0])

const filterDataByDate = () => {
  isSearched.value = true
  filteredData.value = weeklyData.filter((item) => {
    const itemDate = new Date(item.openDt)
    const start = new Date(startDate.value)
    const end = new Date(endDate.value)
    return itemDate >= start && itemDate <= end
  })
}

const resetData = () => {
  startDate.value = '2017-01-01'
  endDate.value = new Date().toISOString().split('T')[0]
  selectedColumns.value = ['movieNm', 'openDt', 'audiAcc', 'showRange']
  isSearched.value = false
  filteredData.value = weeklyData
}

const filteredData = ref(weeklyData)
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #333;
}

.date-filters {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.date-filters label {
  margin-right: 10px;
}

.date-filters input {
  margin-right: 20px;
}

.column-selection {
  margin-bottom: 20px;
}

.checkbox-container {
  display: inline-block;
  margin-right: 10px;
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 18px;
  text-align: left;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
}

.styled-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.styled-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.dropdown-menu-grid {
  width: 100%; /* 드롭다운 메뉴를 화면 너비에 맞게 조정 */
}

.dropdown-menu-grid .row {
  display: flex;
  flex-wrap: wrap;
}

.dropdown-menu-grid .col-6 {
  flex: 0 0 50%;
  max-width: 50%;
}

.dropdown-menu-grid .col-md-4 {
  flex: 0 0 33.3333%;
  max-width: 33.3333%;
}
</style>

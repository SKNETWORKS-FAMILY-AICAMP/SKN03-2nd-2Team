<template>
  <div class="container mt-4">
    <!-- 드롭다운 컨테이너 -->
    <div class="d-flex justify-content-between mb-3">
      <!-- 컬럼 선택 드롭다운 -->
      <div class="dropdown w-50 me-2">
        <button
          class="btn btn-secondary dropdown-toggle w-100"
          type="button"
          id="dropdownMenuButton"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          style="
            background-color: #ffc77d;
            border-color: #ffc77d;
            color: #4b2e2e;
            font-weight: bold;
          "
        >
          Select Columns
        </button>
        <ul class="dropdown-menu w-100" aria-labelledby="dropdownMenuButton">
          <li v-for="(header, index) in headers" :key="index" class="dropdown-item p-0">
            <label class="form-check-label w-100 p-2">
              <input
                type="checkbox"
                :value="header"
                v-model="selectedColumns"
                class="form-check-input"
              />
              {{ header }}
            </label>
          </li>
        </ul>
      </div>

      <!-- 장르 선택 드롭다운 -->
      <div class="dropdown w-50">
        <button
          class="btn btn-secondary dropdown-toggle w-100"
          type="button"
          id="genreDropdownButton"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          style="
            background-color: #ffc77d;
            border-color: #ffc77d;
            color: #4b2e2e;
            font-weight: bold;
          "
        >
          Filter by Genre
        </button>
        <ul class="dropdown-menu w-100" aria-labelledby="genreDropdownButton">
          <li v-for="(genre, index) in uniqueGenres" :key="index" class="dropdown-item">
            <a class="dropdown-item" href="#" @click="filterByGenre(genre)">{{ genre }}</a>
          </li>
        </ul>
      </div>
    </div>

    <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th v-for="header in selectedColumns" :key="header">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIndex) in filteredData" :key="rowIndex">
          <td v-for="header in selectedColumns" :key="header">
            {{ row[header] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import movieData from '@/assets/data/movies_2021_pages_1_to_20.json'

const headers = ref(Object.keys(movieData[0]))
const selectedColumns = ref(['영화명(국문)', '대표 장르'])
const data = ref(movieData)
const selectedGenre = ref(null)

const uniqueGenres = computed(() => {
  const genres = data.value.map((movie) => movie['대표 장르'])
  return [...new Set(genres)]
})

const filteredData = computed(() => {
  if (!selectedGenre.value) return data.value
  return data.value.filter((movie) => movie['대표 장르'] === selectedGenre.value)
})

const filterByGenre = (genre) => {
  selectedGenre.value = genre
}
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

.d-flex {
  display: flex;
  justify-content: space-between;
}

.me-2 {
  margin-right: 0.5rem;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 18px;
  text-align: left;
}

.table th,
.table td {
  padding: 12px 15px;
}

.table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
}

.table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.form-check-label {
  display: block;
  width: 100%;
  padding: 8px 15px;
}

.dropdown-menu {
  width: 100%;
}
</style>

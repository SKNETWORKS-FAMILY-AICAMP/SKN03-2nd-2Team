<template>
  <div class="container mt-4">
    <h1 class="text-center">Genre Table</h1>
    <!-- 컬럼 선택 드롭다운 -->
    <div class="dropdown mb-3">
      <button
        class="btn btn-secondary dropdown-toggle"
        type="button"
        id="dropdownMenuButton"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        Select Columns
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <li
          v-for="(header, index) in headers"
          :key="index"
          class="dropdown-item"
        >
          <label class="form-check-label">
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
    <div class="dropdown mb-3">
      <button
        class="btn btn-secondary dropdown-toggle"
        type="button"
        id="genreDropdownButton"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        Filter by Genre
      </button>
      <ul class="dropdown-menu" aria-labelledby="genreDropdownButton">
        <li
          v-for="(genre, index) in uniqueGenres"
          :key="index"
          class="dropdown-item"
        >
          <a class="dropdown-item" href="#" @click="filterByGenre(genre)">{{
            genre
          }}</a>
        </li>
      </ul>
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

<script>
import csvData from "@/assets/data/MovieList/movies_2019_pages_1_to_20.csv";

export default {
  data() {
    return {
      headers: [],
      rawData: [],
      filteredData: [],
      selectedColumns: ["영화명(국문)", "대표 장르"], // 기본적으로 선택된 컬럼
      uniqueGenres: [], // 고유한 장르 목록
      selectedGenre: null, // 선택된 장르
    };
  },
  mounted() {
    this.initializeData();
  },
  methods: {
    initializeData() {
      if (csvData.length > 1) {
        this.headers = csvData[0];
        this.rawData = csvData.slice(1).map((row) => {
          const rowData = {};
          this.headers.forEach((header, index) => {
            rowData[header] = row[index];
          });
          return rowData;
        });
        this.filteredData = this.rawData;

        // 고유한 장르 목록 설정
        const genresSet = new Set(this.rawData.map((row) => row["대표 장르"]));
        this.uniqueGenres = Array.from(genresSet);
      }
    },
    filterByGenre(genre) {
      this.selectedGenre = genre;
      this.filteredData = this.rawData.filter(
        (row) => row["대표 장르"] === genre
      );
    },
  },
};
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

.dropdown {
  margin-bottom: 20px;
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
</style>

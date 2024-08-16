<template>
  <div class="container mt-4">
    <!-- 기존 드롭박스 -->
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

    <!-- 새로운 드롭박스 -->
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
          <th>영화명(국문)</th>
          <th v-for="column in selectedColumns" :key="column">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIndex) in filteredRows" :key="rowIndex">
          <td>{{ row["영화명(국문)"] }}</td>
          <td v-for="column in selectedColumns" :key="column">
            {{ row[column] }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import csvFile from "@/components/MovieList/movies_2020_pages_1_to_20.csv";

export default {
  data() {
    return {
      headers: [],
      rows: [],
      selectedColumns: ["대표 장르"], // "대표 장르" 기본 선택
      uniqueGenres: [],
      filteredRows: [],
    };
  },
  mounted() {
    this.loadCSV();
  },
  methods: {
    loadCSV() {
      this.headers = Object.keys(csvFile[0]);
      this.rows = csvFile;
      this.filteredRows = this.rows;
      this.selectedColumns = ["대표 장르"]; // "대표 장르" 기본 선택

      // "대표 장르" 컬럼의 중복된 값을 제거하여 uniqueGenres 배열에 저장
      const genresSet = new Set(this.rows.map((row) => row["대표 장르"]));
      this.uniqueGenres = Array.from(genresSet);
    },
    filterByGenre(genre) {
      this.filteredRows = this.rows.filter((row) => row["대표 장르"] === genre);
    },
  },
};
</script>

<!-- src/components/MovieList.vue -->
<template>
    <div class="container mt-5">
      <h2>영화 목록</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>번호</th>
            <th>이름</th>
            <th>장르</th>
            <th>개봉일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="movie in movies" :key="movie.id">
            <td>{{ movie.id }}</td>
            <td>{{ movie.name }}</td>
            <td>{{ movie.genre }}</td>
            <td>{{ movie.releaseDate }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import { dummyData } from '@/assets/data/DummyData.js';

  export default {
    name: 'MovieList',
    data() {
      return {
        movies: dummyData
      };
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  
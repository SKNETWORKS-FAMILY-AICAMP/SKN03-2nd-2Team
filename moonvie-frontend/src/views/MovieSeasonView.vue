<script setup>
import MovieCard from '@/components/MovieCard.vue'
import MovieSeason from '@/components/MovieSeason.vue'

import { useTopMovieStore } from '@/stores/topMovieStore'
import { storeToRefs } from 'pinia'

const topMovieStore = useTopMovieStore()
const { topMovies } = storeToRefs(topMovieStore)
</script>
<template>
  <article class="p-8 lg:p-16">
    <h1 class="text-4xl font-bold text-white">시즌별 인기 영화</h1>
    <MovieSeason />
    <figure class="grid grid-cols-1 gap-4 lg:grid-cols-2 xl:grid-cols-4">
      <template v-for="(movie, idx) in topMovies" :key="movie">
        <MovieCard :movieName="movie" :idx="idx + 1" />
      </template>
    </figure>
  </article>
</template>

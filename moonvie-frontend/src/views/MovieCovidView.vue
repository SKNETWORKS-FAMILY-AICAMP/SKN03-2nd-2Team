<script setup>
import MovieCovidTabs from '../components/MovieCovidTabs.vue'
import MovieCovidMoney from '@/components/MovieCovidMoney.vue'
import MovieCovidPeople from '@/components/MovieCovidPeople.vue'
import { useMovieStore } from '@/stores/movieStore'
import { storeToRefs } from 'pinia'
const movieStore = useMovieStore()
const { currentCovidTab } = storeToRefs(movieStore)
</script>
<template>
  <article class="p-8 lg:p-16">
    <MovieCovidTabs />
    <template v-if="currentCovidTab === 0">
      <MovieCovidMoney />
    </template>
    <template v-else-if="currentCovidTab === 1">
      <MovieCovidPeople />
    </template>
  </article>
</template>

<script setup>
import GenreTabs from '@/components/GenreTabs.vue'
import GenreSeason from '@/components/GenreSeason.vue'
import GenreHoliday from '@/components/GenreHoliday.vue'
import GenreCovid from '@/components/GenreCovid.vue'
import { useMovieStore } from '@/stores/movieStore'
import { storeToRefs } from 'pinia'
const movieStore = useMovieStore()
const { currentTab } = storeToRefs(movieStore)
</script>
<template>
  <article class="p-8 lg:p-16">
    <GenreTabs />
    <template v-if="currentTab === 0">
      <GenreSeason />
    </template>
    <template v-else-if="currentTab === 1">
      <GenreHoliday />
    </template>
    <template v-else-if="currentTab === 2">
      <GenreCovid />
    </template>
  </article>
</template>

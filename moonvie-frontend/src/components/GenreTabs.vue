<script setup>
import { storeToRefs } from 'pinia'
import { useMovieStore } from '@/stores/movieStore'
import { useRouter } from 'vue-router'
const router = useRouter()
const movieStore = useMovieStore()
const { genreTabs } = storeToRefs(movieStore)
const handleTabClick = (itemName) => {
  movieStore.setTabCurrent(itemName)
  router.go()
}
</script>

<template>
  <nav class="flex border-b border-white/10 py-4 mb-8">
    <div
      class="flex min-w-full flex-none gap-x-6 px-2 text-sm font-semibold leading-6 text-gray-400"
    >
      <template v-for="tab in genreTabs" :key="tab.name">
        <a
          :class="[
            tab.current
              ? ' text-moonYellow border-b-2 border-moonYellow'
              : 'text-gray-300 hover:text-white hover:border-b-2 hover:border-moonYellow/10',
            'rounded-md px-3 py-2 text-sm font-medium'
          ]"
          @click="handleTabClick(tab.name)"
          >{{ tab.name }}</a
        >
      </template>
    </div>
  </nav>
</template>

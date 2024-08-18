<script setup>
import { storeToRefs } from 'pinia'
import { useTopMovieStore } from '@/stores/topMovieStore'

const topMovieStore = useTopMovieStore()
const { movieInfo } = storeToRefs(topMovieStore)
</script>
<template>
  <div class="overflow-hidden rounded-lg bg-gray-700 shadow">
    <div class="text-moonYellow text-4xl font-bold px-4 pt-9 sm:px-6">
      #{{ $attrs.idx }} {{ $attrs.movieName }}
    </div>
    <div class="bg-gray-700 px-4 py-5 sm:p-6">
      <div class="mx-auto max-w-7xl">
        <div class="grid grid-cols-1 gap-px sm:grid-cols-2">
          <template v-for="info in movieInfo" :key="info.name">
            <div class="bg-gray-700 mb-4">
              <p class="text-sm font-medium leading-6 text-gray-400">{{ info.name }}</p>
              <p class="mt-2 flex items-baseline gap-x-2">
                <span class="text-2xl font-semibold tracking-tight text-white">
                  {{ info.value }}
                </span>
                <span class="text-sm text-gray-400">{{ info.subName }}</span>
              </p>
            </div>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useTopMovieStore } from '@/stores/topMovieStore'
import { storeToRefs } from 'pinia'

const topMovieStore = useTopMovieStore()
const { startDate, endDate, maxDate, error } = storeToRefs(topMovieStore)

onMounted(() => {
  const now = new Date()
  maxDate.value = now.getFullYear() * 100 + (now.getMonth() + 1)
})
</script>
<template>
  <div class="mx-auto py-4">
    <div class="mb-8 pb-4 border-b-2 border-white/10">
      <div class="flex items-center mb-2">
        <input
          v-model="startDate"
          @input="limitInput(startDate)"
          type="text"
          placeholder="시작년월 (YYYYMM)"
          class="mr-2 p-2 bg-gray-800 text-white rounded w-60"
          maxlength="6"
        />
        <input
          v-model="endDate"
          @input="limitInput(endDate)"
          type="text"
          placeholder="종료년월 (YYYYMM)"
          class="mr-2 p-2 bg-gray-800 text-white rounded w-60"
          maxlength="6"
        />
        <button
          @click="validateDates"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          조회
        </button>
      </div>
      <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<template>
  <div>
    <PeriodTable v-if="isTable" />
    <PeriodChart v-else />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import PeriodTable from '@/components/PeriodTable.vue'
import PeriodChart from '@/components/PeriodChart.vue'

const store = useCounterStore()
const isTable = computed(() => store.viewMode === 'table')
</script>

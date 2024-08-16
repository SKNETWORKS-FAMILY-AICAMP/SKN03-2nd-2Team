<template>
  <div class="layout">
    <MoonvieHeader />
    <main class="content">
      <router-view />
    </main>
    <MoonvieFooter />
  </div>
</template>

<script setup>
import MoonvieHeader from '@/components/MoonvieHeader.vue'
import MoonvieFooter from '@/components/MoonvieFooter.vue'
</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #919191;
}
.content {
  flex: 1;
}
</style>

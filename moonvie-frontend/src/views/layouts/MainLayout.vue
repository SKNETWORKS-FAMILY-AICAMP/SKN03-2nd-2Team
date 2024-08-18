<script setup>
// import { ref } from 'vue'
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'
</script>

<template>
  <div>
    <header>
      <TheHeader />
    </header>
    <main>
      <RouterView />
    </main>
    <footer>
      <TheFooter />
    </footer>
  </div>
</template>
<style scoped></style>

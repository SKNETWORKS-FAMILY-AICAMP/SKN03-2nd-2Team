<<<<<<< HEAD
<template>
  <mainLayout />
</template>

<script setup>
import MainLayout from './views/Layouts/MainLayout.vue'
</script>

<style>
body {
  background-color: #919191;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

router-view {
  flex: 1;
}
</style>
=======
<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style scoped></style>
>>>>>>> origin/hotfix

<template>
    <div>
      <MoonvieHeader />
      <main>
        <router-view />
      </main>
      <MoonvieFooter />
    </div>
  </template>
  
  <script>
  import MoonvieHeader from './MoonvieHeader.vue';
  import MoonvieFooter from './MoonvieFooter.vue';
  
  export default {
    name: 'MainLayout',
    components: {
        MoonvieHeader,
        MoonvieFooter
    }
  };
  </script>
  
  <style scoped>
  /* MainLayout styles */
  </style>

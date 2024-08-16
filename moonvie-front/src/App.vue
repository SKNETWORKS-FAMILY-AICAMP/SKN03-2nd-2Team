<template>
  <div id="app">
    <mainLayout />
  </div>
</template>

<script>
import MainLayout from './components/Layout/MainLayout.vue';

export default {
  name: 'App',
  components: {
    MainLayout
  }
};
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

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

router-view {
  flex: 1;
}
</style>

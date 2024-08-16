<template>
  <div>
    <WeeklyData />
    <MoonvieFooter />
  </div>
</template>

<script>
import WeeklyData from '../components/WeeklyData';

export default {
  name: 'MoonvieMonth',
  components: {
    WeeklyData
  }
};
</script>

<style scoped>
body {
  background-color: #919191;
}
.container {
  flex: 1;
}
</style>

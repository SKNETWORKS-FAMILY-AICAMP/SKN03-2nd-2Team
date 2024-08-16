<template>
  <div>
    <MovieList />
    <MoonvieFooter />
  </div>
</template>

<script>
import MovieList from '../components/MovieList';

export default {
  name: 'MoonvieMonth',
  components: {
    MovieList
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
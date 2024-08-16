<template>
  <div>
    <GenreTable />
    <MoonvieFooter />
  </div>
</template>

<script>
import GenreTable from '../components/GenreTable';

export default {
  name: 'MoonvieMonth',
  components: {
    GenreTable
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
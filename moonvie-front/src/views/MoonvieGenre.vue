<template>
  <div>
    <GenreTable />
  </div>
</template>

<script>
import GenreTable from "@/components/GenreTable.vue";

export default {
  name: "MoonvieGenre",
  components: {
    GenreTable,
  },
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

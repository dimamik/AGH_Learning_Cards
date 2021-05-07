<template>
  <div class="HomeComponent">
    There should be list of cards and some greeting
    <CardsListComponent></CardsListComponent>
  </div>
</template>

<script>

import CardsListComponent from "@/components/CollectionsListComponent";

export default {
  name: "HomeComponent",
  components: {
    CardsListComponent
  }
}
</script>

<style scoped>

</style>
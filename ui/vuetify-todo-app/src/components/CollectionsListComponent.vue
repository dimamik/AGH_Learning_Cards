<template>
  <div>
    <row :gutter="12" class="ma-auto"
    >
      <column v-for="card in cards" :key="card.id" :lg="3" :md="4" :xs="12" class="pa-2 pr-3">
        <SingleCollectionComponent class="inline-block"
                                   v-bind:card="card"
        ></SingleCollectionComponent>
      </column>
    </row>
  </div>
</template>
<script>
import SingleCollectionComponent from "@/components/SingleCollectionComponent";
import {Column, Row} from 'vue-grid-responsive';

export default {
  // TODO Add binding property cards (which are collections btw)
  name: "CollectionsListComponent",
  components: {
    SingleCollectionComponent,
    Row,
    Column
  },
  data() {
    return {
      cards: [{
        id: 1,
        title: "Title: Math Formulas!",
        frontSide: "Example math formula: l = 2 pi r",
        author: "Some Author: sad2020"

      }, {
        id: 2,
        title: "Title: Math Formulas!",
        frontSide: "Example math formula: l = 2 pi r",
        author: "Some Author: sad2020"

      }, {
        id: 3,
        title: "Title: Math Formulas!",
        frontSide: "Example math formula: l = 2 pi r",
        author: "Some Author: sad2020"

      }, {
        id: 4,
        title: "Title: Math Formulas!",
        frontSide: "Example math formula: l = 2 pi r",
        author: "Some Author: sad2020"

      },]

    }
  }
}
</script>

<style scoped>

</style>
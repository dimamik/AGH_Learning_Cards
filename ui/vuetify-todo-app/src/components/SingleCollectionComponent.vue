<template>
  <FlipCard
  >
    <template slot="front" class="red"
    >
      <b> {{ card.title }}</b> <br>
      <span>{{ card.frontSide }}</span>
    </template>
    <template slot="back">
      <b>{{ card.author }}</b>
      <v-layout align-content-end fill-height justify-center>
        <v-card-actions>
          <v-btn
              color="primary"
              v-bind:to="'learn-collection'"
          >
            Learn
          </v-btn>
        </v-card-actions>
      </v-layout>
    </template>
  </FlipCard>
</template>

<script>
import FlipCard from "@/components/FlipCard";

export default {
  name: "SingleCollectionComponent",
  props: ['card'],
  components: {
    FlipCard
  }
};
</script>

<style>
.front {
  background-color: #00c853;
}

.back {
  background-color: #00b8d4;
}

.back,
.front {
  /*TODO Play with sizes*/
  height: 150px;
}

</style>

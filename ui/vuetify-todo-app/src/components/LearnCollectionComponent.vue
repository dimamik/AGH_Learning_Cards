<template>
  <div>

    <FlipCard
    >
      <template slot="front" class="red"
      >
        <span>{{ card.frontSide }}</span>
      </template>
      <template slot="back">
        <b>{{ card.backSide }}</b>

      </template>
    </FlipCard>
  </div>
</template>

<script>
import FlipCard from "@/components/FlipCard";

export default {
  name: "LearnCollectionComponent",
  components: {
    FlipCard
  },
  data() {
    return {
      card: {
        frontSide: "Word to learn",
        backSide: "Definition"
      }
    }
  }
}
</script>


<style scoped>
/*TODO Make scoped working and change propagation*/
.front {
  background-color: #00c853;
}

.back {
  background-color: #00b8d4;
}

.back,
.front {
  /*TODO Play with sizes*/
  height: 250px;

  /*TODO Play with with and parent props to make it work*/
  width: 15vh;
}

</style>
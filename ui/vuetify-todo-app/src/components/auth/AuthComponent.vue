<template>
  <v-container>
    <v-row justify="center" class="header">
      <h2>Sign in or sign up</h2>
    </v-row>
    <v-row justify="space-around">
      <v-col md="5">
        <SignInComponent></SignInComponent>
      </v-col>
      <v-col md="5">
        <SignUpComponent></SignUpComponent>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SignInComponent from "./SignInComponent";
import SignUpComponent from "./SignUpComponent";

export default {
  name: "AuthComponent",
  components: {SignInComponent, SignUpComponent}
}
</script>

<style scoped>
  .header {
    margin: 2em 0;
  }
</style>
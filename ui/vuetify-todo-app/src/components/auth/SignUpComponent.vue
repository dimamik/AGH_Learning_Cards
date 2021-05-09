<template>
  <v-card dark class="form-card">
    <v-card-title>Sign up</v-card-title>
    <v-form @submit="signUp">
      <v-text-field
          type="text"
          label="username"
          outlined
          v-model="username"
          :rules="AuthService.usernameRules"
      ></v-text-field>
      <v-text-field
          type="email"
          label="email"
          outlined
          v-model="email"
          :rules="AuthService.emailRules"
      ></v-text-field>
      <v-text-field
          type="password"
          label="password"
          outlined
          v-model="password"
          :rules="AuthService.passwordRules"
      ></v-text-field>
      <v-card-actions>
        <v-btn type="submit" depressed color="primary">Sign up</v-btn>
      </v-card-actions>
    </v-form>
    <v-alert
        v-if="error"
        type="error"
    >
      {{ error }}
    </v-alert>
  </v-card>
</template>

<script>
import AuthService from "../../services/AuthService";
import router from "../../router";

export default {
  name: "SignUpComponent",
  data() {
    return {
      AuthService,
      username: '',
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    signUp(e) {
      e.preventDefault();
      AuthService.signUp(this.username, this.email, this.password)
          .then(() => router.push("my-cards"))
          .catch(e => this.error = e.response.data.message);
    }
  }
}
</script>

<style scoped>
.form-card {
  padding: 1em;
}
</style>
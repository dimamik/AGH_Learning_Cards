<template>
  <div>
    <v-navigation-drawer
        v-model=drawer
        app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Learning Cards App
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>
      <v-list
          dense
          nav
      >
        <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            v-bind:to="item.route"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item
            v-if="AuthService.current"
            link
            @click="signOut"
        >
          <v-list-item-icon>
            <v-icon>mdi-logout</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Sign out</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
            v-else link
            to="auth"
            key="Sign out"
        >
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>Authenticate</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Learning Cards</v-toolbar-title>
    </v-app-bar>

  </div>

</template>

<script>
import AuthService from "../services/AuthService";
import router from "../router";

export default {
  name: "NavigationBar",
  data: () => ({
    AuthService,
    drawer: null,
    items: [
      {title: 'Home', icon: 'mdi-home-search', route: 'home'},
      {title: 'My Collections', icon: 'mdi-cards', route: 'my-cards'},
      {title: 'Learn Collection', icon: 'mdi-school', route: 'learn-collection'},
      {title: 'Profile', icon: 'mdi-account', route: 'profile'}
    ],
    right: null
  }),
  methods: {
    signOut() {
      AuthService.signOut()
        .then(() => {
            if (router.currentRoute.name !== 'home') {
                router.push("home")
            }
        });
    }
  }
}
</script>

<style scoped>

</style>
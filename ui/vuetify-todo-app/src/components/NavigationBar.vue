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
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Learning Cards</v-toolbar-title>
    </v-app-bar>

  </div>

</template>

<script>
export default {
  name: "NavigationBar",
  data: () => ({
    drawer: null,
    items: [
      {title: 'Home', icon: 'mdi-home-search', route: 'home'},
      {title: 'My Collections', icon: 'mdi-cards', route: 'my-cards'},
      {title: 'Learn Collection', icon: 'mdi-school', route: 'learn-collection'},
      {title: 'Profile', icon: 'mdi-account', route: 'profile'},
    ],
    right: null
  }),
}
</script>

<style scoped>

</style>
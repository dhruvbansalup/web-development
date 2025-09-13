<template>
  <router-link to="/child">child</router-link>
  <router-view></router-view>
  <dynamicComponent />
</template>

<script>
import dynamicComponent from './components/dynamicComponent.vue'

export default {
  name: 'App',
  components: {
    dynamicComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<template>
  <div id="app">
    <NavbarSection />
    <router-view></router-view> 
  </div>
</template>

<script>
import NavbarSection from './components/NavbarSection.vue';


export default {
  name: 'App',
  components: {
    NavbarSection,
  },
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

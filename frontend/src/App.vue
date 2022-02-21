<script>
import Sidebar from "@/components/sidebar/Sidebar";
import { sidebarWidth } from "@/components/sidebar/state";
export default {
  components: { Sidebar },
  setup() {
    return { sidebarWidth };
  },
};
</script>
<template>
  <Sidebar />
  <div :style="{ 'margin-left': sidebarWidth }">
    <router-view />
  </div>
</template>

<style>
html,
body {
  background-image: url("./assets/wallpaperflare.com_wallpaper.jpg");
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

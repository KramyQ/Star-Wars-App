<template>
  <div
    class="InformantSection"
    :style="{
      backgroundImage: `url('../assets/wallpaperflare.com_wallpaper.jpg')`,
    }"
  >
    <oddsContainer msg="tqt"></oddsContainer>
  </div>
</template>

<script>
// @ is an alias to /src
import oddsContainer from "@/components/oddsPrediction/oddsContainer.vue";

export default {
  name: "InformantSection",
  components: {
    oddsContainer,
  },
};
</script>

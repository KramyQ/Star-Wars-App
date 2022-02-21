<template>
  <div class="oddsDisplay">
    <label class="Text" v-if="successRate.status">
      Here are the success chances for the given information :</label
    >
    <p class="display Text" id="successValue" v-if="successRate.status">
      {{ successRate.value }} %
    </p>
  </div>
</template>

<script>
export default {
  name: "oddsDisplay",
  props: {
    successRate: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.Text {
  font-family: "Comfortaa", cursive;
  color: #ffffff;
  font-size: 20px;
  font-weight: 200;
  line-height: 30px;
  margin: 0 0 10px;
  text-align: center;
}
</style>

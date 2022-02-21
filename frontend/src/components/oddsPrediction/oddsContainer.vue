<template>
  <div class="oddsContainer center">
    <odds-display data-testid="oddsDisplay" :success-rate="successRate"></odds-display>
    <br />
    <oddsUploadInterface data-testid="oddsUploadInterface"
      v-if="!successRate.status"
      @send-rebel-info="sendRebelInfo"
    ></oddsUploadInterface>
  </div>
  <button @click="successRate.status = false" class="center2">
    <i class="fa-solid fa-arrow-rotate-right white-arrow"></i>
  </button>
</template>

<script>
import oddsDisplay from "./oddsDisplay.vue";
import oddsUploadInterface from "./oddsUploadInterface.vue";
import {getOdds} from "@/services/OddPredictionService";

export default {
  name: "oddsContainer",
  components: { oddsDisplay, oddsUploadInterface },
  data() {
    return {
      successRate: {
        value: 0,
        status: false,
      },
    };
  },
  methods: {
    sendRebelInfo({ file }) {
      getOdds(file)
        .then((response) => {
          this.successRate.value = response.data;
          this.successRate.status = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.white-arrow {
  font-size: 2em;
  color: white;
}

.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.center2 {
  margin: 0;
  position: absolute;
  top: 65%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.oddsContainer {
  height: 150px;
  width: 400px;
  border-radius: 10px;
  background: rgba(76, 71, 71, 0.73);
  box-shadow: 0 20px 50px rgba(246, 63, 42, 0.7);
}

button {
  width: 150px;
  height: 50px;
  cursor: pointer;
  border: none;
  font-family: "Comfortaa", cursive;
  color: rgba(255, 255, 255, 0.5);
  font-size: 20px;
  border-radius: 4px;
  box-shadow: inset 0px 3px 5px rgba(255, 255, 255, 0.5),
    0px 0px 10px rgba(0, 0, 0, 0.15);
  background: rgb(2, 0, 36);
  background: linear-gradient(
    45deg,
    rgba(2, 0, 36, 0) 5%,
    rgba(255, 255, 255, 0.5) 6%,
    rgba(255, 255, 255, 0) 9%,
    rgba(255, 255, 255, 0.5) 10%,
    rgba(255, 255, 255, 0) 17%,
    rgba(255, 255, 255, 0.5) 19%,
    rgba(255, 255, 255, 0) 21%
  );
  background-size: 150%;
  background-position: right;
  transition: 1s;
}

button:hover {
  background-position: left;
  color: white;
  box-shadow: inset 0px 3px 5px rgba(255, 255, 255, 1),
    0px 0px 10px rgba(0, 0, 0, 0.25);
}

button:focus {
  outline: none;
}
</style>

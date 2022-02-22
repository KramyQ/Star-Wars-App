<template>
  <div class="container">
    <div class="oddsModalContent" id="oddsModalContent">
      <p id="message-display">{{message}}</p>
      <button class="button"  @click="$emit('close-modal')">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: String,
  }
}
</script>

<style scoped>
body {
  font-family: "Roboto", sans-serif;
  padding: 0;
  margin: 0;
  background: rgba(76, 71, 71, 0.73);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
}



.oddsModalContent {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  width: 320px;
  height: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(71, 76, 74, 0.94);
  color: #ffffff;
  text-align: center;
  border-radius: 20px;
  padding: 30px 30px 70px;
}
.button {
  background: #72271e;
  border: 1px solid #3d3a3a;
  border-radius: 6px;
  box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: nunito,roboto,proxima-nova,"proxima nova",sans-serif;
  font-size: 16px;
  font-weight: 800;
  line-height: 16px;
  min-height: 40px;
  outline: 0;
  padding: 12px 14px;
  text-align: center;
  text-rendering: geometricprecision;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
}

.button:hover{
  background: #a83426;
}
.button:active {
  background-color: initial;
  background-position: 0 0;
  color: #8e100c;
}

.button:active {
  opacity: .5;
}

</style>

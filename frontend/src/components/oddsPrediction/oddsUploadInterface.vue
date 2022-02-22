<template>
  <odds-modal
    v-if="oddsModal"
    @close-modal="closeModal"
    :message="this.oddsModalMessage"
  >
  </odds-modal>
  <div v-else>
    <label class="Text"> Please import your information </label>
    <br />
    <br />
    <input
      id="fileUpload"
      type="file"
      accept="application/json"
      @change="handleFileUpload($event)"
      hidden
    />
    <button @click="chooseFiles()">Upload</button>
    <button @click="submitFile()">Send</button>
  </div>
</template>

<script>
import OddsModal from "@/components/oddsPrediction/oddsModal";
import { readFileAsText, validateEmpireJson } from "@/services/dataValidation";

export default {
  name: "oddsUploadInterface",
  components: { OddsModal },
  data() {
    return {
      file: "",
      oddsModal: false,
      oddsModalMessage: "",
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    chooseFiles: function () {
      document.getElementById("fileUpload").click();
    },
    submitFile() {
      if (this.file != "") {
        readFileAsText(this.file).then((textFile) => {
          if (validateEmpireJson(textFile)) {
            this.$emit("send-rebel-info", { file: this.file });
          } else {
            this.oddsModal = true;
            this.oddsModalMessage =
              "Please import a file with the right format.";
          }
        });
      } else {
        this.oddsModal = true;
        this.oddsModalMessage = "Please import a file.";
      }
    },
    closeModal() {
      this.oddsModal = false;
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

button {
  margin: 5px;
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

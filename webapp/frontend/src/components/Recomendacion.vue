<template>
  <div class="recommendation-body" id="main-row">
    <div class="row">
      <v-col cols="12" md="6">
        <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
        <div style="">
          <v-card :loading="loading" class="left" style="display: flow-root">
            <template slot="progress" id="loading">
              <v-progress-linear
                color="var(--main-green)"
                height="6"
                indeterminate
              ></v-progress-linear>
            </template>
            <v-row id="title-row">
              <v-col cols="12" md="3">
                <img height="160px" :src="apiin" />
              </v-col>
              <v-col cols="12" md="7"  style="margin: auto">
                <h4 class="headline mb-2">Tu plan de alimentación de hoy</h4>
              </v-col>
              <v-col cols="12" md="2"  style="margin: auto">
                <v-icon class="reload" size="30px" @click="reload">
                  mdi-cached
                </v-icon>
              </v-col>
            </v-row>

            <div class="overline text-left" style="margin: 35px">
              <v-row>
                <v-col md="4">
                  <div @mouseover="active = true" @mouseleave="active = false">
                    <v-icon size="40px"> mdi-cup </v-icon>
                    {{ waterGlasses }}
                  </div>
                </v-col>
                <v-col md="6">
                  <div v-show="active" class="dialog text-center">
                    <div>¡Hidratarse es importante!</div>
                    Deberías beber
                    {{ this.$store.getters.waterIntake.toFixed(0) }} ml de agua
                    al día
                  </div>
                </v-col>
              </v-row>
            </div>

            <div v-for="(comida, index) in comidas" :key="index">
              <div
                class="d-flex flex-no-wrap justify-space-between"
                :key="recom_key"
              >
                <v-list-item three-line>
                  <v-list-item-content>
                    <div class="overline text-left" style="margin-left: 20px">
                      {{ comida }}
                    </div>
                    <div
                      v-for="(r, index) in rec"
                      :key="index"
                      class="recipe-card-div"
                    >
                      <v-list-item
                        v-if="r.Comida == comida"
                        class="receta"
                        @mouseover="displayOptions = index"
                        @mouseout="displayOptions = null"
                      >
                        <v-overlay :z-index="zIndex" :value="overlay === index">
                          <div class="recipe-info-card">
                            <recipe-info
                              :recipe="r"
                              :default_icon="default_icon"
                            ></recipe-info>
                            <div class="close-icon">
                              <v-icon
                                class="white--text"
                                size="30px"
                                color="orange"
                                @click="exitOverlay()"
                              >
                                mdi-close
                              </v-icon>
                            </div>
                          </div>
                        </v-overlay>
                        <v-list class="info_receta">
                          <v-list-item-title class="body-1">
                            <div class="text-left font-weight-bold">
                              {{ r.Nombre }}
                            </div>
                          </v-list-item-title>
                          <v-list-item-subtitle>
                            <p class="text-left caption">
                              {{ r.energia.toFixed(1) }} kcal
                            </p>
                          </v-list-item-subtitle>
                        </v-list>

                        <v-divider></v-divider>

                        <v-icon
                          size="25px"
                          class="option-icon"
                          v-show="displayOptions === index"
                          @click="displayInfo(index, r)"
                        >
                          mdi-information-outline
                        </v-icon>
                        <v-icon
                          size="25px"
                          class="option-icon"
                          v-show="displayOptions === index"
                          :class="{ reroll: animated }"
                          @animationend="animated = false"
                          @click="reroll(index)"
                        >
                          mdi-rotate-right
                        </v-icon>

                        <v-list-item-avatar size="60" color="#FAD7A0" rounded>
                          <img
                            v-if="r.image_src !== 'None'"
                            :src="getImageSrc(index)"
                          />
                          <v-icon size="35" v-else>
                            {{ default_icon[comida] }}
                          </v-icon>
                        </v-list-item-avatar>
                      </v-list-item>
                    </div>
                  </v-list-item-content>
                </v-list-item>
              </div>
            </div>
          </v-card>
        </div>

        <v-card class="left" style="margin-top:2rem;">
        <v-container>
          <v-form ref="form" v-model="valid" lazy-validation class="formulario">
            <h3>¡Prueba a cambiar tus atributos!</h3>
            <v-card-text>
              <v-slider
                v-model="weight.val"
                step="1"
                color="var(--main-orange)"
                track-color="var(--main-orange-pale)"
                thumb-label
                min="40"
                max="150"
                label="PESO"
                value="1"
                ticks
              ></v-slider>
            </v-card-text>

            <v-select
              v-model="selected_activity"
              :items="activity_types"
              label="Actividad física"
              solo
            ></v-select>

            <v-card-text>
              <v-slider
                v-model="height.val"
                step="1"
                color="var(--main-orange)"
                track-color="var(--main-orange-pale)"
                min="130"
                max="220"
                label="ALTURA"
                thumb-label
                ticks
              ></v-slider>
            </v-card-text>

            <v-select
              v-model="objetivo"
              :items="objectives"
              label="Objetivo nutricional"
              solo
            ></v-select>

            <v-card-text>
              <v-slider
                v-model="alpha"
                step="0.01"
                min="0"
                max="1"
                color="var(--main-orange)"
                track-color="var(--main-orange-pale)"
                label="VALOR NUTRICIONAL - GUSTOS"
                thumb-label
                ticks
              ></v-slider>
            </v-card-text>

            <div class="buttonHolder">
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"

                @click="createUser"
              >
                GENERAR PLAN
              </v-btn>
            </div>
          </v-form>
        </v-container>
      </v-card>
      </v-col>
      <v-col cols="12" md="6" class="stats">
        <!-- COL 2: STATS de las comidas + EXPLICACIÓN-->

        <div class="infos">
          <user-card></user-card>
        </div>

        <div class="infos">
          <nutritional-info
            :recipes="rec"
            ref="nutritionalInfoChild"
          ></nutritional-info>
        </div>

        <div class="infos">
          <explanation-card></explanation-card>
        </div>
      </v-col>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ExplanationCard from "./recom-plan/ExplanationCard.vue";
import UserCard from "./recom-plan/UserCard.vue";
import NutritionalInfo from "./recom-plan/NutritionalInfo";
import DoughnutChart from "./graphs/DoughnutChart.vue";
import BarChart from "./graphs/BarChart.vue";
import RecipeInfo from "./recom-plan/RecipeInfo.vue";

export default {
  name: "Recomendacion",
  components: {
    "doughnut-chart": DoughnutChart,
    "explanation-card": ExplanationCard,
    "recipe-info": RecipeInfo,
    "nutritional-info": NutritionalInfo,
    "user-card": UserCard,
    "bar-chart": BarChart,
  },
  data() {
    NutritionalInfo;
    return {
      rec: [], // recommendation full json
      active: false,
      zIndex: 1,
      recom_key: 0,
      comidas: ["desayuno", "snack", "comida", "merienda", "cena"],
      default_icon: {
        desayuno: "mdi-food-variant",
        snack: "mdi-food-apple",
        comida: "mdi-pasta",
        merienda: "mdi-food-croissant",
        cena: "mdi-noodles",
      },
      objectives: ["Perder peso", "Mantener", "Ganar peso"],
      activity_types: [
        "1. Sedentario (nada de ejercicio / trabajo de oficina)",
        "2. Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
        "3. Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
        "4. Muy activo (ejercicio casi diario intenso)",
        "5. Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)",
      ],
      height: {
        label: "Altura (cm)",
        val: this.$store.getters.height,
        color: "red",
      },
      weight: {
        label: "Peso (kg)",
        val: this.$store.getters.weight,
        color: "blue",
      },
      body_type: "default",
      ingredients: ["empty"],
      age: "",
      selected_activity: this.$store.getters.nivel_actividad,
      objetivo: this.$store.getters.objective,
      alpha: "0.70",
      selected_sex: "",
      apiin: require("../assets/apiín.png"),
      loading: true,
      displayOptions: null,
      overlay: -1,
      animated: false,
    };
  },

  computed: {
    waterGlasses() {
      return Math.ceil(this.$store.getters.waterIntake / 250);
    },
  },
  watch: {
    rec: function (newVal, oldVal) {
      // watch it
      this.rec = newVal;
    },
  },
  methods: {
    getRecomendacion(lab) {
      const path = "http://localhost:5000/recomendacion";

      if (lab) {
        var targetUser = {
          username: this.$store.getters.username.concat("", "_lab"),
        };
      } else {
        var targetUser = {
          username: this.$store.getters.username,
        };
      }
      axios
        .post(path, targetUser)
        .then((res) => {
          this.rec = res.data;
          this.loading = false;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    createUser() {
        
        var new_user = {
        username:this.$store.getters.username,
        weight: this.weight.val,
        height: this.height.val,
        alpha: this.alpha,
        activity_level: this.activity_types.indexOf(this.selected_activity) + 1,
        objective: this.objectives.indexOf(this.objetivo),
      };

      axios({
        baseURL: "http://localhost:5000",
        url: "/newUserLab",
        method: "post",
        data: new_user,
      })
        .then((res) => {
          console.log(res.data);
          this.getRecomendacion(true)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    reroll(index) {
      const path = "http://localhost:5000/reroll";
      var reroll_params = {
        username: this.$store.getters.username,
        recipe_id: this.rec[index]["Recipe_id"],
        food_type: this.rec[index]["Comida"],
      };
      this.animated = true;
      axios
        .post(path, reroll_params)
        .then((res) => {
          var new_rec = res.data[0];
          this.animated = false;
          this.$set(this.rec, index, new_rec);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    reload() {
      this.loading = true;
      this.getRecomendacion(0);
    },
    displayInfo(index, recipe) {
      this.overlay = index;
    },
    exitOverlay() {
      this.overlay = -1;
      this.displayOptions = null;
    },
    getImageSrc(index) {
      return this.rec[index].image_src;
    },
    mouseOver: function () {
      this.active = !this.active;
    },
  },
  created() {
    this.getRecomendacion(0);
  },
};
</script>

<style scoped lang="scss">
#main-row {
  padding-top: 60px;
}

.recipe-card-div {
  margin-bottom: -10px;
}

.buttonHolder {
  text-align: center;
}

.formulario {
  font-family: "Cairo", sans-serif;
  margin-top: 1cm;
  background-color: white;
  margin: auto;
  width: 95%;
  padding: 30px;
  justify-content: flex-end;
  text-align: left;
  line-height: 50px;
}

.infos {
  margin: auto;
  width: 90%;
}

.option-icon {
  margin-left: 10px;
  color: var(--main-green);
}

.stats {
  
}

.dialog {
  margin: auto;
  position: absolute;
  width: 400px;
  border-radius: 10px;
  background-color: rgb(197, 236, 182);
}

.left {
  margin-left: 2rem;
  padding-bottom: 1rem;
}

#randomrow {
  margin: 0;
}

.reroll {
  animation-name: spin;
  animation-duration: 800ms;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
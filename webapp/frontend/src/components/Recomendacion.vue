<template>
  <div class="recommendation-body">
    <v-row id="title-row">
        <v-col cols="12" md="9">
            <h3 class="headline mb-2"> Plan de Alimentación de Hoy para {{this.$store.getters.username}} </h3>
        </v-col>
        <v-col cols="12" md="1">
            <v-icon class="reload"
            @click="reload">
            mdi-cached
            </v-icon>
        </v-col>
    </v-row>
    <v-row>
    <v-col cols="12" md="7" style="margin-left:40px">
    <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
        <v-container>
        <v-card
        class="mx-auto"
        max-width="700"
        outlined
        v-for="(comida, index) in comidas"
        :key="index"
        >  
        <div class="d-flex flex-no-wrap justify-space-between" :key="recom_key">
        <v-list-item three-line
        >
            <v-list-item-content>
            <div class="overline">
                {{ comida }}
            </div>
            <div v-for="(r, index) in rec"
                :key="index"
            >   
                <v-list-item 
                    v-if="r.Comida==comida" 
                    class="receta"
                    @click="displayInfo(index,r)"
                >
                <v-overlay
                :z-index="zIndex"
                :value="r.overlay"
                >
                <div class="recipe-info-card">
                    <recipe-info :recipe="r" :default_icon="default_icon"></recipe-info>
                    <div class="close-icon">
                        <v-icon
                            class="white--text"
                            size="30px"
                            color="orange"
                            @click="exitOverlay(index)"
                        >
                            mdi-close 
                        </v-icon>
                    </div>
                </div>
                </v-overlay>
                    <v-list class="info_receta">
                        <v-list-item-title class="body-1" >
                        <p class="text-left font-weight-bold">
                                {{ r.Nombre }} {{ r.overlay }}
                            </p> 
                        </v-list-item-title>
                        <v-list-item-subtitle> 
                            <p class="text-left caption">
                                {{ r.energia.toFixed(1) }} kcal
                            </p> 
                        </v-list-item-subtitle>
                    </v-list>
                    <v-divider></v-divider>
                    <v-list-item-avatar 
                    size="60" 
                    color="#FAD7A0"
                    rounded>
                        <img v-if="r.image_src !== 'None'" :src="getImageSrc(index)" />
                        <v-icon size="35" v-else> {{ default_icon[comida] }} </v-icon>
                    </v-list-item-avatar>
                </v-list-item>
            </div>
            </v-list-item-content>

        </v-list-item>
        </div>
        </v-card>
        </v-container>
    </v-col>
    <v-col cols="12" md=4 >
    <!-- COL 2: STATS de las comidas + EXPLICACIÓN-->
        <div class="nutri-info">
            <nutritional-info :recipes="rec" ref="nutritionalInfoChild"></nutritional-info>


       </div>
       <div class="explanation">
            <user-card></user-card>
       </div>

       <div class="explanation">
            <explanation-card></explanation-card>
       </div>

       
    </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import ExplanationCard from './ExplanationCard.vue';
import UserCard from './UserCard.vue';
import NutritionalInfo from './NutritionalInfo';
import DoughnutChart from './DoughnutChart.vue';
import RecipeInfo from './RecipeInfo.vue';

export default {
  name: "Recomendacion",
  components: { 
      'doughnut-chart': DoughnutChart, 
      'explanation-card': ExplanationCard,
      'recipe-info': RecipeInfo,
      'nutritional-info': NutritionalInfo,
      'user-card': UserCard  },
  data() {
    NutritionalInfo
      return {
          rec: [], // recommendation full json
          overlay: false,
          zIndex: 1,
          recom_key: 0,
          recipes: [], // overlay values for each recipe
          comidas: ['desayuno','snack','comida','merienda','cena'],
          default_icon: {
                'desayuno': 'mdi-food-variant',
                'snack': 'mdi-food-apple',
                'comida': 'mdi-pasta',
                'merienda': 'mdi-food-croissant',
                'cena': 'mdi-noodles'
              }
    };
  },
  watch: { 
      	rec: function(newVal, oldVal) { // watch it
          this.rec = newVal
        }
    },
  methods: {
    getRecomendacion() {
        const path = "http://localhost:5000/recomendacion";
        var targetUser = {
            username: this.$store.getters.username
        }
        axios
        .post(path, targetUser)
        .then((res) => {
          this.rec = res.data;
          this.rec.forEach(element => {
            element.overlay = false
          })
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setUser() { // FUNCION a introducir en el código de usuarios!
        var userData = {'name': 'Francesca', // este sería el usuario sacado del form o de una request a flask
                        'age': 23, 
                        'sex': 'Mujer', 
                        'weight': 65, 
                        'height': 165, 
                        'body_type': 'Mesomorfo', 
                        'activity_level': 2, 
                        'objective': 0, 
                        'tdee': 2762.46711,
                        'water_intake': 2181.9684256}
        this.$store.commit("setUserData", {
            userdata: userData,
        }); 
    },  
    reload(){
        this.getRecomendacion()
    },
    //overlay methods
    displayInfo(index,recipe){
        this.setOverlay(index,true)
    },
    exitOverlay(index){
        this.setOverlay(index,false)
        this.forceRerender()
    },
    forceRerender() {
      this.recom_key += 1; 
    },
    setOverlay(index, value){
        var updatedRec = this.rec[index]
        updatedRec.overlay = value
        this.$set(this.rec, index, updatedRec)
        console.log(this.rec[index].overlay)
    },
    getImageSrc(index){
        return this.rec[index].image_src
    }
  },
  created() {
      this.setUser();
      this.getRecomendacion();
  }
};
</script>

<style scoped>

#title-row {
  padding-top: 40px;
}
</style>
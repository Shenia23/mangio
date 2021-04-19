<template>
  <div class="recommendation-body" id="main-row">
    
    <v-row >
    <v-col cols="12" md="6">
    <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
        <v-card
        class="division"
        >
        <v-row id="title-row">
            <v-col cols="12" md=3>
                <img height="160px" :src="apiin" />
            </v-col>
            <v-col cols="12" md="7" class="stats">
                <h4 class="headline mb-2"> Plan de Alimentación de Hoy para {{this.$store.getters.username}} </h4>
            </v-col>
            <v-col cols="12" md="2" class="stats">
                <v-icon class="reload"
                size="30px"
                @click="reload">
                mdi-cached
                </v-icon>
            </v-col>
        </v-row>

        <div class="overline text-left" style="margin:35px">
            <v-row>
                <v-col md="4">
                    <div @mouseover="active = true" @mouseleave="active = false">
                        <v-icon size="40px"> mdi-cup </v-icon>
                        {{ waterGlasses }}
                    </div>
                </v-col>
                <v-col md="6">
                    <div v-show="active" 
                    class="dialog text-center"> 
                        <div> ¡Hidratarse es importante! </div>
                        Deberías beber {{ this.$store.getters.waterIntake.toFixed(0) }} ml de agua al día
                    </div>
                </v-col>
            </v-row>
            

        </div>

        <div
        v-for="(comida, index) in comidas"
        :key="index"
        >  
        <div class="d-flex flex-no-wrap justify-space-between" :key="recom_key">
        <v-list-item three-line
        >
            <v-list-item-content>
            <div class="overline text-left" style="margin-left:20px"> 
                {{ comida }}
            </div>
            <div v-for="(r, index) in rec"
                :key="index"
                class="recipe-card-div"
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
                                {{ r.Nombre }}
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
        </div>
        </v-card>
    </v-col>
    <v-col cols="12" md=6 class="stats">
    <!-- COL 2: STATS de las comidas + EXPLICACIÓN-->

        <div class="infos">
            <user-card></user-card>
       </div>

        <div class="infos">
            <nutritional-info :recipes="rec" ref="nutritionalInfoChild"></nutritional-info>
       </div>
       
       <div class="infos">
            <explanation-card></explanation-card>
       </div>

       
    </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import ExplanationCard from './recom-plan/ExplanationCard.vue';
import UserCard from './recom-plan/UserCard.vue';
import NutritionalInfo from './recom-plan/NutritionalInfo';
import DoughnutChart from './graphs/DoughnutChart.vue';
import BarChart from './graphs/BarChart.vue';
import RecipeInfo from './recom-plan/RecipeInfo.vue';

export default {
  name: "Recomendacion",
  components: { 
      'doughnut-chart': DoughnutChart, 
      'explanation-card': ExplanationCard,
      'recipe-info': RecipeInfo,
      'nutritional-info': NutritionalInfo,
      'user-card': UserCard,
      'bar-chart': BarChart  },
  data() {
    NutritionalInfo
      return {
          rec: [], // recommendation full json
          active: false,
          zIndex: 1,
          recom_key: 0,
          comidas: ['desayuno','snack','comida','merienda','cena'],
          default_icon: {
                'desayuno': 'mdi-food-variant',
                'snack': 'mdi-food-apple',
                'comida': 'mdi-pasta',
                'merienda': 'mdi-food-croissant',
                'cena': 'mdi-noodles'
              },
          apiin: require('../assets/apiín.png')
    };
  },
  computed: {
    waterGlasses(){
        return Math.ceil(this.$store.getters.waterIntake/250)
    },
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
          this.rec = res.data
          this.rec.forEach(element => {
            element.overlay = false
          })
        })
        .catch((error) => {
          console.error(error);
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
    },
    mouseOver: function(){
            this.active = !this.active;   
        }
  },
  created() {
      this.getRecomendacion();
  }
};
</script>

<style scoped lang="scss">

#main-row {
  padding-top: 60px;
}

.recipe-card-div{
    margin-bottom: -10px;
}

.infos{
    margin:auto;
    width: 90%;
}

.stats{
    margin: auto;
}

.dialog{
    margin:auto;
    position: absolute;
    width: 400px;
    border-radius: 10px;
    background-color: rgb(197, 236, 182);
}

.division{
    width: 100%;
    margin-left: 2rem;
}

</style>
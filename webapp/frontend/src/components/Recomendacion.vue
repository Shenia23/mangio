<template>
  <div class="row recommendation-body">
    <v-col cols="12" md="7" style="margin-left:40px">
    <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
        <p></p>
        <h3 class="headline mb-2"> Plan de Alimentación de Hoy </h3>
        <v-container>
        <v-card
        class="mx-auto"
        max-width="550"
        outlined
        v-for="(comida, index) in comidas"
        :key="index"
        >  
        <div class="d-flex flex-no-wrap justify-space-between">
        <v-list-item three-line
        >
            <v-list-item-content>
            <div class="overline mb-1">
                {{ comida }}
            </div>
            <div v-for="(r, index) in rec"
                :key="index"
            >   
                <v-list-item v-if="r.Comida==comida" class="receta">
                    <v-list class="info_receta">
                        <v-list-item-title class="body-1 mb-1" >
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
                    <v-list-item-avatar tile size="50" color="grey"></v-list-item-avatar>
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
            <h3 class="headline mb-3"> Información Nutricional </h3>
            <doughnut-chart ref="doughnutChild" :new_data="chartData"
            :width="500"
            :height="300"></doughnut-chart>
       </div>
       <div class="explanation">
            <explanation-card></explanation-card>
       </div>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
import ExplanationCard from './ExplanationCard.vue';
import DoughnutChart from './DoughnutChart.vue';
import BodyType from './BodyType.vue';
//import Doughnut from '@/components/Doughnut.vue';

export default {
  name: "Recomendacion",
  components: { 
      'doughnut-chart': DoughnutChart, 
      'explanation-card': ExplanationCard },
  data() {
      return {
          rec: [],
          comidas: ['desayuno','snack','comida','merienda','cena'],
          chartData: {
            labels: ["Proteínas","Grasas","Carbohidratos"],
            datasets: [{
                borderWidth: 1,
                borderColor: [
                '#184d47',
                '#96bb7c',
                '#fad586'              
                ],
                backgroundColor: [
                '#184d47',
                '#96bb7c',
                '#fad586',        
                ],
                data: []
                }]
          }
    };
  },
  methods: {
    getRecomendacion() {
        const path = "http://localhost:5000/recomendacion";
        axios
        .get(path)
        .then((res) => {
          this.rec = res.data;
          let values = ['proteina','grasa','carbohidratos']
          values.forEach(element => {
              var e_sum = this.getSum(element,this.rec)
              this.chartData.datasets[0].data.push(e_sum.toFixed(1))
          });
          this.$refs.doughnutChild.renderChart(this.chartData);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getSum(type,rec) {
        var sum = 0;
        rec.forEach(element=>{
            sum += element[type]
        });
        return sum;
    }
  },
  created() {
      this.getRecomendacion();
  }
};
</script>
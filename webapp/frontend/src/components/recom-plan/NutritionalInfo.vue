<template>
  <div>
    <v-row>
      <v-col md="6">
        <v-card
          class="main"
        >
          <doughnut-chart key="chart_key" ref="dChart" :chartData="chartData"></doughnut-chart>
        </v-card>
      </v-col>

      <v-col md="6">
        <v-card
          class="main"
          >          
            <radar-chart ref="rChart" :chartData="radarData"></radar-chart>
          </v-card>
        
      </v-col>

    </v-row>
        <v-card
        class="main"
        >
          <bar-chart style="height: 300px" ref="bChart" :chartData="objectivesData"></bar-chart>
        </v-card>
    <v-row>

    </v-row>
  </div>

    <!--
    <div class="objectives subtitle-2">
      <v-row class="font-weight-bold">
        <v-col md="4"  >
        </v-col>
        <v-col md="4">
            Valores
        </v-col>
        <v-col md="4">
            Objetivos
        </v-col>
      </v-row>
      <v-row 
      v-for="objetivo in Object.keys(objectives)" :key="objetivo"
      >
          <v-col md="4" class="text-left">
              {{ objetivo }}
          </v-col>
          <v-col md="4">
              {{ objetivo=='energia' ? totalCalories + ' kcal' : getSum(objetivo) + ' g' }}
          </v-col>
          <v-col md="4" class="ml-auto">
              {{ objectives[objetivo] }} {{ objetivo=='energia' ? 'kcal' : 'g' }}
          </v-col>
      </v-row>
    </div>
    -->
</template>

<script>
import DoughnutChart from '../graphs/DoughnutChart.vue'
import BarChart from '../graphs/BarChart.vue'
import RadarChart from '../graphs/RadarChart.vue'

  export default {
  components: { DoughnutChart, BarChart, RadarChart },
      data: () => ({
        name: 'nutritional-info',
        chartData: {
            labels: ["Proteínas","Grasas","Carbos"],
            datasets: [{
                borderWidth: 1,
                borderColor: [
                'rgb(224, 144, 224)',
                '#ffffff',
                '#ffffff'              
                ],
                backgroundColor: [
                'rgb(224, 144, 224)',
                '#96bb7c',
                '#fad586',        
                ],
                data: []
                }]
          },
        objectivesData: {
          labels: ["Desayuno","Merienda","Comida","Snack","Cena"],
          datasets: [
              {
                  label: "Valor",
                  data: [],
                  borderWidth: 1,
                  minBarLength: 100,
                  borderColor: [
                    '#3f9b8be0',
                  'rgb(233, 174, 66)',          
                  '#96bb7c',
                  '#fad586',
                  'rgb(224, 144, 224)',
                  ],
                  backgroundColor: [
                    '#3f9b8be0',
                    'rgb(233, 174, 66, 0.7)' ,
                  '#96bb7ce0',
                  '#fad586e0',     
                  'rgb(224, 144, 224, 0.7)',
                  ],
              },
              {
                  label: "Objetivo",
                  data: [20, 10, 35, 10, 25],
                  borderWidth: 2,
                  minBarLength: 2,
                  borderColor: [
                    '#3f9b8be0',
                  'rgb(233, 174, 66)',   
                  '#96bb7c',
                  '#fad586',
                  'rgb(224, 144, 224)',
                  ],
              },
          ]
      },
      radarData:{
          labels: ["Proteínas","Grasas","Carbos"],
          datasets: [
              {
                  label: "Objetivo",
                  data: [],
                  borderColor: [
                  '#184d47'         
                  ],
              },
              {
                  label: "Valor",
                  data: [],
                  borderColor: [
                  '#96bb7c',           
                  ],
                  backgroundColor: [
                  '#96bb7ce0',      
                  ],
              },
          ]
      },
      objectives: {
        'energia': 2500,
        'grasa': 83,
        'proteina': 187,
        'carbohidratos': 250
      }
    }),
    computed: {
      obj: function () {
        return this.$store.getters.objectives
      }
    },
    props: {
        recipes: Array
    },
    watch: { 
      	recipes: function(newVal, oldVal) { // watch it
          this.recipes = newVal
          this.load()
        }
    },
    computed: {
      totalCalories: function() {
        var calSum = 0
        this.recipes.forEach( e =>{
          calSum += e.energia
        })
        return calSum.toFixed(0)
      }
    },
    methods: {
        load(){
            //load doughnut graph
            var values = ['proteina','grasa','carbohidratos'];
            var values_sum = []
            var macro_goals = []

            values.forEach(element => {
              var e_sum = this.getSum(element);
              values_sum.push(e_sum)

              var macro_objectives = this.$store.getters.objectives
              macro_goals.push(macro_objectives[element].toFixed(0))
            });

            var recipes_kcal = []
            this.objectivesData.labels.forEach(element => {
              var receta = this.recipes.find(o => o.Comida == element.toLowerCase())
              recipes_kcal.push(receta['energia'].toFixed(2))
            })

            // chart -> porcentaje macros
            this.chartData.datasets[0].data = this.getPercentages(values_sum);
            // bar -> porcentaje que ocupa cada comida vs objetivos
            this.objectivesData.datasets[0].data = this.getPercentages(recipes_kcal);

            // radar -> macros (gramos) objetivo vs recomendacion
            this.radarData.datasets[0].data = macro_goals;
            this.radarData.datasets[1].data = values_sum;

            this.$refs.dChart.reload();
            this.$refs.bChart.reload();
            this.$refs.rChart.reload();
        },
        getSum(type) {
        var sum = 0;
        this.recipes.forEach(element=>{
            sum += element[type]
        });
        return sum.toFixed(0);
        },
        getPercentages(sums){
          var pctg = []
          var total = sums.reduce((a, b) => parseInt(a) + parseInt(b), 0)
          sums.forEach( e => {
            pctg.push( (e*100 / total).toFixed(2))
          })
          return pctg
        }
    },
  }
</script>

<style scoped>

.main{
  margin-bottom: 1rem;
  padding: 20px;
}

.chart-div{
    margin: auto;
}

.objectives{
  margin: auto;
  padding: 5%;
  border-radius: 10px;
  background-color: rgb(197, 236, 182);
  color: #3f9b8be0;
}

</style>s
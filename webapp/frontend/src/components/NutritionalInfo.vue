<template>
  <v-row>
    <v-col md="6">
      <v-card
        class="main"
        max-width="400"
      >
        <div class="chart-div">
        <doughnut-chart key="chart_key" ref="dChart" :chartData="chartData"></doughnut-chart>
        </div>
      </v-card>
    </v-col>

    <v-col md="6">
      <v-card
        class="ain"
        max-width="400"
      >
        <div>
        <bar-chart ref="bChart" :chartData="objectivesData"></bar-chart>
        </div>
      </v-card>
    </v-col>
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
  </v-row>
</template>

<script>
import DoughnutChart from './graphs/DoughnutChart.vue'
import BarChart from './graphs/BarChart.vue'

  export default {
  components: { DoughnutChart, BarChart },
      data: () => ({
        name: 'nutritional-info',
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
          },
        objectivesData: {
          labels: ["Proteínas","Grasas","Carbohidratos"],
          datasets: [
              {
                  label: "Valor",
                  data: [4,6,7],
                  borderWidth: 1,
                  minBarLength: 100,
                  borderColor: [
                  '#184d47',
                  '#96bb7c',
                  '#fad586'              
                  ],
                  backgroundColor: [
                  '#185d47',
                  '#96bb7c',
                  '#fad586',        
                  ],
              },
              {
                  label: "Objetivo",
                  data: [7,8,6],
                  borderWidth: 2,
                  minBarLength: 2,
                  borderColor: [
                  '#184d47',
                  '#96bb7c',
                  '#fad586'              
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
              macro_goals.push(this.objectives[element])
            });

            this.chartData.datasets[0].data = values_sum;
            this.objectivesData.datasets[0].data = values_sum;
            this.objectivesData.datasets[1].data = macro_goals;

            this.$refs.dChart.reload();
            this.$refs.bChart.reload();
        },
        getSum(type) {
        var sum = 0;
        this.recipes.forEach(element=>{
            sum += element[type]
        });
        return sum.toFixed(0);
        },
    },
  }
</script>

<style scoped>

.main{
  padding: 20px;
}

.chart-div{
    width: 230px; 
    margin: auto;
}

.objectives{
  margin: auto;
  padding: 5%;
  border-radius: 10px;
  background-color: rgb(197, 236, 182);
}

</style>s
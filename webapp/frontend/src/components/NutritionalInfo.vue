<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-title>
      Información Nutricional
    </v-card-title>

    <v-divider></v-divider>

    <div id="chart-div">
    <doughnut-chart key="chart_key" ref="dChart" :new_data="chartData"></doughnut-chart>
    </div>
  </v-card>
</template>

<script>
import DoughnutChart from './DoughnutChart.vue'

  export default {
  components: { DoughnutChart },
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
          }
    }),
    props: {
        recipes: Array
    },
    watch: { 
      	recipes: function(newVal, oldVal) { // watch it
          this.recipes = newVal
          this.load()
        }
    },
    methods: {
        load(){
            //load doughnut graph
            this.chartData.datasets[0].data = []
            var values = ['proteina','grasa','carbohidratos'];
            values.forEach(element => {
              var e_sum = this.getSum(element,this.recipes);
              this.chartData.datasets[0].data.push(e_sum.toFixed(1));
            });
            this.$refs.dChart.renderChart(this.chartData);
        },
        getSum(type,rec) {
        var sum = 0;
        rec.forEach(element=>{
            sum += element[type]
        });
        return sum;
        },
        updateChart() {
            this.chart_key += 1; 
        },
    },
  }
</script>

<style scoped>

#chart-div{
    width: 230px; 
    margin: auto;
    padding-top: 20px;
    padding-bottom: 20px;
}

</style>
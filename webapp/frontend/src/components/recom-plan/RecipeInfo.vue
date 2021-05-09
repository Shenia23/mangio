<template>
  <v-card
    class="mx-auto my-12"
    max-width="550"
    color="white"
  >
    <div>
     <v-img v-if="recipe.image_src !== 'None'" :src="recipe.image_src" height="150"/>
     <v-icon v-else size="50" color="green" id="default-icon"> {{ default_icon[recipe.Comida] }} </v-icon>
    </div>

    <v-card-title class="black--text">{{ recipe.Nombre }}</v-card-title>

    <v-card-text class="black--text">
      <v-row v-if="recipe.Valoracion !== 'None'"
        align="center"
        class="mx-0"
      >
        <v-rating 
          :value="recipe.Valoracion"
          background-color="green lighten-3"
          color="green"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>
        
        <div class="grey--text ml-4">
          {{ recipe.Valoracion}}
        </div>
      </v-row>

      
      <v-row>
        <v-col md="6">
          <div class="my-4 subtitle-1 text-left" style="margin-left: 20px;">
            Ingredientes
          </div>
          <div v-for="(ing, index) in recipe.Ingredientes" :key="index">
                <v-row v-if="ing.Unidad !== 'None'" class="ing-list">
                  <v-icon color="green">mdi-chevron-right</v-icon> {{ ing.Ingrediente }}: {{ ing.Cantidad}} {{ ing.Unidad}}
                </v-row>
                <v-row v-else class="ing-list"> 
                  <v-icon color="green">mdi-chevron-right</v-icon> {{ ing.Ingrediente }}: {{ ing.Total_Grams.toFixed(0) }} gramos
                </v-row>
          </div>
          <v-card-text>
          <v-chip-group
            active-class="deep-purple accent-4 white--text"
            column
          >
            <v-chip>{{ recipe.energia.toFixed(1) }} kcal </v-chip>

          </v-chip-group>
        </v-card-text>

        </v-col>
        <v-col md="5" style="margin: auto;">
          <div class="graph">
              <doughnut-chart :chartData="chartData"></doughnut-chart>
          </div>
        </v-col>    
      </v-row>

      
    </v-card-text>

    <v-divider color="grey" class="mx-4"></v-divider>

    <v-card-text class="black--text">
      {{ preferenceText(recipe['preference_score']) }} 
    </v-card-text>


  </v-card>
</template>

<script>
import DoughnutChart from '../graphs/DoughnutChart.vue';

  export default {
    components: {
      "doughnut-chart": DoughnutChart
    },
    data: () => ({
        name: 'recipe-info',
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
    }),
    props: {
        recipe: Object,
        default_icon: Object
    },
    created() {
      var values = ['proteina','grasa','carbohidratos'];
      var values_sum = []

      values.forEach(element => {
        values_sum.push(this.recipe[element])
      });

      this.chartData.datasets[0].data = this.getPercentages(values_sum);
    },
    methods: {
      getPercentages(sums){
          var pctg = []
          var total = sums.reduce((a, b) => parseInt(a) + parseInt(b), 0)
          sums.forEach( e => {
            pctg.push( (e*100 / total).toFixed(2))
          })
          return pctg
      },
      preferenceText(score){
        if(score>=0.8){
          return "Esta receta tiene una puntación muy alta según tus gustos, esperamos que la disfrutes."
        }
        else if(score>=0.3){
          return "Creemos que esta receta debería gustarte, ¡disfrútala!"
        }
        else if(score<=-0.3){
          return "Es posible que esta receta contenga algún ingrediente que no te guste, ¡pero también tenemos que tener en cuenta tus requisitos nutricionales! Siempre puedes cambiarla por algo que te apetezca más."
        }
        return "¡Esta receta es neutral!"
      }
    },
  }
</script>

<style scoped>

.ing-list {
  padding-left: 20px;
  padding-bottom: 10px;
}
#default-icon{
  padding-top: 10px;
}

.graph{
  width: 110%;
  position: relative;
}
</style>
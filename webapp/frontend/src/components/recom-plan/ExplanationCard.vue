<template>
  <v-card class="mx-auto">
    <v-img :src="img" height="150px"></v-img>

    <v-row>
      <v-col md="4" style="margin: auto">
        <img height="150px" :src="cabocha" />
      </v-col>
      <v-col md="8" style="margin: auto">
        <v-card-subtitle style="font-size: 120%">
          Basándonos en tu objetivo de <b>{{ this.$store.getters.objetivo}}</b> creemos que una distribución
          de macronutrientes con un <b>{{this.getPercentages(this.$store.getters.objectives)[0]}}%
          de proteína</b>, un <b>{{this.getPercentages(this.$store.getters.objectives)[2]}}% de carbohidratos </b>
          y un <b>{{this.getPercentages(this.$store.getters.objectives)[1]}}% de grasa </b> es la más apropiada
          para ti. Además como tienes un TDEE de <b>{{ this.$store.getters.tdee}}</b> calorías, te hemos recomendado 
          un plan con un consumo diario de <b>{{this.$store.getters.cals_obj}}</b> calorías para cumplir tu objetivo. 
         
          
          <br><br>
          Haz click para saber más.
        </v-card-subtitle>
      </v-col>
    </v-row>

    <v-card-actions id="card-action">
      <v-spacer></v-spacer>

      <v-btn icon @click="show = !show">
        <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-card-text style="font-size: 110%">
          * El TDEE es el gasto energético total de una persona en un día. Es
          decir, todas las calorías que gasta teniendo en cuenta su tasa
          metabólica basal y su actividad diaria. <br> <br>
          * Los macronutrientes son los nutrientes que necesitamos en mayor
          cantidad y que nos aportan energía. Este grupo está formado por
          proteínas, carbohidratos y grasas. <br> <br>
          * La tasa metabólica basal es la cantidad de calorías que tu cuerpo 
          gasta para realizar las funciones más básicas, como respirar.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
       name: 'explanation-card',
       img: require('../../assets/hq_fruit.jpeg'),
       cabocha: require('../../assets/colaboza.png'),
       show: false,
      };
    },
    methods: {
       getPercentages(sums){
         var values_sums = []
         values_sums.push(sums["proteina"])
         values_sums.push(sums["grasa"])
         values_sums.push(sums["carbohidratos"])
         
          var pctg = []
          var total = values_sums.reduce((a, b) => parseInt(a) + parseInt(b), 0)
          values_sums.forEach( e => {
            pctg.push( (e*100 / total).toFixed(0))
          })
          return pctg
        }
    },
  }
</script>

<style scoped>
.v-card {
  margin-top: 2rem;
}

#card-action {
  margin-top: -3rem;
}
</style>
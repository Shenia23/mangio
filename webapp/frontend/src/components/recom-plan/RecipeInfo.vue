<template>
  <v-card
    class="mx-auto my-12"
    max-width="500"
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

      <div class="my-4 subtitle-1">
        Ingredientes
      </div>
      
      <div v-for="(ing, index) in recipe.Ingredientes" :key="index">
          <v-row v-if="ing.Unidad !== 'None'" class="ing-list">
            – {{ ing.Ingrediente }}: {{ ing.Cantidad}} {{ ing.Unidad}}
          </v-row>
          <v-row v-else class="ing-list"> 
            – {{ ing.Ingrediente }}: {{ ing.Total_Grams.toFixed(0) }} gramos
          </v-row>
      </div>
    </v-card-text>

    <v-divider color="grey" class="mx-4"></v-divider>

    <v-card-title class="black--text">Información Nutricional</v-card-title>

    <v-card-text>
      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>{{ recipe.energia.toFixed(1) }} kcal </v-chip>

      </v-chip-group>
    </v-card-text>

  </v-card>
</template>

<script>
  export default {
      data: () => ({
        name: 'recipe-info',
    }),
    props: {
        recipe: Object,
        default_icon: Object
    },
    methods: {
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
</style>
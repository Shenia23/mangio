<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="500"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="200"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>{{ recipe.Nombre }}</v-card-title>

    <v-card-text>
      <v-row v-if="recipe.Valoracion !== 'None'"
        align="center"
        class="mx-0"
      >
        <v-rating 
          :value="recipe.Valoracion"
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
          <div v-if="ing.Unidad !== 'None'">
            {{ ing.Ingrediente }}: {{ ing.Cantidad}} {{ ing.Unidad}}
          </div>
          <div v-else>
            {{ ing.Ingrediente }}: {{ ing.Total_Grams.toFixed(0) }} gramos
          </div>
      </div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Información Nutricional</v-card-title>

    <v-card-text>
      <v-chip-group
        v-model="selection"
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
        recipe: Object
    },
    methods: {
    },
  }
</script>
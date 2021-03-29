<template>
  <v-sheet class="mx-auto" elevation="8" max-width="900">
    <v-slide-group v-model="model" class="pa-4" multiple show-arrows>
      <v-slide-item v-for="(item, i) in ingredient_options" :key="i" v-slot="{ active, toggle }">
        <v-card
          :color="active ? 'primary' : 'grey lighten-1'"
          class="ma-4"
          height="200"
          width="150"
          @click="toggle"
        >
            <v-card-text class = "ingredient_name">{{item}}</v-card-text>

          <v-row class="fill-height" align="center" justify="center">
            <v-scale-transition>
                
              
            </v-scale-transition>
          </v-row>

        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
</template>

<script>
export default {
  data: () => ({
    ingredient_options: [
      "sal",
      "cebolla",
      "huevo",
      "ajo",
      "pimienta",
      "leche",
      "aceite de oliva",
      "azúcar",
      "tomate",
      "aceite",
      "harina",
      "mantequilla",
      "agua",
      "perejil",
      "limón",
      "queso",
      "patata",
      "pollo",
      "pimiento",
      "pimienta negra",
      "vino",
      "zanahoria",
      "pimentón",
      "vinagre",
      "vainilla",
      "pan",
      "canela",
      "laurel",
      "arroz",
      "orégano",
    ],
  }),
};
</script>


<style scoped>
.ingredient_name{
      font-size: 20px;
      text-align: center;
      font-weight: bold;
      color: rgb(0, 135, 254);

}
</style>
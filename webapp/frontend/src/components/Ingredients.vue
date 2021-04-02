<template>
  <v-container class="pa-4 text-center" >
      <div> Selecciona tus <strong> ingredientes favoritos:</strong></div>

    <v-sheet class="mx-auto" elevation="8" max-width="900">
      <v-slide-group v-model="model" class="pa-4" multiple show-arrows>
        <v-slide-item
          v-for="(item, i) in ingredient_options"
          :key="i"
          v-slot="{ active, toggle }"
        >
          <v-card
            :color="active ? 'primary' : 'grey lighten-1'"
            class="ma-4"
            :id="item"
            height="200"
            width="150"
            @click="
              toggle();
              return_ingredients(item, liked_ingredients);
            "
          >
            <v-card-text class="ingredient_name">{{ item }}</v-card-text>

            <v-row class="fill-height" align="center" justify="center">
              <v-scale-transition> </v-scale-transition>
            </v-row>
          </v-card>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    liked_ingredients: [],
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
  methods: {
    return_ingredients: function (ingredient, liked_ingredients) {
      if (liked_ingredients.includes(ingredient) == false) {
        liked_ingredients.push(ingredient);
        this.$emit("changeSelectedIngredients", liked_ingredients);
      } else {
        for (var i = 0; i < liked_ingredients.length; i++) {
          if (liked_ingredients[i] == ingredient) {
            liked_ingredients.splice(i, 1);
          }
        }

        console.log(liked_ingredients);
        this.$emit("changeSelectedIngredients", liked_ingredients);
      }
    },
  },
};
</script>


<style scoped>
.ingredient_name {
  font-size: 20px;
  text-align: center;
  font-weight: bold;
  color: rgb(0, 247, 78);
}
</style>
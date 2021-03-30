<template>
  <v-container>
    <div>
      <h1 class="title">Creación de recetas</h1>
    </div>
    <v-form ref="form" v-model="valid" lazy-validation class="formulario">
      <v-text-field
        v-model="name"
        :counter="40"
        label="Nombre de la receta"
        required
        style="margin-bottom: 10px"
      ></v-text-field>

      <v-autocomplete
        v-model="value"
        :items="items"
        dense
        filled
        label="Filled"
      ></v-autocomplete>

      <v-btn color="green" fab dark style="margin-right: 20px">
        <v-icon dark large> add_circle_outline</v-icon>
      </v-btn>
      
      <v-btn :disabled="!valid" color="success" class="mr-4" @click="validate">
        CREATE RECIPE
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import BodyType from "./BodyType.vue";
import Ingredients from "./Ingredients.vue";
export default {
  components: { BodyType, Ingredients },
  data: () => ({
    valid: true,
    name: "",
    ingredients: [],
    units: [],
    quantities: [],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>


<style scoped>
.formulario {
  margin-top: 1cm;
  background-color: rgb(155, 245, 158);
  margin: auto;
  width: 80%;
  border: 3px solid rgb(97, 213, 97);
  padding: 10px;

  justify-content: flex-end;
  text-align: right;
  line-height: 200px;
}
input {
  height: 20px;
  flex: 0 0 200px;
  margin-left: 10px;
}
.inbtn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
}
</style>
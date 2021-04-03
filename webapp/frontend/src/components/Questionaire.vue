<template>
  <v-container>
    <div>
      <h1 class="title">Cuestionario de preferencias nutricionales</h1>
    </div>
    <v-form ref="form" v-model="valid" lazy-validation class="formulario">
      <v-text-field
        v-model="name"
        :counter="30"
        :rules="nameRules"
        label="Nombre"
        required
        style="margin-bottom: 10px"
      ></v-text-field>

      <v-text-field
        v-model="age"
        label="Edad"
        required
        type="number"
        style="margin-bottom: 20px"
      ></v-text-field>

      <v-select
        v-model="selected_sex"
        :items="sex_options"
        label="Selecciona tu sexo"
        solo
      ></v-select>

      <v-slider
        v-model="height.val"
        :label="height.label"
        :thumb-color="height.color"
        thumb-label="always"
        max="220"
        min="150"
        style="margin-bottom: 10px"
        required
      ></v-slider>

      <v-checkbox
        v-model="using_scale"
        label="Va a utilizar la balanza Xiaomi Mi Body Composition Scale 2 ?"
        color="red"
        hide-details
      ></v-checkbox>

      <div
        v-if="using_scale == true"
        class="if-balanza"
        style="width: 50%; padding: 5px"
      >
        <v-btn
          :loading="loading3"
          :disabled="loading3"
          color="blue-grey"
          class="ma-2 white--text"
          @click="loader = 'loading3'"
        >
          Conectar con balanza
          <v-icon right dark> mdi-bluetooth </v-icon>
        </v-btn>
      </div>

      <div v-else class="if-not-balanza">
        <v-slider
          v-model="weight.val"
          :label="weight.label"
          :thumb-color="weight.color"
          thumb-label="always"
          max="150"
          min="40"
          style="margin-bottom: 10px; margin-top: 40px"
          required
        ></v-slider>
      </div>

      <BodyType :body_type="body_type" @changeBodyType="body_type = $event">
      </BodyType>

      <v-select
        v-model="selected_activity"
        :items="activity_types"
        label="Cuánta actividad física realizas?"
        solo
      ></v-select>

      <v-select
        v-model="objective"
        :items="objectives"
        label="Selecciona tu objetivo nutricional"
        solo
      ></v-select>

      <Ingredients
        id="ingredients"
        :ingredients="ingredients"
        @changeSelectedIngredients="ingredients = $event"
      ></Ingredients>

      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="createUser"
      >
        Crear nuevo usuario
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import BodyType from "./BodyType.vue";
import Ingredients from "./Ingredients.vue";
import axios from "axios";

export default {
  components: { BodyType, Ingredients },
  data: () => ({
    sex_options: ["Hombre", "Mujer"],
    activity_types: [
      "1. Sedentario (nada de ejercicio / trabajo de oficina)",
      "2. Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
      "3. Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
      "4. Muy activo (ejercicio casi diario intenso)",
      "5. Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)",
    ],
    name: "",
    using_scale: false,
    objectives: ["Perder peso", "Mantener", "Ganar peso"],
    height: { label: "Altura (cm)", val: 165, color: "red" },
    weight: { label: "Peso (kg)", val: 65, color: "blue" },
    body_type: "default",
    ingredients: ["empty"],
    age: "",
    selected_activity: "",
    selected_sex: "",
    mi_scale_data: {
      weight: 63.95,
      weight_unit: "kg",
      bmi: 28.42,
      basal_metabolism: 1264.14,
      visceral_fat: 8.02,
      lean_body_mass: 48.59,
      body_fat: 40.94,
      water: 42.17,
      bone_mass: 2.36,
      muscle_mass: 35.41,
      protein: 13.2,
      body_type: "Overweight",
      metabolic_age: 48,
    },
  }),
  methods: {
    toggle_using_scale() {
      if (this.using_scale) {
        this.using_scale = false;
      } else {
        this.using_scale = true;
      }
    },
    createUser() {
      var new_user = {
        name: this.name,
        age: parseInt(this.age,10),
        sex: this.selected_sex,
        weight: this.weight.val,
        height: this.height.val,
        body_type: this.body_type,
        activity_level: this.activity_types.indexOf(this.selected_activity) + 1,
        objective: this.objectives.indexOf(this.selected_activity) + 1,
        liked_ingredients: this.ingredients,
        using_scale: this.using_scale,
        scale_data: this.mi_scale_data
      };
      console.log(new_user);

      axios({
        baseURL: "http://localhost:5000",
        url: "/newUser",
        method: "post",
        data: new_user,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>


<style scoped>
.formulario {
  margin-top: 1cm;
  background-color: rgb(155, 245, 158);
  margin: auto;
  width: 90%;
  border: 3px solid rgb(97, 213, 97);
  padding: 10px;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: right;
  line-height: 200px;
}
input {
  height: 20px;
  flex: 0 0 200px;
  margin-left: 10px;
}

.checkbox-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.checkbox-form .answers {
  display: flex;
  flex-direction: column;
  align-items: left;
  width: 100%;
}

.checkbox-form label {
  margin-left: 1em;
}

.checkbox-form .item {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 1em;
  height: 25px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  display: flex;
  align-items: center;
}

.checkbox-form .item input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkbox-form .checkmark {
  position: absolute;
  top: 1;
  left: 0;
  border-radius: 45%;
  height: 20px;
  width: 20px;
  background-color: white;
}

.checkbox-form .item input:checked ~ .checkmark {
  background-color: green;
}

.checkbox-form .checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.checkbox-form .item input:checked ~ .checkmark:after {
  display: block;
}

.checkbox-form .item .checkmark:after {
  left: 7px;
  top: 4px;
  width: 6px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style>
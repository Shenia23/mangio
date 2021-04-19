<template>
  <v-container>
    <div>
      <h1 class="title">Cuestionario de preferencias nutricionales</h1>
    </div>
    <v-stepper v-model="e6" vertical>
      <v-stepper-step :complete="e6 > 4" step="1" editable>
        ¿Quién eres?
        <small style="margin-top: 3px"
          >Cuéntanos un poco sobre ti, esto nos ayudará a personalizar tu plan
          de alimentación</small
        >
      </v-stepper-step>

      <v-stepper-content step="1">
        <v-text-field
          v-model="username"
          :counter="30"
          label="Nombre de usuario"
          style="margin-bottom: 10px"
        ></v-text-field>

        <v-text-field
          v-model="name"
          :counter="30"
          :rules="nameRules"
          label="Nombre"
          style="margin-bottom: 10px"
        ></v-text-field>

        <v-text-field
          v-model="age"
          label="Edad"
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
          style="margin-bottom: 20px"
        ></v-slider>
        <v-btn color="primary" @click="e6 = 2"> Continue </v-btn>
        <v-btn text> Cancel </v-btn>
      </v-stepper-content>

      <v-stepper-step :complete="e6 > 2" step="2" editable>
        ¿Cuánto pesas?
        <small style="margin-top: 3px">
          Recuerda, puedes conectarte con una balanza Xiaomi para una estimación
          más precisa</small
        >
      </v-stepper-step>

      <v-stepper-content step="2">
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
          <BodyType :body_type="body_type" @changeBodyType="body_type = $event">
          </BodyType>
        </div>
        <v-btn color="primary" @click="e6 = 3"> Continue </v-btn>
        <v-btn text> Cancel </v-btn>
      </v-stepper-content>

      <v-stepper-step :complete="e6 > 3" step="3" editable>
        Actividad física y objetivos nutricionales
        <small style="margin-top: 3px">
          Saber cuánto te mueves y cuál es tu objetivo nos ayudará a adaptar el
          plan a tus necesidades</small
        >
      </v-stepper-step>

      <v-stepper-content step="3">
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
        <v-btn color="primary" @click="e6 = 4"> Continue </v-btn>
        <v-btn text> Cancel </v-btn>
      </v-stepper-content>

      <v-stepper-step step="4" editable>
        Tus preferencias de comida
        <small style="margin-top: 3px">
          Nos gustaría además recomendarte comida que te guste... aunque a veces
          hay que hacer algún sacrificio ;)</small
        >
      </v-stepper-step>
      <v-stepper-content step="4">
        <Ingredients
          id="ingredients"
          :ingredients="ingredients"
          @changeSelectedIngredients="ingredients = $event"
        ></Ingredients>

        <p color="success" class="btn btn-1" @click="createUser">
          <svg>
            <rect x="0" y="0" fill="none" width="100%" height="100%"/>
          </svg>
          Crear nuevo usuario
        </p>

      </v-stepper-content>
    </v-stepper>
  </v-container>
</template>

<script>
import BodyType from "./BodyType.vue";
import Ingredients from "./Ingredients.vue";
import axios from "axios";
import VueSwing from "vue-swing";

export default {
  components: { BodyType, Ingredients, VueSwing },
  data: () => ({
    e6: 1,
    sex_options: ["Hombre", "Mujer"],
    activity_types: [
      "1. Sedentario (nada de ejercicio / trabajo de oficina)",
      "2. Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
      "3. Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
      "4. Muy activo (ejercicio casi diario intenso)",
      "5. Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)",
    ],
    username: "",
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
        username: this.username,
        name: this.name,
        age: parseInt(this.age, 10),
        sex: this.selected_sex,
        weight: this.weight.val,
        height: this.height.val,
        body_type: this.body_type,
        activity_level: this.activity_types.indexOf(this.selected_activity) + 1,
        objective: this.objectives.indexOf(this.selected_activity) + 1,
        liked_ingredients: this.ingredients,
        using_scale: this.using_scale,
        scale_data: this.mi_scale_data,
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


<style scoped lang="scss">
.formulario {
  margin-top: 1cm;
  background-color: rgb(113, 192, 113);
  margin: auto;
  width: 95%;
  border: 2px solid rgb(97, 213, 97);
  padding: 10px;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
  line-height: 300px;
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

.card {
  margin-top: 30 px;
  align-items: center;
  background-color: rgb(232, 254, 202);
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  font-size: 22px;
  height: 300px;
  justify-content: center;
  left: calc(50% - 100px);
  position: absolute;
  width: 200px;
}



@import url(https://fonts.googleapis.com/css?family=Roboto:400,100,900);

//colors
$red: #E1332D;
$white: #fff;

//base styles

* {
  box-sizing: inherit;
  transition-property: all;
  transition-duration: .6s;
  transition-timing-function: ease;
}

  
  p {
    background: rgba($white, 0);
    margin: auto;
    line-height: 1.4;
    padding: .25em;
    text-decoration: none;
    
  }
//default button
.btn {
  color: green;
  cursor: pointer;
  // display: block;
  font-size:16px;
  font-weight: 400;
  line-height: 45px;
  max-width: 250px; 
  position: relative;
  text-decoration: none;
  text-transform: uppercase;
  width: 100%; 
  
  
}

/////////////////////////////////
//button one
///////////////////////////////
.btn-1 {
  background: white;
  font-weight: 100;
  
  svg {
    height: 45px;
    left: 0;
    position: absolute;
    top: 0; 
    width: 100%; 
  }
  
  rect {
    fill: none;
    stroke: green;
    stroke-width: 2;
    stroke-dasharray: 422, 0;
    transition: all 0.35s linear;
  }
}

.btn-1:hover {
  font-weight: 900;
  letter-spacing: 1px;
  color: green;
  
  rect {
    stroke-width: 5;
    stroke-dasharray: 15, 410;
    stroke-dashoffset: 48;
    transition: all 1.35s cubic-bezier(0.19, 1, 0.22, 1);
  }
}

////////////////////////////
//button two
//////////////////////////
.btn-2 {
    letter-spacing: 0;
}

.btn-2:hover,
.btn-2:active {
  letter-spacing: 5px;
}

.btn-2:after,
.btn-2:before {
  backface-visibility: hidden;
  border: 1px solid rgba(#fff, 0);
  bottom: 0px;
  content: " ";
  display: block;
  margin: 0 auto;
  position: relative;
  transition: all 280ms ease-in-out;
  width: 0;
}

.btn-2:hover:after,
.btn-2:hover:before {
  backface-visibility: hidden;
  border-color: #fff;
  transition: width 350ms ease-in-out;
  width: 70%;
}

.btn-2:hover:before {
  bottom: auto;
  top: 0;
  width: 70%;
}

/////////////////////////////
//button -3 
///////////////////////////
.btn-3 {
  background: lighten($red, 3%);  
  border: 1px solid darken($red, 4%);
  box-shadow: 0px 2px 0 darken($red, 5%), 2px 4px 6px darken($red, 2%);
  font-weight: 900;
  letter-spacing: 1px;
  transition: all 150ms linear;
}

.btn-3:hover {
  background: darken($red, 1.5%);
  border: 1px solid rgba(#000, .05);
  box-shadow: 1px 1px 2px rgba(#fff, .2);
  color: lighten($red, 18%); 
  text-decoration: none;
  text-shadow: -1px -1px 0 darken($red, 9.5%);
  transition: all 250ms linear;
}




</style>
<template>
  <v-container>
    <div>
    <h1 class="title"> Cuestionario de preferencias nutricionales </h1>
  </div>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    class="formulario"
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Nombre"
      required
      style="margin-bottom:10px;"

    ></v-text-field>
    <v-text-field
      label="Edad"
      required
      type="number"
      style="margin-bottom:10px;"
    ></v-text-field>
   
    <v-slider
      v-model="height.val"
      :label="height.label"
      :thumb-color="height.color"
      thumb-label="always"
      max="220"
      min="150"
      style="margin-bottom:10px;"
      required
    ></v-slider>

        <input type="checkbox" value="balanza" v-model="checkedBalanza">
    <label for="jack">Usar Balanza</label>
    <br>

    <div v-if="checkedBalanza=='balanza'" class="if-balanza">
    <span> Aquí meter conector ble con balanza {{ checkedNames }}</span>
    </div>

    <div v-else class="if-not-balanza">
    <v-slider
      v-model="weight.val"
      :label="weight.label"
      :thumb-color="weight.color"
      thumb-label="always"
      max="150"
      min="40"
      style="margin-bottom:10px;"
      required
    ></v-slider>
    
     <BodyType :body_type="body_type" @changeBodyType="body_type = $event" 
     >
     </BodyType>

      <v-select
        :items="activity_types"
        label="Cuánta actividad física realizas?"
        solo
      ></v-select>

    </div>


    <Ingredients id="ingredients" :ingredients="ingredients" @changeSelectedIngredients="ingredients_list = $event"></Ingredients>


    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validate
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>
    
    

    <v-btn
      color="warning"
      @click="resetValidation"
    >
      Reset Validation
    </v-btn>
  </v-form>
  </v-container>
</template>

<script>
import BodyType from './BodyType.vue'
import Ingredients from './Ingredients.vue'
  export default {
  components: { BodyType , Ingredients},
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 20) || 'Name must be less than 10 characters',
      ],
      select: null,
      activity_types: [
                "Sedentario (nada de ejercicio / trabajo de oficina)",
                "Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
                "Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
                "Muy activo (ejercicio casi diario intenso)",
                "Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)"
            ],
      height: { label: 'Altura (cm)', val: 165, color: 'red' },
      weight: { label: 'Peso (kg)', val: 65, color: 'blue' },
      body_type : "default",
      ingredients: ["empty"],
      checkedBalanza: []
    }),
    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      }
    },
  }
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
</style>
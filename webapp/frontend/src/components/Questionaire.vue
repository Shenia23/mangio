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
      :counter="30"
      :rules="nameRules"
      label="Nombre"
      required
      style="margin-bottom:10px;"

    ></v-text-field>
    <v-text-field
      label="Edad"
      required
      type="number"
      style="margin-bottom:20px;"
    ></v-text-field>

    <v-radio-group v-model="radios">
      <template v-slot:label>
        <div> Selecciona tu <strong> sexo:</strong></div>
      </template>
      <v-radio value="Mujer">
        <template v-slot:label>
          <div> Mujer </div>
        </template>
      </v-radio>
      <v-radio value="Hombre">
        <template v-slot:label>
          <div> Hombre </div>
        </template>
      </v-radio>
    </v-radio-group>
   
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


    <v-checkbox
              v-model="checkedBalanza"
              label="Va a utilizar la balanza Xiaomi Mi Body Composition Scale 2 ?"
              color="red"
              value="balanza"
              style="margin-bottom:10px;"
              hide-details
    ></v-checkbox>
    
    <div v-if="checkedBalanza=='balanza'" class="if-balanza">
      <span> Aquí meter conector ble con balanza</span>
    </div>

    <div v-else class="if-not-balanza">
      <v-slider
        v-model="weight.val"
        :label="weight.label"
        :thumb-color="weight.color"
        thumb-label="always"
        max="150"
        min="40"
        style="margin-bottom:10px;margin-top:40px;"
        required
      ></v-slider>
        </div>

      <BodyType :body_type="body_type" @changeBodyType="body_type = $event" 
      >
      </BodyType>

        <v-select
          :items="activity_types"
          label="Cuánta actividad física realizas?"
          solo
        ></v-select>

  

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
  width: 90%;
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
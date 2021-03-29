
<template>

<div class="row">
  <div class="column">      
    <v-expansion-panels  style="margin: 12% 0 0 5%" inset>
    <v-expansion-panel>
        <v-expansion-panel-header>Perfiles prediseñados</v-expansion-panel-header>
        <v-expansion-panel-content>
          Perfiles hechos previamente para comprobar como se ajustaría el plan de alimentación a distintos tipos de personas.
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Nuevos perfiles</v-expansion-panel-header>
        <v-expansion-panel-content>
         En este apartado el usuario se registra, respondiendo un formulario y tomando sus medidas con la báscula.
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Plan de alimentación</v-expansion-panel-header>
        <v-expansion-panel-content>
          Se disponen las comidas que se sugerirán al usuario.
        </v-expansion-panel-content>
      </v-expansion-panel>

        <v-expansion-panel>
        <v-expansion-panel-header>Perfil de usuario</v-expansion-panel-header>
        <v-expansion-panel-content>
          El usuario puede ver más datos sobre sí mismo.
        </v-expansion-panel-content>
      </v-expansion-panel>

        <v-expansion-panel>
        <v-expansion-panel-header>Nuevas recetas</v-expansion-panel-header>
        <v-expansion-panel-content>
         Añadir nuevas recetas y calcular sus valores nutricionales.
        </v-expansion-panel-content>
      </v-expansion-panel>
  </v-expansion-panels></div>
  
    <div class="column">   <img src="../assets/monigote.png"  style="width:40%;height:72%; margin:8% 0 0 5%"></div>
</div>



</template>




<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
      .then(response => {
        this.randomNumber = response.data.randomNumber
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>

<style scoped>
.column {
  float: left;
  width: 50%;
}
</style>


<template>
  <div class="container" style="height: 50%">
    <img src="../assets/comida.jpg" />
    <div class="top-left">
      <h3>MANGIO PERMITE GENERAR</h3>
    </div>
    <div class="top-left2">
      <h3>UN PLAN DE RECOMENDACIÓN</h3>
    </div>
    <div class="top-left3">
      <h3>FÁCIL DE SEGUIR</h3>
    </div>

    <div class="top-right">
      <v-expansion-panels inset>
        <v-expansion-panel>
          <v-expansion-panel-header
            ><h2>Perfiles prediseñados</h2></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <p>
              Perfiles hechos previamente para comprobar como se ajustaría el
              plan de alimentación a distintos tipos de personas.
            </p></v-expansion-panel-content
          >
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header
            ><h2>Nuevos perfiles</h2></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <p>
              En este apartado el usuario se registra, respondiendo un
              formulario y tomando sus medidas con la báscula.
            </p>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header
            ><h2>Plan de alimentación</h2></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <p>Se disponen las comidas que se sugerirán al usuario.</p>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header
            ><h2>Perfil de usuario</h2></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <p>El usuario puede ver más datos sobre sí mismo.</p>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header
            ><h2>Nuevas recetas</h2></v-expansion-panel-header
          >
          <v-expansion-panel-content>
            <p>Añadir nuevas recetas y calcular sus valores nutricionales.</p>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>

    <div class="row" style="margin-left: 15%">
      <div class="column" style="margin-left: 18%">
        <v-card class="mx-auto" max-width="100%">
          <v-img
            :src="require('../assets/receta.png')"
            aspect-ratio="1"
          ></v-img>

          <v-card-title> +2000 RECETAS </v-card-title>

          <v-card-subtitle> Una amplia selección de platos.</v-card-subtitle>
        </v-card>
      </div>

      <div class="column" style="margin-left: 18%">
        <v-card class="mx-auto" max-width="330">
          <v-img
            :src="require('../assets/receta.png')"
            aspect-ratio="1"
          ></v-img>

          <v-card-title> +2000 RECETAS </v-card-title>

          <v-card-subtitle> Una amplia selección de platos.</v-card-subtitle>
        </v-card>
      </div>

      <div class="column" style="margin-left: 18%">
        <v-card class="mx-auto" max-width="330">
          <v-img
            :src="require('../assets/receta.png')"
            aspect-ratio="1"
          ></v-img>

          <v-card-title> +2000 RECETAS </v-card-title>

          <v-card-subtitle> Una amplia selección de platos.</v-card-subtitle>
        </v-card>
      </div>
    </div>
  </div>
</template>




<script>
import axios from "axios";
export default {
  data() {
    return {
      randomNumber: 0,
    };
  },
  methods: {
    getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },
    getRandom() {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`;
      axios
        .get(path)
        .then((response) => {
          this.randomNumber = response.data.randomNumber;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getRandom();
  },
};
</script>

<style scoped>
.container {
  position: relative;
  text-align: center;
  margin-left: -10%;
  font-size: 180%;
  margin-right: -10%;
  margin-top: -1%;
}

.column {
  margin-top: 1%;
}

p {
  font-size: 80%;
}

/* Top left text */
.top-left {
  position: absolute;
  background-color: white;
  top: 40%;
  left: 18%;
}

.top-left2 {
  position: absolute;
  background-color: white;
  top: 54%;
  left: 18%;
}

.top-left3 {
  position: absolute;
  background-color: white;
  top: 68%;
  left: 18%;
}

/* Top right text */
.top-right {
  position: absolute;
  top: 30%;
  left: 60%;
  width: 55%;
}
</style>

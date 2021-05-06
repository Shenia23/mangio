<template>
  <v-container>
    <div>
      <h1 class="title">Selección de perfil predeterminado</h1>
    </div>
    <v-row align="center">
      <v-item-group v-model="window" class="shrink mr-6" mandatory tag="v-flex">
        <v-item
          v-for="n in predetermined_profiles.length"
          :key="n"
          v-slot="{ active, toggle }"
        >
          <div>
            <v-btn :input-value="active" icon @click="toggle">
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </div>
        </v-item>
      </v-item-group>

      <v-col>
        <v-window v-model="window" vertical>
          <v-window-item v-for="n in predetermined_profiles.length" :key="n">
            <div class="row">
              <v-col cols="12" md="5">
                <v-card flat>
                  <v-card-text>
                    <v-row class="mb-4" align="center">
                      <v-avatar color="rgb(113, 192, 113)" class="mr-4"
                        ><v-icon>mdi-face</v-icon></v-avatar
                      >
                      <strong class="title">
                        Usuario {{ n }}:
                        {{ predetermined_profiles[n - 1].username }}
                      </strong>
                      <v-spacer></v-spacer>
                    </v-row>
                    <br><br>
                    <p style="font-size: 20px">
                      <b>Nombre</b> : {{ predetermined_profiles[n - 1].name }}
                    </p>
                    <p style="font-size: 20px">
                      <b>Edad</b> : {{ predetermined_profiles[n - 1].age }}
                    </p>
                    <p style="font-size: 20px">
                      <b>Sexo</b> : {{ predetermined_profiles[n - 1].sex }}
                    </p>
                    <p style="font-size: 20px">
                      <b>Altura</b> : {{ predetermined_profiles[n - 1].height }}
                    </p>

                    <p style="font-size: 20px">
                      <b>Peso</b> : {{ predetermined_profiles[n - 1].weight }}
                    </p>
                    <p style="font-size: 20px">
                      <b>Tipo de cuerpo</b> :
                      {{ predetermined_profiles[n - 1].body_type }}
                    </p>

                    <p style="font-size: 20px">
                      <b>Nivel de actividad</b> :
                      {{
                        activity_types[
                          predetermined_profiles[n - 1].activity_level - 1
                        ]
                      }}
                    </p>

                    <p style="font-size: 20px">
                      <b>Objetivo</b> :
                      {{ objectives[predetermined_profiles[n - 1].objective] }}
                    </p>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col cols="12" md="2">
                <br><br><br>
                <v-img
                  center
                  max-height="600"
                  max-width="250"
                  contain
                  :src="predetermined_profiles[n - 1].image_path"
                ></v-img>
              </v-col>
              <v-col cols="12" md="4">
                <br><br><br><br><br>
                <p style="font-size: 25px"> <i>"{{predetermined_profiles[n - 1].custom_text}}"</i></p>
              </v-col>
            </div>
            <DialogPredetProfileSelected v-model="showPredetSelected" />
            
            <p
              color="success"
              class="btn btn-1"
              @click="setUser(predetermined_profiles[n - 1])"
            >
              <svg>
                <rect x="0" y="0" fill="none" width="100%" height="100%" />
              </svg>
              Seleccionar perfil!
            </p>
          </v-window-item>

          
        </v-window>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DialogPredetProfileSelected from "./DialogPredetProfileSelected.vue";

export default {
  components: {
    DialogPredetProfileSelected,
  },
  props: {
    predetermined_profiles: Array,
  },
  data: () => ({
    length: 3,
    window: 0,
    activity_types: [
      "Sedentario (nada de ejercicio / trabajo de oficina)",
      "Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
      "Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
      "Muy activo (ejercicio casi diario intenso)",
      "Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)",
    ],
    objectives: ["Perder peso", "Mantener", "Ganar peso"],
    showPredetSelected: false,
  }),
  methods: {
    setUser(userData) {
      // FUNCION a introducir en el código de usuarios!
      console.log(userData);
      this.showPredetSelected = true;
      this.$store.commit("setUserData", {
        userdata: userData,
      });
    },
  },
};
</script>

<style scoped  lang="scss">
.perfiles {
  margin-top: 1cm;
  margin: auto;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
}
@import url(https://fonts.googleapis.com/css?family=Roboto:400,100,900);

//colors
$red: #e1332d;
$white: #fff;

//base styles

* {
  box-sizing: inherit;
  transition-property: all;
  transition-duration: 0.6s;
  transition-timing-function: ease;
}

p {
  background: rgba($white, 0);
  margin: auto;
  line-height: 1.4;
  padding: 0.25em;
  text-decoration: none;
}
//default button
.btn {
  color: var(--main-orange);
  cursor: pointer;
  // display: block;
  font-size: 16px;
  font-weight: 400;
  line-height: 45px;
  max-width: 250px;
  position: relative;
  text-decoration: none;
  text-transform: uppercase;
  width: 100%;
}

.btn-1 {
  background: white;
  font-weight: 500;

  svg {
    height: 45px;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
  }

  rect {
    fill: none;
    stroke: var(--main-orange);
    stroke-width: 2;
    stroke-dasharray: 422, 0;
    transition: all 0.35s linear;
  }
}

.btn-1:hover {
  font-weight: 900;
  letter-spacing: 1px;
  color: var(--main-orange);

  rect {
    stroke-width: 5;
    stroke-dasharray: 15, 410;
    stroke-dashoffset: 48;
    transition: all 1.35s cubic-bezier(0.19, 1, 0.22, 1);
  }
}
</style>
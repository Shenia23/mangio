<template>
  <v-container >
      <div>
      <h1 class="title">Selección de usuario</h1>
    </div>
    <v-row align="center">
      <v-item-group v-model="window" class="shrink mr-6" mandatory tag="v-flex">
        <v-item v-for="n in users.length" :key="n" v-slot="{ active, toggle }">
          <div>
            <v-btn :input-value="active" icon @click="toggle">
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </div>
        </v-item>
      </v-item-group>

      <v-col>
        <v-window v-model="window" class="elevation-1" vertical>
          <v-window-item v-for="n in users.length" :key="n">
            <v-card flat>
              <v-card-text>
                <v-row class="mb-4" align="center">
                  <v-avatar color="rgb(113, 192, 113)" class="mr-4"><v-icon>mdi-face</v-icon></v-avatar>
                  <strong class="title"> Usuario {{ n }}: {{users[n-1].username}} </strong>
                  <v-spacer></v-spacer>
                  <v-btn icon>
                    <v-icon>mdi-chevron-double-right</v-icon>
                  </v-btn>
                </v-row>

                <p>
                  <b>Nombre</b> : {{users[n-1].name}}
                </p>
                <p>
                  <b>Edad</b> : {{users[n-1].age}}
                </p>
                <p>
                  <b>Sexo</b> : {{users[n-1].sex}}
                </p>
                <p>
                  <b>Altura</b> : {{users[n-1].height}}
                </p>

                <p>
                  <b>Peso</b> : {{users[n-1].weight}}
                </p>
                <p>
                  <b>Tipo de cuerpo</b> : {{users[n-1].body_type}}
                </p>

                <p>
                  <b>Nivel de actividad</b> : {{activity_types[users[n-1].activity_level-1]}}
                </p>

                <p>
                  <b>Objetivo</b> : {{objectives[users[n-1].objective-1]}}
                </p>

                
              </v-card-text>
            </v-card>
          </v-window-item>
        </v-window>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
   users: Array
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
  }),
  methods:{ 
      
  }
};
</script>

<style scoped>
.perfiles {
  margin-top: 1cm;
  margin: auto;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
}
</style>
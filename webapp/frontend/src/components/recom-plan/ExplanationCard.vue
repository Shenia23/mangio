<template>
  <v-card
    class="mx-auto"
  >
    <v-img
      :src="img"
      height="150px"
    ></v-img>

    <v-card-title>
      Explicación
    </v-card-title>

    <v-row>
      <v-col md="4" style="margin: auto">
          <img height="150px" :src="cabocha" />
      </v-col>
      <v-col md="7" style="margin: auto">
        <v-card-subtitle>
          ¡Te explicamos qué criterios tomamos a la hora de hacer recomendaciones!
          Haz click para saber más.
        </v-card-subtitle>
    </v-col>
    </v-row>

    <v-card-actions>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
          <v-card-text>
            Info extra! Algún gráfico, whatever
          </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
       name: 'explanation-card',
       img: require('../../assets/fruit.jpg'),
       cabocha: require('../../assets/colaboza.png'),
       show: false,
      }
    },
  }
</script>

<style scoped>

.v-card{
  margin-top: 2rem;
}

</style>s
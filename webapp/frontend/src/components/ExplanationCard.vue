<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      :src="img"
      height="100px"
    ></v-img>

    <v-card-title>
      Explicación
    </v-card-title>

    <v-card-subtitle>
      La recomendación se basa en...
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="show = !show"
      >
       Más
      </v-btn>

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
       img: require('../assets/fruit.jpg'),
       show: false,
      }
    },
  }
</script>
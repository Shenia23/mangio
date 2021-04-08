<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-card-title>
      Información de Usuario
    </v-card-title>

    <v-card-subtitle>
      {{ this.$store.getters.userdata.name }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="show = !show"
      >
       {{ show ? 'Menos' : 'Más'}}
      </v-btn>

      <v-spacer></v-spacer>

    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-card-text>
          {{ this.$store.getters.userdata.name }} tiene {{this.$store.getters.userdata.age}} años
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
       name: 'user-card',
       show: false
      }
    },
  }
</script>
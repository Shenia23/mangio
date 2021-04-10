<template>
<div>
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

      <v-card
      class="mx-auto"
      max-width="700">
          <div class="media-left">
            <figure class="image is-64x64">
              <img :src="img" alt="Image">
            </figure>
          </div>
          <div class="media-content">
            <div class="content">
              <p>
                <strong>Nombre</strong> <small>Edad</small>
                <br>
                Cosas
              </p>
            </div>
              <div class="level-left">
                <a class="level-item">
                  <span class="icon is-small"><i class="fas fa-heart"></i></span>
                  <span class="likes">3</span>
                </a>
              </div>
          </div>
      </v-card> 
    </div>
</template>

<script>
  export default {
    data () {
      return {
       name: 'user-card',
       show: false,
       img: require('../assets/fruit.jpg'),
      }
    },
  }
</script>
<template>
  <v-card
    class="mx-auto main"
  >
    <v-container>
    <v-layout>
      <v-flex xs6 pr-3>
      <v-list-item >
      <v-list-item-content>
          <v-list-item>
              <div class="avatar">
                  <v-list-item-avatar 
                  size="90" 
                  color="#FAD7A0"
                  id="avatar-icon"
                  >
                      <img :src="img" />
                  </v-list-item-avatar>
              </div>
              <v-list>
                  <v-list-item-title class="body-1" >
                      <p class="text-left font-weight-bold">
                          {{ this.$store.getters.userdata.name }} 
                      </p> 
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-left caption"> 
                      <p>
                          @{{ this.$store.getters.userdata.username }}
                      </p> 
                  </v-list-item-subtitle>
              </v-list>
          </v-list-item>
      </v-list-item-content>
      </v-list-item>
      </v-flex>
      <v-divider vertical></v-divider>
        <v-flex xs6 class="text-left caption">
          <v-list-item >
          <v-list-item-content>
          <v-list-item>
          <v-list>
          <p>
              {{ this.$store.getters.userdata.age }} años
          </p> 
          <p>
            {{ this.$store.getters.userdata.weight}} kg
          </p>
          <p>
            Objetivo: {{ goals[this.$store.getters.userdata.objective]}}
          </p>
          </v-list>
          </v-list-item>
          </v-list-item-content>
          </v-list-item>
        </v-flex>
    </v-layout>
    </v-container>

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
          Gustos
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
       show: false,
       img: require('../../assets/fruit.jpg'),
       goals: ['','Bajar de peso','Mantener el peso','Subir de peso']
      }
    },
  }
</script>

<style scoped>

.avatar{
    border-style: dashed;
    border-radius: 50%;
    border-width: 1pt;
    margin-right: 20px;
    padding: 5px;
} 

#avatar-icon{
    margin: auto;
}

.main{
  margin-bottom: 1rem;

}

</style>
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-list-item 
        >
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
                <v-list-item-subtitle> 
                    <p class="text-left caption">
                        {{ this.$store.getters.userdata.age }} años
                    </p> 
                </v-list-item-subtitle>
            </v-list>
        </v-list-item>
    </v-list-item-content>
    </v-list-item>

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
       show: false,
       img: require('../assets/fruit.jpg'),
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

</style>
<template>
  <v-container>
      <v-card>
    <v-tabs
      v-model="tab"
      background-color="rgb(113, 192, 113)"
      centered
      dark
      icons-and-text
    >
      <v-tabs-slider></v-tabs-slider>

      <v-tab href="#tab-1">
        Nuevo usuario
        <v-icon>mdi-account-plus</v-icon>
      </v-tab>

      <v-tab href="#tab-2">
        Perfiles predeterminados
        <v-icon>mdi-account-multiple</v-icon>
      </v-tab>

      <v-tab href="#tab-3">
        Acceder
        <v-icon>mdi-account-key</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        :key="1"
        :value="'tab-1'"
      >
        <Questionaire/>
      </v-tab-item>
      <v-tab-item
        :key="2"
        :value="'tab-2'"
      >
        <PredeterminedProfiles/>
      </v-tab-item>
      <v-tab-item
        :key="3"
        :value="'tab-3'"
      >
      Acceder
      </v-tab-item>
    </v-tabs-items>
  </v-card>
    
  

    
  </v-container>
</template>

<script>
import Questionaire from "./Questionaire.vue";
import PredeterminedProfiles from "./PredeterminedProfiles.vue"

export default {
  components: { Questionaire, PredeterminedProfiles},
  data: () => ({
      tab: null,
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      
  }),
  methods: {},
};
</script>


<style scoped>
.nav{
    background: "transparent";

}

</style>
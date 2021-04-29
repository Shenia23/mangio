<template>
  <v-container>
      <v-card>
    <v-tabs
      v-model="tab"
      background-color="var(--main-orange)"
      centered
      dark
      icons-and-text
    >
      <v-tabs-slider></v-tabs-slider>

      <v-tab href="#tab-1">
        Nuevo usuario
        <v-icon>mdi-account-plus</v-icon>
      </v-tab>

      <v-tab href="#tab-2" v-on:click="getPredeterminedProfiles">
        Perfiles predeterminados
        <v-icon>mdi-account-multiple</v-icon>
      </v-tab>

      <v-tab href="#tab-3" v-on:click="getExistingUsers">
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
        <PredeterminedProfiles :predetermined_profiles="this.predetermined_profiles"/>
      </v-tab-item>
      <v-tab-item
        :key="3"
        :value="'tab-3'"
      >
      <Users :users="this.users"/>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
    

    
  </v-container>
</template>

<script>
import Questionaire from "./Questionaire.vue";
import PredeterminedProfiles from "./PredeterminedProfiles.vue"
import Users from "./Users.vue"
import axios from "axios";

export default {
  components: { Questionaire, PredeterminedProfiles, Users},
  data: () => ({
      tab: null,
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      predetermined_profiles: null,
      users: null,
  }),
  methods: {
    getPredeterminedProfiles() {
      const path = `http://localhost:5000/predeterminedUserProfiles`;
      axios
        .get(path)
        .then((response) => {
          console.log(response)

          this.predetermined_profiles = response.data.predetermined_profiles;
          console.log(this.predetermined_profiles)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getExistingUsers() {
      const path = `http://localhost:5000/availableUsers`;
      axios
        .get(path)
        .then((response) => {
          console.log(response)

          this.users = response.data.users;
          console.log(this.users)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>


<style scoped>
.nav{
    background: "transparent";

}

</style>
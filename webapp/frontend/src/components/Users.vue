<template>
  <v-container>
    <div>
      <h1 class="title">Selección de usuario</h1>
    </div>
    <v-row align="center">
      
            

      <v-col>
        <v-window v-model="window" class="elevation-1" vertical>
          

          <v-list dense>
            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item v-for="n in users.length" :key="n" @click="setUser(users[n - 1])">
                
                <v-list-item-content>
                  <v-list-item-title v-text="users[n - 1].username"></v-list-item-title>
                </v-list-item-content>

              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-window>
      </v-col>
    </v-row>
    <DialogPredetProfileSelected v-model="showPredetSelected" />
  </v-container>
</template>

<script>
import DialogPredetProfileSelected from "./DialogPredetProfileSelected.vue";


export default {
  components: {
    DialogPredetProfileSelected,
  },
  props: {
    users: Array,
  },
  data: () => ({
    length: 3,
    window: 0,
    showPredetSelected: false,
    activity_types: [
      "Sedentario (nada de ejercicio / trabajo de oficina)",
      "Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)",
      "Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)",
      "Muy activo (ejercicio casi diario intenso)",
      "Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)",
    ],
    objectives: ["Perder peso", "Mantener", "Ganar peso"],
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

<style scoped>
.perfiles {
  margin-top: 1cm;
  margin: auto;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
}
</style>
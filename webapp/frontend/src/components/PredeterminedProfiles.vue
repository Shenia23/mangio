<template>
  <v-container >
      <div>
      <h1 class="title">Selección de perfil predeterminado</h1>
    </div>
    <v-row align="center">
      <v-item-group v-model="window" class="shrink mr-6" mandatory tag="v-flex">
        <v-item v-for="n in length" :key="n" v-slot="{ active, toggle }">
          <div>
            <v-btn :input-value="active" icon @click="toggle">
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </div>
        </v-item>
      </v-item-group>

      <v-col>
        <v-window v-model="window" class="elevation-1" vertical>
          <v-window-item v-for="n in length" :key="n">
            <v-card flat>
              <v-card-text>
                <v-row class="mb-4" align="center">
                  <v-avatar color="grey" class="mr-4"></v-avatar>
                  <strong class="title"> Usuario {{ n }}</strong>
                  <v-spacer></v-spacer>
                  <v-btn icon>
                    <v-icon>mdi-chevron-double-right</v-icon>
                  </v-btn>
                </v-row>

                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                  irure dolor in reprehenderit in voluptate velit esse cillum
                  dolore eu fugiat nulla pariatur. Excepteur sint occaecat
                  cupidatat non proident, sunt in culpa qui officia deserunt
                  mollit anim id est laborum.
                </p>

                

                
              </v-card-text>
            </v-card>
          </v-window-item>
        </v-window>
      </v-col>
    </v-row>
    <div>{{predetermined_profiles}}</div>
  </v-container>
</template>

<script>
export default {
  props: {
   predetermined_profiles: Array
 },
  data: () => ({
    length: 3,
    window: 0,
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
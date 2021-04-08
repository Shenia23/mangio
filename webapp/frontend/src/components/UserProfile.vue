<template>
  <div class="cdiv">
          <p class="text" style="font-size:300%">Perfil de usuario</p>
    <div class="container">
      <div class="row">
        <div class="col-sm">
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">
                {{ this.$store.getters.userdata.height }} cm
              </p>
              <div style="font-size: 145%" class="text--primary">Altura</div>
            </v-card-text>
          </v-card>

          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">{{ this.$store.getters.userdata.body_type }}</p>
              <div style="font-size: 145%" class="text--primary">
                Tipo de cuerpo
              </div>
            </v-card-text>
          </v-card>
              <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">1980</p>
              <div style="font-size: 145%" class="text--primary">
                Metabolismo basal
              </div>
            </v-card-text>
          </v-card>
        </div>
        <div class="col-sm">
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">{{ this.$store.getters.userdata.name }}</p>
              <div style="font-size: 145%" class="text--primary">Nombre</div>
            </v-card-text>
          </v-card>
              <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">{{ this.$store.getters.userdata.sex }}</p>
              <div style="font-size: 145%" class="text--primary">
                Sexo
              </div>
            </v-card-text>
          </v-card>
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">25.5%</p>
              <div style="font-size: 145%" class="text--primary">
                Índice de masa corporal
              </div>
            </v-card-text>
          </v-card>
        </div>
        <div class="col-sm">
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">{{ this.$store.getters.userdata.age }}</p>
              <div style="font-size: 145%" class="text--primary">Edad</div>
            </v-card-text>
          </v-card>
              <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">{{ this.$store.getters.userdata.weight }} kg</p>
              <div style="font-size: 145%" class="text--primary">
                Peso
              </div>
            </v-card-text>
          </v-card>
          <v-card class="mx-auto" max-width="344">
            <v-card-text>
              <p class="display-1 text--primary">24%</p>
              <div style="font-size: 145%" class="text--primary">
                Grasa vísceral
              </div>
            </v-card-text>
          </v-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.cdiv {
  margin-top: 0.5em;
  margin-bottom: 0.1em;
  background-color: white;
  margin: auto;
  width: 80%;
  border: 3px solid #96bb7c;
  padding: 10px;

  justify-content: flex-end;
  line-height: 200px;
}

.mx-auto{

  background: #8bc34a;

}
</style>
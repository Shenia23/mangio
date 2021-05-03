<template>
  <v-footer
    dark
    padless
  >
    <v-card
      flat
      tile
      class="lighten-1 white--text text-center"
    >
      <v-card-text>
       
      </v-card-text>

      <v-card-text class="white--text pt-1 footer-text">
          <b>Mangio! es una aplicación para el apoyo al seguimiento de buenos hábitos de alimentación a través de la generación de un plan de comidas saludable. Ha sido realizada para la asignatura de Laboratorio de Proyectos del Grado de Ingeniería de Tecnologías de Telecomunicación de Universidad de Vigo. </b>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong> Mangio! </strong>
         <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4 white--text"
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-text>
    </v-card>
  </v-footer>
</template>


<script>
  export default {
    data: () => ({
      icons: [
        'mdi-github',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>

<style scoped>
.lighten-1 {
  background: var(--main-green);
  width: 100%;
}
.footer-text{
  width: 90%;
  margin: auto;
}
</style>
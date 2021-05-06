<template>
  <v-row justify="center">
    <v-dialog
      v-model="show"
      persistent
      max-width="400"
    >

      <v-card>
        <v-card-title class="headline">
          Perfil seleccionado
        </v-card-title>
        <v-card-text>Pulsa <b>IR AL PLAN</b> para ver el plan de alimentación para este perfil.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
            to='/planalimentacion'
          >
            IR AL PLAN
          </v-btn>
          
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: {
     value: Boolean
  },
  computed: {
    show: {
      get () {
        return this.value
      },
      set (value) {
         this.$emit('input', value)
      }
    }
  }
}
</script>
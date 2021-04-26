<template>
  <v-row justify="center">
    <v-dialog
      v-model="show"
      persistent
      max-width="290"
    >

      <v-card>
        <v-card-title class="headline">
          Creación de usuario completada
        </v-card-title>
        <v-card-text>Pulsa <b>IR AL PLAN</b> para ver tu plan de alimentación personalizado.</v-card-text>
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
<template>
  <div class="recommendation-body"> 
    <v-card
        class="mx-auto"
        max-width="600"
        outlined
        v-for="(r, index) in rec" :key="index"
    >
        <v-list-item three-line>
        <v-list-item-content>
            <div class="overline mb-2">
            {{ r.tipo }}
            </div>
            <v-list-item-title class="heading-6 mb-1">
            {{ r.nombre }}
            </v-list-item-title>
            <v-list-item-subtitle> {{r.calorias}}kcal </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar
            tile
            size="80"
            color="grey"
        ></v-list-item-avatar>
        </v-list-item>

    </v-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Recomendacion',
  data() {
    return {
      rec: [],
    };
  },
  methods: {
    getRecomendacion() {
      const path = 'http://localhost:5000/recomendacion';
      axios.get(path)
        .then((res) => {
          this.rec = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getRecomendacion();
  },
};
</script>
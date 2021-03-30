<template>
  <div class="row recommendation-body">
    <v-col cols="12" md="4" style="margin-left:40px">
    <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
        <p></p>
        <v-title class="headline mb-2"> Recomendación para Hoy </v-title>
        <v-container>
        <v-card
        class="mx-auto"
        max-width="550"
        outlined
        v-for="(comida, index) in comidas"
        :key="index"
        >  
        <div class="d-flex flex-no-wrap justify-space-between">
        <v-list-item three-line
        >
            <v-list-item-content>
            <div class="overline mb-1">
                {{ comida }}
            </div>
            <div v-for="(r, index) in rec"
                :key="index"
            >   
                <v-list-item v-if="r.Comida==comida" class="receta">
                    <v-list class="info_receta">
                        <v-list-item-title class="body-1 mb-1" >
                        <p class="text-left font-weight-bold">
                                {{ r.Nombre }}
                            </p> 
                        </v-list-item-title>
                        <v-list-item-subtitle> 
                            <p class="text-left caption">
                                {{ r.energia }} kcal
                            </p> 
                        </v-list-item-subtitle>
                    </v-list>
                    <v-divider></v-divider>
                    <v-list-item-avatar tile size="50" color="grey"></v-list-item-avatar>
                </v-list-item>
            </div>
            </v-list-item-content>

        </v-list-item>
        </div>
        </v-card>
        </v-container>
    </v-col>

    <v-col cols="12" md=4 >
    <!-- COL 2: STATS de las comidas + EXPLICACIÓN-->
        <p class="headline mb-2"> Stats </p>
          <Doughnut></Doughnut>
        <p class="headline mb-2"> Explicación</p>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
import Doughnut from './Doughnut.vue'

export default {
  name: "Recomendacion",
  components: { Doughnut},
  data() {
 
       return {
      rec: [],
      comidas: ['desayuno','snack','comida','merienda','cena'],
    };
  },
  methods: {
    getRecomendacion() {
      const path = "http://localhost:5000/recomendacion";
      axios
        .get(path)
        .then((res) => {
          this.rec = res.data;
          console.log(res)
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
<template>
  <v-container class="pa-4 text-center">
    <v-row
      class="fill-height"
      align="center"
      justify="center"
    >
      <template v-for="(item, i) in items">
        <v-col
          :key="i"
          cols="12"
          md="4"
        >
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 14 : 2"
              :class="{ 'on-hover': hover }"
              height="450px"
            >
           <v-img
                :src="item.img"
                height="300px"
              >

                <v-card-title class="title black--text">
                  <v-row
                    class="fill-height flex-column"
                    justify="space-between"
                  >

                  </v-row>
                </v-card-title>
                 
                </v-img>
                <v-btn :class="{ 'show-btns': hover }"
                        :color="transparent"
                        v-on:click.stop="action2"> {{ item.title }}

                </v-btn>

            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>




<script>
  export default {
    data: () => ({
      items: [
        {
          title: 'Ectomorfo',
          img: require('../assets/ectomorph.jpg'),
        },
        {
          title: 'Mesomorfo',
          img: require('../assets/mesomorph.jpg'),
        },
        {
          title: 'Endomorfo',
          img: require('../assets/endomorph.jpg'),
        },
      ],
      transparent: 'rgba(255, 255, 255, 0)',
    }),
  }
</script>

<style scoped>
.v-card {
  transition: opacity .6s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.8;
 }

.show-btns {
  color: rgb(0, 0, 0) !important;
}
.image_button{
    opacity: 1;
    color: rgb(0, 0, 0) !important;
}
</style>
<template type="default">
  <v-container class="pa-4 text-center">
    <v-row class="fill-height" align="center" justify="center">
      <template v-for="(item, i) in items">
        <v-col :key="i" cols="12" md="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 14 : 2"
              :class="{ 'on-hover': hover }"
              :id="item.title"
              @click="change_opacity(item.title)"
              height="375px"
            >
              <v-img :src="item.img" size="100px">
                <v-card-title class="title black--text">
                  <v-row
                    class="fill-height flex-column"
                    justify="space-between"
                  >
                  </v-row>
                </v-card-title>
              </v-img>
              <v-card-text :class="{ 'show-btns': hover }"
                :color="transparent">{{ item.title }}</v-card-text>
              
            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>




<script>
export default {
  props: {
    body_type: String,
  },
  data: () => ({
    items: [
      {
        title: "Ectomorfo",
        img: require("../assets/ectomorph.jpg"),
      },
      {
        title: "Mesomorfo",
        img: require("../assets/mesomorph.jpg"),
      },
      {
        title: "Endomorfo",
        img: require("../assets/endomorph.jpg"),
      },
    ],
    transparent: "rgba(255, 255, 255, 0)",
  }),
  methods: {
    change_opacity: function (id) {
      var ids = ["Ectomorfo", "Endomorfo", "Mesomorfo"];
      var vcards = document.getElementsByTagName("on-hover");
      for (var i = 0; i < ids.length; i++) {
        if (ids[i] == id) {
          this.$emit("changeBodyType", id);
          document.getElementById(id).style.opacity = 1;
        } else {
          document.getElementById(ids[i]).style.opacity = 0.7;
        }
      }
    },
  },
};
</script>

<style scoped>
.v-card {
  transition: opacity 0.6s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.6;
}

.show-btns {
  color: rgb(0, 0, 0) !important;
}
.image_button {
  opacity: 1;
  color: rgb(0, 0, 0) !important;
}
</style>
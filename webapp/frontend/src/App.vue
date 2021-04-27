
<template >

  <v-app  >
    <v-toolbar color="green" class="vToolbar" app>
      <span class='hidden-sm-and-up'>
        <v-toolbar-side-icon @click='sidebar = !sidebar'> </v-toolbar-side-icon>
      </span>
      <v-toolbar-title class="vTitle" >
        <router-link to='/' tag='span' >
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class='hidden-xs-only'>
        <v-btn color="green" :depressed="true" v-for='item in menuItems' :key='item.title' :to='item.path'>
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      
      <router-view></router-view>
      
    </v-content>

    <Footer class="footer"/>
  </v-app>

</template>

<script>
import Footer from './components/Footer.vue'
export default {
  name: 'app',
  components: { Footer },

  data () {
    return {
      appTitle: 'Mangio!',
      sidebar: false,
      menuItems: [
        { title: 'Nuevo usuario', path: '/nuevoUsuario', icon: 'fiber_new' },
        { title: 'Plan de alimentación', path: '/planalimentacion', icon: 'fastfood' },
        { title: 'Nuevas recetas', path: '/nuevasrecetas', icon: 'add_circle' }
      ]
    }
  }
}
</script>


<style>
.footer{
  margin-top: 100px;
}

.vTitle{
font-family: "Gill Sans";
font-size: 300%;
    cursor: pointer;

}

.vToolbar{
  color:rgb(51, 161, 51);
   max-height: 10%;
   width: 100%;

}

#app {
  font-family: "Bodoni MT", Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #fffbf0;

}
</style>


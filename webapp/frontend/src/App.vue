
<template >
  <v-app  >
    <v-toolbar color="light-green" class="vToolbar" app>
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
        <v-btn color="light-green" depressed='true' v-for='item in menuItems' :key='item.title' :to='item.path'>
          <v-icon left dark>{{ item.icon }}</v-icon>
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      
      <router-view></router-view>
      
    </v-content>
    
  </v-app>

</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      appTitle: 'Mangio!',
      sidebar: false,
      menuItems: [
        { title: 'Perfiles prediseñados', path: '/perfiles', icon: 'folder_shared' },
        { title: 'Nuevo usuario', path: '/nuevoUsuario', icon: 'fiber_new' },
        { title: 'Plan de alimentación', path: '/planalimentacion', icon: 'fastfood' },
        { title: 'Perfil de usuario', path: '/perfilusuario', icon: 'account_circle' },
        { title: 'Nuevas recetas', path: '/nuevasrecetas', icon: 'add_circle' }
      ]
    }
  }
}
</script>


<style>


.vTitle{
font-family: "Gill Sans";
font-size: 300%;
    cursor: pointer;

}

.vToolbar{
  color: rgb(141, 254, 141);
   max-height: 10%;

}

#app {
   font-family: "Bodoni MT", Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #ffffff;

}
</style>


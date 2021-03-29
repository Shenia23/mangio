
<template >

  <v-app >
    


    <v-toolbar max-height=9% app class="toolbar">
      
      <v-toolbar-title >
        <router-link to='/' tag='span' style='cursor: pointer'>
          <h1> {{appTitle}}</h1>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class='hidden-xs-only'>
        <v-btn flat v-for='item in menuItems' :key='item.title' :to='item.path'>
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
      height: '1px',
      width: '100%',
      menuItems: [
        { title: 'Nuevo usuario', path: '/nuevoUsuario', icon: 'logo.png' },
        { title: 'Plan de alimentación', path: '/planalimentacion', icon: 'face' },
        { title: 'Nuevas recetas', path: '/nuevasrecetas', icon: 'lock_open' }
      ]
    }
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #137d2c;
}

</style>


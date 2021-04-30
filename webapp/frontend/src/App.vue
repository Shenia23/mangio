
<template >

  <v-app>
    <v-toolbar color="var(--main-green)" class="vToolbar" app>
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
        <v-btn class="items" :depressed="true" v-for='item in menuItems' :key='item.title' :to='item.path'>
          <v-icon size=30 color="white" left dark class="itemIcon">{{ item.icon }}</v-icon>
          <p class="itemTitle" style="font-weight:bold;" > {{ item.title }} </p>
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


@import url('https://fonts.googleapis.com/css?family=Cairo');

:root {
    --main-green:#87c441;
    --main-orange: #f9e17a;
    --main-darkgreen: #4caf50;
}


.footer{
  margin-top: 100px;
}

.vTitle{
font-family: 'Cairo', sans-serif;
font-weight: 'bold';
color: white;
text-shadow: 1px 1px 2px #000000;
font-size: 300%;
    cursor: pointer;

}


.itemTitle{
  font-family: 'Cairo', sans-serif;
  color:white;
  margin-top:5%;
  font-size:150%
  
}


.items{

   font-size:200%;
   background:var(--main-green)!important

}

.vToolbar{
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

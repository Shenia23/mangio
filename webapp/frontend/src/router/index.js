
import Vue from 'vue'
import Router from 'vue-router'
const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '*', component: 'NotFound' },
  {path: '/nuevousuario', component: 'About'},
  {path: '/perfilusuario', component: 'About'},
  {path: '/planalimentacion', component: 'About'},
  {path: '/nuevasrecetas', component: 'About'},
  {path: '/perfiles', component: 'About'}

]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})

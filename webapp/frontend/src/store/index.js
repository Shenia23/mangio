import Vue from "vue";
import Vuex from "vuex";
 
Vue.use(Vuex);
 
export default new Vuex.Store({
 state: {
     user: {
         userdata: {
            'name': 'Francesca', // este sería el usuario sacado del form o de una request a flask
            'age': 23, 
            'sex': 'Mujer', 
            'weight': 65, 
            'height': 165, 
            'body_type': 'Mesomorfo', 
            'activity_level': 3, 
            'objective': 0, 
            'tdee': 2762.46711,
            'water_intake': 2171.9684256
            // cambiar por Object 
         }
     }
 },
 getters: {
     username: state => {
         return state.user.userdata.name
     },
     userdata: state => {
         return state.user.userdata
     }
 },
 mutations: {
     setUserData(state, payload) {
         state.user.userdata = payload.userdata
     }
 },
 actions: {}
});
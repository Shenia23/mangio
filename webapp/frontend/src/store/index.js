import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: {
            userdata: {
                'username': 'francescademo',
                'name': 'Francesca', // este sería el usuario sacado del form o de una request a flask
                'age': 23,
                'sex': 'Mujer',
                'weight': 65,
                'height': 165,
                'body_type': 'Mesomorfo',
                'activity_level': 3,
                'objective': 1,
                'tdee': 2762.46711,
                'water_intake': 2171.9684256,
                'macro_objectives': {
                    'energia': 2500,
                    'grasa': 83,
                    'proteina': 187,
                    'carbohidratos': 250
                }
            },
            
        }
    },
    getters: {
        username: state => {
            return state.user.userdata.username
        },
        userdata: state => {
            return state.user.userdata
        },
        objectives: state =>{
            return state.user.userdata['macro_objectives']
        },
        waterIntake: state =>{
            return state.user.userdata['water_intake']
        },
        tdee: state =>{
            return Math.round(state.user.userdata['tdee'])
        },
        cals_obj: state =>{
            switch(state.user.userdata
                ['objective']){
                   case 0: return Math.round(state.user.userdata['tdee']) - 500
                   case 1: return Math.round(state.user.userdata['tdee']) 
                   case 2: return Math.round(state.user.userdata['tdee']) + 500
               }
        },
        objetivo: state =>{
           switch(state.user.userdata
            ['objective']){
               case 0: return "perder peso"
               case 1: return "mantenerte en tu peso"
               case 2: return "ganar peso"
           }
        },
    },
    mutations: {
        setUserData(state, payload) {
            console.log("hola")
            state.user.userdata = payload.userdata
        },
        setObjectives(state, payload) {
            state.user.userdata.objectives = payload.objectives
        }
    },
    actions: {}
});
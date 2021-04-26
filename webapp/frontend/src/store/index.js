import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: {
            userdata: {
                "username": "francescademo",
                "name": "Francesca",
                "sex": "Mujer",
                "age": 43,
                "height": 170,
                "body_type": "Ectomorfo",
                "activity_level": 2,
                "liked_ingredients": [
                    "huevo"
                ],
                "disliked_ingredients": null,
                "objective": 3,
                "using_scale": false,
                "weight": 65,
                "bmi": 22.49134948096886,
                "bmr": 1390.1270000000002,
                "tdee": 1911.4246250000003,
                "water_intake": 1834.9676400000003,
                "macro_objectives": {
                    "grasa": 42.47610277777778,
                    "proteina": 143.35684687500003,
                    "carbohidratos": 238.92807812500004,
                    "energia": 1911.4246250000003
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
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
        "objective": 0,
        "using_scale": false,
        "weight": 65,
        "alpha": 0.70,
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
    objectives: state => {
      return state.user.userdata['macro_objectives']
    },
    waterIntake: state => {
      return state.user.userdata['water_intake']
    },
    weight: state => {
      return state.user.userdata['weight']
    },
    height: state => {
      return state.user.userdata['height']
    },
    bmi: state => {//anxo
      return Math.round(state.user.userdata['bmi'])
    },
    bmr: state => {//bmi
      return state.user.userdata['bmr']
    },
    bmrRound: state => {//bmi
      return Math.round(state.user.userdata['bmr'])
    },
    tdee: state => {
      return Math.round(state.user.userdata['tdee'])
    },
    cals_obj: state => {
      switch (state.user.userdata
      ['objective']) {
        case 0: return Math.round(state.user.userdata['tdee']) - 500
        case 1: return Math.round(state.user.userdata['tdee'])
        case 2: return Math.round(state.user.userdata['tdee']) + 500
      }
    },
    nivel_actividad: state => {
      switch (state.user.userdata['activity_level']) {

        case 1: return "1. Sedentario (nada de ejercicio / trabajo de oficina)"
        case 2: return "2. Ligeramente activo (ejercicio ligero de 1 a 3 días semanales)"
        case 3: return "3. Moderadamente activo (ejercicio moderado de 3 a 5 días semanales)"
        case 4: return "4. Muy activo (ejercicio casi diario intenso)"
        case 5: return "5. Extremadamente activo (ejercio diario muy intenso, 2 entrenamientos diarios)"
      }
    },
    objetivo: state => {
      switch (state.user.userdata
      ['objective']) {
        case 0: return "perder peso"
        case 1: return "mantenerte en tu peso"
        case 2: return "ganar peso"
      }
    },
    objective: state => {
      switch (state.user.userdata
      ['objective']) {
        case 0: return "Perder peso"
        case 1: return "Mantener"
        case 2: return "Ganar peso"
      }
    },
    bmiText: state => {//anxo
      var auxbmi
      var bmi = state.user.userdata['bmi']
      if (bmi < 18.5) return "esta por debajo de su peso ideal (Insuficiencia ponderal)"
      else if (bmi > 18.5 && bmi < 24.9) return "esta dentro de su peso ideal (normopeso)"
      else if (bmi > 25 && bmi < 26.9) return "esta un poco por encima de su peso (Sobrepeso grado I)"
      else if (bmi > 27 && bmi < 29.9) return "esta bastante por encima de su peso (Sobrepeso grado II (preobesidad))"
      else if (bmi > 30 && bmi < 34.9) return "está muy por encima de su peso (Obesidad de tipo I)"
      else if (bmi > 35 && bmi < 39.9) return "está muy por encima de su peso (Obesidad de tipo II)"
      else if (bmi > 40) return "está muy por encima de su peso (Obesidad de tipo III (mórbida))"
      
    },
    tdeeBmr: state => {//anxo

      return state.user.userdata['tdee'].toFixed(2) - state.user.userdata['bmr'].toFixed(2)
    },

    tdeeText: state => {//anxo

      var factor = state.user.userdata
        ['activity_level']


      switch (factor) {
        case 0: return "la escasa actividad"
        case 1: return "la escasa actividad"
        case 2: return "la actividad"
        case 3: return "la gran actividad"
        case 4: return "la enorme cantidad de actividad"

      }
    },
    macroText: state => {//anxo

      switch (state.user.userdata
      ['objective']) {
        case 0: return "Cualquier tipo de dieta en la que se consuma menos energía de la que se utiliza dará lugar a la pérdida de peso. Una dieta baja en carbohidratos y rica en proteínas puede darte una mayor sensación de saciedad. Además, las proteínas son importantes para la construcción de los músculos. Comer suficientes proteínas durante la pérdida de peso puede ayudar a mantener más masa muscular. Debido a la reducción de hidratos de carbono en tu dieta en comparación a una dieta de mantenimiento del peso, se han aumentado la cantidad de grasas que debes ingerir, pero recuerda que estas grasas, deben ser saludables (insaturadas), las que se encuentran en los frutos secos, el pescado y frutas como el aguacate. Recuerda que el cardio ayuda en la perdida de peso, pero también los ejercicios de musculación."
        case 1: return "Una dieta saludable que no pretende ni adelgazar ni engordar, se basa en ingerir la misma energía que consume tu cuerpo. Manteniendo una proporción similar entre proteínas y grasas se alimentará a tus músculos adecuadamente y ayudará en la asimilación de vitaminas de tu organismo y un mayor porcentaje de hidratos de carbono te aportará la energía necesaria para afrontar el día a día."
        case 2: return "Para ganar masa muscular aumentamos la ingesta de carbohidratos en comparación con una dieta de mantenimiento. Ten en cuenta que para ganar masa muscular debes acompañar la alimentación de ejercicio físico. Recuerda, a no ser que tiendas a engordar debido a tu metabolismo, necesitarás algo más que un incremento en las calorías que ingieres. Reduce el cardio en tu rutina y aumenta los ejercicios de musculación. Además si haces ejercicio físico es importante ingerir proteínas ya que es el componente principal de los músculos, con lo que reducimos el porcentaje de grasas en la dieta. Aunque no del todo ya que son muy importantes en el metabolismo, contribuyendo en la asimilación de vitaminas de tu organismo y funcionando como una gran reserva de energía."

      }
    },
    tdeeRec: state => {//anxo
      switch (state.user.userdata
      ['tdee'].toFixed(2)) {
        case 0: return "Te recomiendo comenzar una rutina de ejercicio físico, que te ayudará en el control del peso y mejorará tu calidad de vida."
        case 1: return "Pese a que ya haces ejercicio, quizá no lo suficiente, te recomiendo aumentar la frecuencia o intensidad de los entrenamientos."
        case 2: return "Recuerda continuar con tu rutina de ejercicio semanal. El ejercicio es fundamental para tener una calidad de vida saludable."
        case 3: return "Con la cantidad de ejercicio que haces, intenta no saltarte demasiadas comidas, ya que es muy importante no descuidar la alimentación."
        case 4: return "Con la cantidad de ejercicio que haces, intenta no saltarte demasiadas comidas, ya que es muy importante no descuidar la alimentación."
      }
    },
    



  },
  mutations: {
    setUserData(state, payload) {
      state.user.userdata = payload.userdata
    },
    setObjectives(state, payload) {
      state.user.userdata.objectives = payload.objectives
    }
  },
  actions: {}
});

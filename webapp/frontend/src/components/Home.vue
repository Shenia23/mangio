
<template>
  <div>
    <head>
      <meta charset="utf-8" />
      <link rel="icon" type="image/png" href="../assets/img/favicon.ico" />

      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
      <div class="top-left">
        <title>MANGIO</title>
      </div>
      <meta
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
        name="viewport"
      />
      <meta name="viewport" content="width=device-width" />
    </head>

    <body class="landing-page landing-page2">
      <div class="wrapper">
        <div
          class="parallax filter-gradient light-green"
          data-color="light-green"
        >
          <div class="container">
            <div class="row">
              <div class="col-md-7 hidden-xs">
                <div class="parallax-image">
                  <img src="../assets/img/showcases/showcase-2/mac3.png" />
                </div>
              </div>
              <div class="col-md-5">
                <div class="description text-center">
                  <img contain :src="logo" height="100px" />
                  <br />
                  <h2>Tu app nutricional</h2>
                  <div class="buttons">
                    <a
                      href="https://github.com/Shenia23/mangio"
                      class="btn"
                      style="color: #3e4243"
                    >
                      <i class="fa fa-github" style="color: #3e4243"></i>
                      Explicación
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="section section-gray section-clients">
          <div class="container text-center">
            <h4 class="header-text">Tecnologías</h4>
            <p>
              Mangio! está construída con cariño, empleando las siguientes
              tecnologías:<br />
            </p>
            <div class="logos">
              <ul class="list-unstyled">
                <li><img src="../assets/img/logos/flask.png" /></li>
                <li><img src="../assets/img/logos/vuejs.png" /></li>
                <li><img src="../assets/img/logos/ble.png" /></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="section section-presentation" >
          <div class="container">
            <div class="row">
              <div class="col-md-5 hidden-xs">
                <div class="description">
                  <h4 class="header-text">Nuevos usuarios</h4>
                  <p>
                    A través del formulario de registro y del
                    <b>cuestionario de preferencias nutricionales</b>
                    dispondremos de toda la información necesaria para crear un
                    plan de alimentación personalizado, que se adapte a tus
                    necesidades y gustos.
                  </p>

                  <p>
                    Además, si deseas probar el funcionamiento sin registrarte,
                    puedes hacerlo sin problemas a través de nuestros
                    <b>perfiles prediseñados</b>, que hemos seleccionado
                    cuidadosamente para mostrar el funcionamiento de la
                    aplicación
                  </p>
                </div>
              </div>
              <div class="col-md-6">
                <img
                  src="../assets/img/showcases/showcase-2/mac_2_cuestionario.jpeg"
                  style="margin-top: -50px"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="section section-demo">
          <div class="container">
            <div class="row">
              <div class="col-md-6">
                <div class="demo-image">
                  <img
                    src="../assets/img/showcases/showcase-2/mac1.png"
                    alt=""
                  />
                </div>
              </div>
              <div class="col-md-5 col-md-offset-1">
                <h4 class="header-text">Plan de alimentación</h4>
                <p>
                  Una vez seleccionado el perfil de usuario, es posible acceder
                  a las recomendaciones personalizadas en la pestaña del
                  <b>Plan de Alimentación</b>.
                </p>

                <p>
                  Por una parte están las recomendaciones de ese día, ordenadas
                  por el tipo de comida (desayuno, merienda, cena…). Es posible
                  realizar acciones sobre ellas, como seleccionar otra
                  recomendación distinta individual o globalmente. Por otro lado
                  aparecen gráficas con la información global de la
                  recomendación y un pequeño texto explicativo de los parámetros
                  tomados por el recomendador.
                </p>
              </div>
            </div>
            <br />
            <div class="row">
              <div class="col-md-5">
                <h4 class="header-text">Nuevas recetas</h4>
                <p>
                  En la línea de incorporar de alguna manera técnicas de
                  <b>Crowdsourcing</b> en la app, se ha incorporado la
                  posibilidad de añadir Nuevas Recetas a la base de datos, así
                  estas podrán ser utilizadas por todos los usuarios y
                  permitirán mejorar nuestras bases de datos.
                </p>
              </div>
              <div class="col-md-6 col-md-offset-1">
                <div class="demo-image">
                  <img
                    src="../assets/img/showcases/showcase-2/ipad_creacion_recetas.png"
                    alt=""
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="section section-features">
          <div class="container">
            <h4 class="header-text text-center">Features</h4>
            <div class="row">
              <div class="col-md-3">
                <div class="card card-blue">
                  <div class="icon">
                    <v-icon right dark> mdi-chart-bar </v-icon>
                  </div>
                  <div class="text">
                    <h4>Estadísticas</h4>
                    <p>
                      Estas gráficas muestran el % de cada macronutriente en tu
                      plan de alimentación, una comparación entre los
                      macronutrientes propuestos y la cantidad ideal, y las
                      kilocalorías que representa cada comida del día.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card card-blue">
                  <div class="icon">
                    <v-icon right dark> mdi-heart </v-icon>
                  </div>

                  <h4>Introduce tus gustos</h4>
                  <p>
                    A través de un cuestionario de preferencias con estilo
                    Tinder, podremos determinar las recetas que mejor se adaptan
                    para ti, sin olvidar tus gustos.
                  </p>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card card-blue">
                  <div class="icon">
                    <v-icon right dark> mdi-bluetooth </v-icon>
                  </div>

                  <h4>Conecta tu báscula inteligente</h4>
                  <p>
                    Para obtener una medición más precisa, puedes conectar tu
                    báscula inteligente (Xiaomi Mi Body Composition Scale 2) y
                    recogeremos sus datos para ofrecerte las mejores
                    recomendaciones
                  </p>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card card-blue">
                  <div class="icon">
                    <v-icon right dark> mdi-clock-fast </v-icon>
                  </div>
                  <h4>Velocidad</h4>
                  <p>
                    Analizamos millones de combinaciones para ofrecer aquellas
                    que mejor se adapten a ti en cuestión de segundos.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </body>
    <script
      src="../assets/js/jquery-1.10.2.js"
      type="application/javascript"
    ></script>
    <script
      src="../assets/js/jquery-ui-1.10.4.custom.min.js"
      type="application/javascript"
    ></script>
    <script
      src="../assets/js/bootstrap.js"
      type="application/javascript"
    ></script>
    <script
      src="../assets/js/awesome-landing-page.js"
      type="application/javascript"
    ></script>
  </div>
</template>



<script>
import axios from "axios";
export default {
  data() {
    return {
      randomNumber: 0,
      logo: require('./assets/img/logos/logo-web.png'),
    };
  },
  methods: {
    getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },
    getRandom() {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`;
      axios
        .get(path)
        .then((response) => {
          this.randomNumber = response.data.randomNumber;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getRandom();
  },
};
</script>

<style scoped>

  @import 'https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap-grid.min.css';
  @import "../assets/css/landing-page.css";
  @import "http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css";
  @import "../assets/css/pe-icon-7-stroke.css";
  @import "http://fonts.googleapis.com/css?family=Open+Sans:300italic,400,300";

  
  .landing-page{
      background: #ffffff;
  }
  .btn {
    background-color: #ebebeb;
    color: grey;
    padding: 10px;
    font-size: 180%;
    height: 180%;
    width: 80%;
  }
  .btn:hover {
    background: rgb(182, 182, 182);
  }
  
</style>


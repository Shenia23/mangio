<template>
  <div class="recommendation-body" id="main-row">
    <v-container>
      <div>
        <v-row id="title-row" style="margin: 35px">
          <h1 class="tituloRC">Creación de recetas</h1>
        </v-row>
      </div>
      <div class="row">
        <v-col cols="12" md="6">
          <!-- COL 1: cards de RECOMENDACIONES y RECETAS-->
          <v-form ref="form" v-model="valid" lazy-validation class="formulario">

            <v-autocomplete
              v-model="selected_ingredient"
              :items="ingredients"
              dense
              filled
              label="Escoge un ingrediente"
            ></v-autocomplete>

            <v-text-field
              v-model="selected_quantity"
              label="Cantidad"
              required
              type="number"
              style="margin-bottom: 20px"
            ></v-text-field>

            <v-autocomplete
              v-model="selected_unit"
              :items="units"
              dense
              filled
              label="Escoge la unidad"
            ></v-autocomplete>

            <div class="buttonHolder">
             <v-btn text>
              Añadir ingrediente
            </v-btn>
            <v-btn
            
              color="green"
              fab
              dark
              @click="
                addIngredient(
                  selected_ingredient,
                  selected_quantity,
                  selected_unit
                )
              "
            >
            
              <v-icon> add_circle_outline</v-icon>
            </v-btn>
            </div>

              <!-- results of <div v-for="item in list"></div>  -->
              <div class="buttonHolder">
                <img width="40%" height="40%" src="../assets/colaboza.png" />
              </div>
              <div>
                <h4 class="coltext">
                  Tu ayuda para hacer crecer a Mangio! significa mucho para
                  nosotros.
                </h4>
              </div>

            <v-text-field
              v-model="name"
              :counter="40"
              label="Nombre de la receta"
              required
              style="margin-bottom: 3px"
            ></v-text-field>

              <v-text-field
              v-model="comensales"
              :counter="40"
              label="Número de comensales"
              required
              style="margin-bottom: 3px"
            ></v-text-field>

            <div class="buttonHolder">
             <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="
                createRecipe(
                    name,
                    comensales
                )
              
              "
            >
              CREACIÓN DE NUEVA RECETA
            </v-btn>
          </div>

           
          </v-form>
        </v-col>

        <v-col cols="12" md="6" class="stats">
          <!-- COL 2: STATS de las comidas + EXPLICACIÓN-->
          <v-simple-table class="table">
            <template v-slot:default>
              <thead>
                <tr>
                  <th style="font-size: 40%; color:black" class="text-left">Ingrediente</th>
                  <th style="font-size: 40%; color:black" class="text-left">Cantidad</th>
                  <th style="font-size: 40%; color:black" class="text-left">Unidad</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in recipe_ingredients" :key="item.name">
                  <td class="text-left">{{ item.name }}</td>
                  <td class="text-left">{{ item.quantity }}</td>
                  <td class="text-left">{{ item.unit }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </div>
    </v-container>
  </div>
</template>


<style scoped>
.column_wrapper {
  column-count: 2;
}

.buttonHolder{ text-align: center; }


.coltext {
  font-size: 15px;
  margin-top: 1px;
  margin-bottom: 8%;
  margin-top: -8%;
  color:var(--main-darkgreen);


}

.formulario {
  font-family: "Cairo", sans-serif;
  margin-top: 1cm;
  background-color: white;
  margin: auto;
  width: 95%;
  border: 3px solid var(--main-green);
  padding: 30px;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
  line-height: 50px;

}

.text-left {
  font-size: 402px;
}

.tituloRC {
  font-family: "Cairo", sans-serif;
  font-weight:bold;
  margin-top: 1cm;
  margin-bottom: 5cm;
  background-color: white;
  margin: auto;
  width: 95%;
  border: 3px solid var(--main-green);
  padding: 20px;
  border-radius: 10px;
  justify-content: flex-end;
  text-align: center;
  line-height: 30px;
}

.stats {
  font-family: "Cairo", sans-serif;
  margin-top: 1cm;
  background-color: white;
  margin: auto;
  width: 95%;
  height: 140%;
  border: 3px solid var(--main-green);
  padding: 45px;
  border-radius: 25px;
  justify-content: flex-end;
  text-align: left;
}

input {
  height: 20px;
  flex: 0 0 200px;
  margin-left: 10px;
}
.inbtn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
}

.table {
  border: 3px solid var(--main-green);
  width: 95%;
  margin: auto;
  margin-top: 0px;
  font-size: 50px;

  justify-content: flex-end;
}
</style>



<script>
import BodyType from "./BodyType.vue";
import Ingredients from "./Ingredients.vue";
import axios from "axios";

export default {
  components: { BodyType, Ingredients },
  data: () => ({
    valid: true,
    recipe_name: "",
    selected_ingredient: "",
    selected_unit: "",
    selected_quantity: "",
    comensals:"",
    ingredients_list: [],
    recipe_ingredients: ["", "", "", "", "", "", "", "", "", "", "", "","",""],
    ingredients: [
      "Arroz con leche",
      "Batido de chocolate",
      "Batido de fresa",
      "Batido de soja",
      "Batido fermentado de soja",
      "Batido de chocolate, bajo en calorías",
      "Batido de fresa bajo en calorías",
      "Bebida de soja",
      "Crema catalana",
      "Cremoso san millan",
      "Cuajada",
      "Flan de huevo",
      "Helado de chocolate",
      "Helado de fresa",
      "Helado de nata",
      "Kefir",
      "Leche condensada, entera, con azúcar",
      "Leche de almendra",
      "Leche de cabra",
      "Leche de coco",
      "Leche de oveja",
      "Leche de vaca, desnatada, condensada, con azúcar",
      "Leche de vaca, entera",
      "Leche en polvo, semidesnatada",
      "Leche fermentada, bifidobacterium, entera, natural",
      "Leche materna",
      "Leche merengada",
      "Leche",
      "Leche, semidesnatada, pasteurizada",
      "Mousse de chocolate",
      "Mousse de queso fresco, con frutas",
      "Mousse de queso fresco, desnatado, azucarado",
      "Mousse de queso fresco, desnatado, con frutas",
      "Mousse de yogur, con frutas",
      "Mousse de yogur, natural",
      "Nata",
      "Natillas sabor vainilla",
      "Petit líquido, sabor fresa",
      "Petit suïsse, cereales y fruta",
      "Petit suisse, chocolate",
      "Petit suisse, fresa",
      "Petit Suisse, natural azucarado",
      "Preparado lácteo con omega 3",
      "Queso afuega'l pitu",
      "Queso ahumado de aliva",
      "Queso azul",
      "Queso brie",
      "Queso cabra, curado",
      "Queso cabrales",
      "Queso Camembert 20-30% MG/ES",
      "Queso camembert 60% mg/es",
      "Queso cantabria",
      "Queso casín",
      "Queso Castellano",
      "Queso cebreiro",
      "Queso Cheddar",
      "Queso curado, genérico",
      "Queso de aracena",
      "Queso de arzúa",
      "Queso de bola",
      "Queso de cádiz",
      "Queso de Castilla-La Mancha, oveja y cabra",
      "Queso de Castilla-La Mancha, oveja, vaca y cabra",
      "Queso de castilla-león, oveja y vaca",
      "Queso de murcia, al vino",
      "Queso de tenerife",
      "Queso de tiétar",
      "Queso edam",
      "Queso emmental",
      "Queso en porciones",
      "Queso flor de guía",
      "Queso fresco",
      "Queso fresco, cabra",
      "Queso fresco, desnatado, con frutas",
      "Queso fundido, extragraso (>60% MG/ES)",
      "Queso gata-hurdes",
      "Queso gaztazarra",
      "Queso",
      "Queso grazalema",
      "Queso Gruyer",
      "Queso herreño",
      "Queso Ibores",
      "Queso Mahón",
      "Queso majorero",
      "Queso manchego",
      "Queso manchego, en aceite",
      "Queso mozzarella",
      "Queso munster",
      "Queso para untar",
      "Queso para untar, con finas hierbas",
      "Queso para untar, con salmón",
      "Queso para untar, natural, bajo en calorías",
      "Queso parmesano",
      "Queso pasiego",
      "Queso pedroches",
      "Queso peñamellera",
      "Queso picón",
      "Queso porrúa",
      "Queso Raclette",
      "Queso rallado, genérico",
      "Queso roquefort",
      "Queso San Simón",
      "Queso semicurado, genérico",
      "Queso serrat",
      "Queso servilleta",
      "Queso Tetilla",
      "Queso tierno, genérico",
      "Queso torta del casar",
      "Queso tupí",
      "Queso Zamorano",
      "Requesón",
      "Yogur griego",
      'Yogur líquido, "tipo actimel"',
      "Yogur líquido, aromatizado sabor s/e",
      "Yogur líquido, con frutas s/e",
      "Yogur líquido, entero, con cereales",
      "Yogur líquido, natural, azucarado",
      "Yogur, búlgaro",
      "Yogur, desnatado, aromatizado sabor s/e",
      "Yogur, desnatado, con cereales",
      "Yogur, desnatado, con cereales, manzana y ciruela",
      "Yogur, desnatado, con cereza y frambuesa",
      "Yogur, desnatado, con ciruela, albaricoque y fibra",
      "Yogur, desnatado, con fresa, grosella y fibra",
      "Yogur, desnatado, con frutas",
      "Yogur, desnatado, con frutas del bosque",
      "Yogur, desnatado, con frutas tropicales",
      "Yogur, desnatado, con manzana",
      "Yogur, desnatado, con melocotón y maracuyá",
      "Yogur, desnatado, con melocotón, frambuesa y fibra",
      "Yogur, desnatado, con piña y pomelo",
      "Yogur",
      "Yogur, desnatado, sabor natural, azucarado",
      "Yogur, desnatado, sabor vainilla",
      "Yogur, enriquecido, con frutas",
      "Yogur, enriquecido, natural",
      "Yogur, enriquecido, natural, azucarado",
      "Yogur, enriquecido, natural, con nata",
      "Yogur, enriquecido, sabor, s/e",
      "Yogur, entero, con cereales y fresas",
      "Yogur, entero, con fresas",
      "Yogur, entero, con frutas del bosque",
      "Yogur, líquido, desnatado, natural",
      "Yogur, líquido, entero, con fresas",
      "Yogur, líquido, entero, con frutas",
      "Yogur, líquido, entero, sabor fresa",
      "Yogur, líquido, entero, sabor fresa y plátano",
      "Yogur, líquido, entero, sabor frutas del bosque",
      "Yogur, líquido, entero, sabor piña y coco",
      "Huevo de codorniz",
      "Huevo",
      "Huevo de gallina, clara, cruda",
      "Huevo de gallina, escalfado",
      "Huevo de gallina, frito",
      "Huevo de gallina, hervido, duro",
      "Huevo de gallina, pasado por agua",
      "Huevo de gallina, revuelto, con mantequilla",
      "Huevo de gallina, yema, cruda",
      "Huevo de gallina, yema, desecada",
      "Huevo de pato, crudo",
      "Huevo de pavo, entero, crudo",
      "Tortilla, a la francesa",
      "Avestruz, solomillo, crudo",
      "Bacón, ahumado, a la parrilla",
      "Bacon, crudo, con grasa separable",
      "Butifarra",
      "Cabrito, parte s/e, crudo, con grasa separable",
      "Callos de ternera",
      "Carne picada",
      "Cecina",
      "Cerdo, chuleta, crudo",
      "Cerdo, costilla, crudo",
      "Cerdo, lomo, asado",
      "Cerdo, lomo, crudo",
      "Cerdo, panceta, cruda",
      "Cerdo",
      "Cerdo, pierna, cruda, con grasa separable",
      "Cerdo, solomillo, asado",
      "Cerdo, solomillo, crudo",
      "Chistorra",
      "Choped pork",
      "Chorizo",
      "Ciervo, parte s/e, crudo, con grasa separable",
      "Conejo",
      "Conejo, entero, estofado",
      "Corazón de cordero, crudo",
      "Corazón de pollo, crudo",
      "Corazon de vaca, crudo",
      "Corazón, de cerdo, crudo",
      "Corazón, de vaca/buey, cocido",
      "Corazón, de vaca/buey, crudo",
      "Cordero, costilla, crudo",
      "Cordero, parte sin especificar",
      "Cordero, pierna, con grasa, asada",
      "Croquetas de pollo",
      "Foie gras",
      "Fuet",
      "Gallina",
      "Higado de pollo, crudo",
      "Hígado, de cerdo, crudo",
      "Hígado, de vaca/buey, crudo",
      "Jamón asado",
      "Jamón cocido",
      "Jamón cocido, enlatado",
      "Jamón ibérico de bellota",
      "Jamón ibérico de cebo",
      "Jamón serrano",
      "Lacón",
      "Lengua de cerdo, cruda",
      "Lengua de cordero, cruda",
      "Lengua, de buey, cruda",
      "Lengua, de ternera, cruda",
      "Liebre",
      "Lomo embuchado",
      "Longaniza",
      "Molleja de cordero",
      "Morcilla",
      "Morcilla, frita",
      "Mortadela",
      "Oca",
      "Panceta, frita",
      "Pate de higado de cerdo, 30% de grasa",
      "Paté de pimienta",
      "Pato, entero, asado",
      "Pato",
      "Pavo, crudo",
      "Pavo",
      "Pavo, fiambre, bajo en grasa",
      "Pavo, muslo, con piel, crudo",
      "Pavo, pechuga, con piel, crudo",
      "Pechuga de pavo",
      "Perdiz, cruda",
      "Pichón, sin piel, asado",
      "Pollo empanado, frito",
      "Pollo, ala, con piel, cruda",
      "Pollo, entero, con piel, asado",
      "Pollo, entero, con piel, crudo",
      "Pollo, fiambre",
      "Pollo, fiambre, bajo en grasa",
      "Pollo, frito",
      "Pollo, muslo, con piel, asado",
      "Pollo, muslo, con piel, crudo",
      "Pollo",
      "Pollo, pechuga, con piel, crudo",
      "Pollo, pechuga, plancha",
      "Pulmón, de cerdo, crudo",
      "Pulmón, de cordero, crudo",
      "Pulmón, de ternera, crudo",
      "Rabo de toro",
      "Riñón, de cordero, crudo",
      "Riñón, de ternera, crudo",
      "Salami",
      "Salchicha de pollo fresca",
      "Salchicha",
      "Salchicha frankfurt",
      "Salchicha, tipo país, a la plancha",
      "Salchicha, tipo viena",
      "Salchichón",
      "Sesos, de cerdo, crudos",
      "Sesos, de cordero, crudos",
      "Sesos, de ternera, crudos",
      "Sobrasada",
      "Ternera, costilla, cruda",
      "Ternera, lomo, crudo, con grasa separable",
      "Ternera",
      "Ternera, parte sin especificar, cruda, con grasa separable",
      "Ternera, solomillo, asado",
      "Ternera, solomillo, sin grasa, crudo",
      "Tocino",
      "Vaca/buey, parte s/e, asado",
      "Vaca/buey, parte s/e, estofado",
      "Vaca/buey, solomillo, a la plancha",
      "Vaca/buey, solomillo, crudo",
      "Almeja",
      "Almejas en conserva",
      "Anchoas",
      "Anguila, al horno",
      "Anguila, cruda",
      "Anguila, hervida",
      "Angula, cruda",
      "Arenque, ahumado",
      "Arenque, salado",
      "Atún",
      "Atun en aceite vegetal",
      "Atún en escabeche",
      "Atún, al horno",
      "Atún, al natural",
      "Atún, crudo",
      "Atún, plancha",
      "Bacaladilla",
      "Bacalao, ahumado",
      "Bacalao, crudo",
      "Bacalao",
      "Bacalao, frito",
      "Bacalao, salado, crudo",
      "Bacalao, salado, remojado, crudo",
      "Berberechos",
      "Berberechos en conserva",
      "Besugo",
      "Bígaro, hervido",
      "Bogavante",
      "Bogavante, hervido",
      "Bonito del norte, al vapor",
      "Bonito del norte, enlatado en aceite de soja",
      "Bonito",
      "Bonito, enlatado en aceite, escurrido",
      "Boquerón",
      "Boquerón, frito",
      "Breca",
      "Caballa, al horno",
      "Caballa",
      "Caballa, enlatada en aceite, escurrida",
      "Cabracho o rascacio, crudo",
      "Calamar, asado",
      "Calamar, conserva",
      "Calamar",
      "Calamares en aceite vegetal",
      "Camarón",
      "Cangrejo",
      "Cangrejo de río crudo",
      "Cangrejo, en conserva",
      "Caracol",
      "Carpa, al horno",
      "Carpa",
      "Caviar",
      "Centollo",
      "Chipiron",
      "Chirla",
      "Cigala",
      "Congrio",
      "Dorada",
      "Dorada, plancha",
      "Faneca",
      "Fletan",
      "Gallo",
      "Gamba quisquilla, congelada",
      "Gamba roja",
      "Gamba",
      "Jurel",
      "Langosta",
      "Langostino",
      "Lenguado",
      "Lenguado, al horno",
      "Lenguado, frito",
      "Lija, cruda",
      "Lubina",
      "Lucio, al horno",
      "Mejillon",
      "Mejillón, en conserva, al natural",
      "Mejillón, en escabeche",
      "Mejillón, hervido",
      "Merluza fresca",
      "Merluza",
      "Merluza, rebozada, frita",
      "Mero",
      "Mero, plancha",
      "Mújol, al horno",
      "Mújol",
      "Nécora",
      "Ostra",
      "Palometa",
      "Panga",
      "Perca, al horno",
      "Perca",
      "Percebe",
      "Pescadilla",
      "Pescadilla, rebozada en harina, frita",
      "Pescado, genérico",
      "Pez espada",
      "Pez espada, emperador, plancha",
      "Pijota",
      "Platija, al vapor",
      "Platija",
      "Pulpo",
      "Pulpo, hervido",
      "Rape, a la parrilla",
      "Rape",
      "Rape, plancha",
      "Raya",
      "Rodaballo",
      "Salema",
      "Salmón",
      "Salmón ahumado",
      "Salmón, plancha",
      "Salmonete",
      "Sardina",
      "Sardina, asada",
      "Sardina, enlatada, en aceite, escurrida",
      "Sardina, enlatada, en escabeche",
      "Sargo",
      "Sepia",
      "Tenca",
      "Trucha",
      "Trucha, ahumada",
      "Vieira",
      "Vieja, cruda",
      "Volador, crudo",
      "Zamburiñas",
      "Aceite de algodón",
      "Aceite de cacahuete",
      "Aceite de coco",
      "Aceite de colza",
      "Aceite de germen de trigo",
      "Aceite de girasol",
      "Aceite de grano de uva",
      "Aceite de hígado de bacalao",
      "Aceite de lino",
      "Aceite de nuez",
      "Aceite",
      "Aceite de oliva",
      "Aceite de oliva virgen extra, producción ecologica",
      "Aceite de palma",
      "Aceite de sésamo",
      "Aceite de soja",
      "Grasa de pollo",
      "Lecitina de soja",
      "Manteca",
      "Mantequilla salada",
      "Mantequilla",
      "Margarina de maíz",
      "Margarina",
      "Mayonesa con aceite de girasol",
      "Mayonesa, baja en calorías",
      "Nata montada",
      "Almidón de arroz",
      "Almidón de maíz",
      "Almidón de trigo",
      "Arroz",
      "Arroz hinchado, para el desayuno, enriquecido",
      "Arroz integral",
      "Arroz integral, hervido",
      "Arroz, hervido",
      "Avena",
      "Barrita cereales con chocolate",
      "Barrita cereales con frutas",
      "Barrita cereales maíz y trigo",
      "Barrita cereales trigo y chocolate",
      "Bizcocho",
      "Bollería, genérico",
      "Cebada",
      "Centeno",
      "Cereales base trigo y chocolate",
      "Cereales desayuno base de arroz chocolateado",
      "Cereales desayuno base de arroz y miel",
      "Cereales desayuno base de arroz, trigo y fruta",
      "Cereales desayuno base de maíz y miel",
      "Cereales desayuno base de maíz y trigo",
      "Cereales desayuno base de maíz, trigo y avena",
      "Cereales desayuno base de trigo azucarado",
      "Cereales desayuno base de trigo y arroz",
      "Cereales desayuno base de trigo y frutas",
      "Cereales desayuno base de trigo y miel",
      "Cereales desayuno base de trigo, avena, maiz y miel",
      "Cereales desayuno base de trigo, avena, maíz, miel y nueces",
      "Cereales desayuno base muesli",
      "Cereales",
      'Cereales para el desayuno, ricos en fibra, tipo "all-bran"',
      "Cereales, en polvo, solubles (eko)",
      "Churro",
      "Croissant",
      "Croissant de chocolate",
      "Donut",
      "Donut, de chocolate",
      "Ensaimada",
      'Galleta ,tipo "digestiva", con chocolate',
      "Galleta salada",
      "Galleta, barquillo, con jalea de frutas",
      "Galleta, cubierta de chocolate",
      "Galleta",
      'Galleta, tipo "Digestiva"',
      "Galletas integrales",
      "Galletas tipo maria",
      'Galletas, con chocolate, tipo "cookies"',
      "Galletas, de mantequilla",
      "Germen de trigo",
      "Gofio",
      "Harina de avena",
      "Harina de avena, cocida en agua",
      "Harina de cebada",
      "Harina de centeno",
      "Harina de maíz",
      "Harina",
      "Harina de trigo, integral",
      "Magdalena",
      "Masa de hojaldre",
      "Mijo",
      "Miso",
      "Muesli",
      "Napolitana, rellena con crema de cacao",
      "Palmera",
      "Pan",
      "Pan blanco, de barra, sin sal",
      "Pan de molde",
      "Pan blanco, frito",
      'Pan blanco, tipo "baguette"',
      "tostada",
      "Pan blanco, tostado sin sal",
      "Pan de avena",
      "Pan de cebada",
      "Pan de centeno",
      "Pan de leche",
      "Pan de maíz",
      "Pan integral",
      "Pan integral, de molde, tostado",
      "Pan integral, sin sal",
      "Pan integral, tostado",
      "Pan rallado",
      "Pan tostado integral",
      "Pan, tipo hamburguesa",
      "Pasta alimenticia, con huevo, cruda",
      "Pasta alimenticia, con huevo, hervida",
      "Pasta alimenticia, con vegetales, cruda",
      "Pasta alimenticia, cruda",
      "Pasta alimenticia, integral, cruda",
      "Pasta alimenticia, integral, hervida",
      "Pasta alimenticia, rellena con carne, hervida",
      "Pastas de te",
      "Pastel con fruta confitada",
      "Pastel de chocolate",
      "Pastel de manzana",
      "Quinoa",
      "Rosquilla",
      "Salvado de trigo",
      "Semilla de lino",
      "Sémola de trigo",
      "Sémola de trigo, hervida",
      "Sobao",
      "Torta de aceite",
      "Trigo",
      "Almendra",
      "Almendra, cruda, con cáscara",
      "Almendra, frita, salada",
      "Almendra, tostada",
      "Altramuz",
      "Alubia",
      "Alubia blanca, seca, cruda",
      "Alubia negra, seca, remojada, hervida",
      "Anacardo",
      "Avellana",
      "Cacahuete",
      "Cacahuete, frito, salado",
      "Cacahuete, tostado, salado",
      "Castaña",
      "Castaña, tostada",
      "Chufa",
      "Crema de almendras",
      "Crema de cacahuete",
      "Frutos secos",
      "Garbanzo",
      "Garbanzo, hervido",
      "Garbanzo, seco, crudo",
      "Guisante, congelado, crudo",
      "Guisante, congelado, hervido",
      "Guisante",
      "Guisantes en conserva",
      "Haba",
      "Haba, frita",
      "Haba, seca",
      "Haba, seca, remojada, hervida",
      "Harina de soja",
      "Judía blanca",
      "Judía pinta",
      "Judía verde",
      "Judías blancas, cocidas",
      "Lenteja, en conserva",
      "Lenteja, hervida",
      "Lenteja",
      "Nuez",
      "Piñón",
      "Piñón, crudo, con cáscara",
      "Pipa de calabaza",
      "Pipa de girasol",
      "Pipas de girasol, peladas, con sal",
      "Pistacho",
      "Sésamo, semilla",
      "Soja, fresca",
      "Soja, frita",
      "Soja",
      "Soja, seca, remojada, hervida",
      "Tofu",
      "Acelga",
      "Acelga, en conserva",
      "Achicoria",
      "Ajo",
      "Ajo, frito",
      "Albahaca",
      "Alcachofa",
      "Alcachofas en conserva",
      "Alcaparra",
      "Apio",
      "Apio, en conserva en salmuera",
      "Bambú",
      "Berenjena",
      "Berenjena, frita, en aceite de girasol",
      "Berro",
      "Boniato",
      "Borraja",
      "Brécol",
      "Brécol, hervido",
      "Calabacín",
      "Calabacín, asado",
      "Calabaza",
      "Calabaza, hervida",
      "Canonigos",
      "Cardo",
      "Cardo, tallo, en conserva",
      "Cebolla",
      "Cebolla, asada",
      "Cebolla, hervida",
      "Cebollino",
      "Champiñón",
      "Champiñones en conserva",
      "Col blanca",
      "Col de bruselas",
      "Col lombarda, hervida",
      "Col rizada",
      "Coliflor, congelada, cruda",
      "Coliflor, hervida",
      "Endibia",
      "Ensalada",
      "Escarola",
      "Espárrago, verde",
      "Esparragos blancos en conserva",
      "Espinaca, en conserva",
      "Espinaca",
      "Espinaca, picada, congelada, cruda",
      "Grelo",
      "Judía verde, congelada, cruda",
      "Judia verde, hervida",
      "Judias verdes en conserva",
      "Lechuga",
      "Lombarda",
      "Maíz, en mazorca, congelado, crudo",
      "Maíz",
      "Menestra de verduras, congelada",
      "Nabo",
      "Níscalo, crudo",
      "Palmito, en conserva",
      "Patata, asada",
      "Patata",
      "Patata, frita con aceite s/e, sin sal",
      "Patata, hervida",
      "Patata, prefrita, congelada",
      "Patata, salteada con aceite girasol",
      "Pepinillos en vinagre",
      "Pepino",
      "Pimiento",
      "Pimiento rojo",
      "Pimiento, frito",
      "Puerro",
      "Puré de patata y queso, en copos",
      "Puré de patata, con verduras, en copos",
      "Puré de patata, en copos",
      "Puré de patatas y champiñones, en copos",
      "Puré, de patata, con leche",
      "Rábano",
      "Remolacha",
      "Repollo",
      "Rúcula",
      "Seta",
      "Seta, plancha",
      "Soja, germinada, en conserva",
      "Tapioca, hervida",
      "Tomate",
      "Tomate, asado",
      "Tomate, maduro, pelado y triturado, enlatado",
      "Tomate, maduro, puré",
      "Trufa",
      "Zanahoria",
      "Aceituna",
      "Aceituna negra, con hueso",
      "Aguacate",
      "Aguacate congelado",
      "Albaricoque",
      "Arandano",
      "Caqui",
      "Cereza",
      "Chayote",
      "Chirimoya",
      "Ciruela",
      "Ciruela, sin piel",
      "Coco, desecado",
      "Coco",
      "Dátil",
      "Frambuesa",
      "Fresa",
      "Granada",
      "Grosella negra",
      "Grosella, cruda",
      "Guayaba, enlatada en almíbar",
      "Guayaba",
      "Higo",
      "Kiwi",
      "Lima",
      "Litchi",
      "Macedonia de frutas, conserva en su jugo",
      "Mandarina",
      "Mandarina, congelada",
      "Mango",
      "Manzana",
      "Melocotón",
      "Melocotón en almíbar",
      "Melocotón, desecado",
      "Melón",
      "Membrillo",
      "Naranja",
      "Nectarina",
      "Níspero",
      "Nispero, sin piel , congelado",
      "Papaya",
      "Paraguaya",
      "Pasta de fruta",
      "Pera",
      "Pera, enlatada en almíbar",
      "Piña",
      "Piña en almíbar",
      "Piña, enlatada en su jugo",
      "Plátano",
      "Pomelo",
      "Sandía",
      "Uva",
      "Uva blanca, congelada",
      "Uva negra, cruda",
      "pasa",
      "Azúcar blanca",
      "Azúcar, moreno",
      'Barra chocolate, tipo "bounty"',
      'Barra de chocolate, tipo "Kit-kat"',
      'Barra de chocolate, tipo "Mars"',
      "Bombón",
      "Cacao en polvo, azucarado",
      "Caramelo",
      "Chicle, sin azúcar",
      "Chocolate blanco",
      "Chocolate",
      "Chocolate con leche y almendras",
      "Chocolate con leche y arroz",
      "Chocolate con nueces de macadamia",
      "Chocolate negro con almendras",
      "Chocolate negro, con azúcar",
      "Chocolate negro",
      "Confitura, frutas s/e, baja en calorías",
      "Crema de chocolate con avellanas",
      "Crema inglesa",
      "Crema pastelera",
      "Fructosa",
      "Gominola, genérica",
      "Jalea real",
      "Mermelada de albaricoque",
      "Mermelada de albaricoque y melocotón, baja en calorías",
      "Mermelada de ciruela",
      "Mermelada de frambuesa",
      "Mermelada de fresa",
      "Mermelada de fresa, baja en calorías",
      "Mermelada de grosella roja",
      "Mermelada de mora",
      "Mermelada de naranja",
      "Miel",
      "Pastel",
      "Regaliz",
      "Turrón, tipo Alicante",
      "Agua de la red",
      "Agua",
      "Agua, con gas, embotellada",
      "Aguardiente",
      "Anís, seco",
      "Bebida energética",
      "Bebida isotónica",
      "Cacao",
      "Café, con leche",
      "Café",
      "Café, en polvo, sin reconstituir",
      "Café, en polvo, soluble",
      "Café, infusión",
      "Café, infusión, descafeinado",
      "Café, sucedáneo, soluble",
      "Cava",
      "Cerveza",
      "Cerveza sin alcohol",
      "Cerveza, baja en alcohol",
      "Cerveza, oscura, 8°- 9°",
      "Coñac",
      "Cubata",
      "Ginebra",
      "Horchata",
      "Infusión",
      "Licor apricot",
      "Licor benedictine",
      "Licor curaçao",
      "Licor de café",
      "Licor de crema 15-17% vol.",
      "Licores de frutas",
      "Limonada",
      "Néctar de albaricoque, envasado",
      "Néctar de ciruela",
      "Néctar de frutas exóticas, envasado",
      "Néctar de mango, envasado",
      "Néctar de maracuyá, envasado",
      "Néctar de melocotón",
      "Néctar de naranja, envasado",
      "Néctar de pera, envasado",
      "Néctar de piña",
      "Néctar de pomelo",
      'Refresco "tipo gaseosa"',
      "Refresco con gas, sabor cola, sin cafeina",
      "Refresco con gas, sabor cola, sin cafeina, bajo en calorías",
      "Refresco de té",
      "Refresco de té, bajo en calorías",
      'Refresco tipo "tónica"',
      "Refresco, con gas, sabor naranja",
      "Refresco de cola",
      "Refresco, sabor cola, bajo en calorías",
      "Refresco, sabor limón, con gas",
      "Refresco, sabor naranja, sin gas",
      "Ron",
      "Sangría",
      "Sidra",
      "Soda",
      "Té, infusión, con leche",
      "Tequila",
      "Vermut, s/e",
      "Vino",
      "Vino dulce, tipo oporto",
      "Vino rosado",
      "Vino tinto",
      "Vodka",
      "Whisky",
      "Zumo de grosella negra",
      "Zumo de grosella roja",
      "Zumo de lima",
      "Zumo de limón",
      "Zumo de mango",
      "Zumo de manzana",
      "Zumo de naranja",
      "Zumo de piña",
      "Zumo de piña y uva",
      "Zumo de pomelo",
      "Zumo de tomate",
      "Zumo de uva y melocotón",
      "Zumo de zanahoria",
      "Ajo, en polvo",
      "Albondigas en conserva",
      "Alioli",
      "Aperitivos de trigo",
      "Azafrán",
      "Bocadillo",
      "Caldo vegetal",
      "Canela",
      "Canelones",
      "Chile",
      "Chile, verde",
      "Comino",
      "Complejo vitaminico",
      "Corteza de trigo",
      "Crema de chocolate y nata",
      "Crema de chocolate, baja en calorías",
      "Crema de coco",
      "Crema de vainilla y mousse de chocolate",
      "Cubito de caldo",
      "Curry",
      "Empanada de carne",
      "Empanadilla",
      "Eneldo, seco",
      "Ensaladilla rusa",
      "Fabada",
      "Flamenquín",
      "Fritos de maíz",
      "Galletas saladas, con queso",
      "Gazpacho",
      "Gelatina",
      "Gomasio",
      "Guindilla, en polvo",
      "Guindilla",
      "Gusanito",
      "Hinojo",
      "Hojaldre",
      "Jengibre",
      "Kebab",
      "Ketchup",
      "Lasaña",
      "Laurel",
      "Mayonesa",
      "Mayonesa, aceite de soja",
      "Menta",
      "Mojo picon",
      "Mostaza",
      "Nuez moscada",
      "Orégano",
      "Paella",
      "Paella marinera",
      "Palomitas de maíz, sin aceite, sin sal",
      "Pasta de sésamo",
      'Patatas chips, "lights"',
      "Patatas, fritas, chips",
      "Perejil",
      "Pimentón",
      "Pimienta",
      "Pimienta negra",
      "Pizza, precocinada",
      "Pudding de pasas",
      "Rollito de primavera",
      "Romero",
      "Sal de mar",
      "Sal",
      "Salsa agridulce",
      "Salsa al curry",
      "Salsa al roquefort",
      "Salsa barbacoa",
      "Salsa bechamel",
      "Salsa boloñesa",
      "Salsa carbonara",
      "Salsa de queso",
      "Salsa de soja",
      "Salsa napolitana",
      "Salsa siciliana, picante",
      "Salsa vinagreta, con aceite de oliva",
      "San jacobo, congelado",
      "Seitán",
      "Sofrito",
      "Sopa de sobre maravilla",
      "Sopa de sobre, sin reconstituir",
      "Suplemento proteico",
      "Surimi",
      "Tabasco",
      "Tomate frito",
      "Tomillo",
      "Vainilla",
      "Vinagre balsámico",
      "Vinagre de manzana",
      "Vinagre",
      "Jamón de york",
      "Azúcar",
      "limón",
    ],
    units: [
      "kg",
      "gr",
      "cucharilla",
      "cucharadita",
      "cucharada",
      "cucharada sopera",
      "taza",
      "vaso",
      "cuenco",
      "envase",
      "paquete",
      "bolsa",
      "lata",
      "botella",
      "litro",
      "paquete",
      "frasco",
      "gota",
      "cabeza",
      "pellizco",
      "sobre",
      "diente",
      "puñado",
      "barra",
      "caja",
      "copa",
      "pizca",
      "chorro",
      "chorrito",
      "unidad",
      "racimo",
      "loncha",
      "receta",
      "capa",
      "rebanada",
      "gajo",
      "tallo",
      "cuadrado",
      "pechuga",
      "filete",
      "trozo",
      "pata",
      "muslo",
      "cubo",
      "lámina",
      "hoja",
      "gramo",
      "ml",
    ],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    clean_ingredient_inputs() {
      this.selected_ingredient = "";
      this.selected_quantity = "";
      this.selected_unit = "";
    },
    addIngredient(selected_ingredient, selected_quantity, selected_unit) {
      var new_ingredient = {
        name: selected_ingredient,
        quantity: selected_quantity,
        unit: selected_unit,
      };
      this.ingredients_list.push(new_ingredient)
      this.recipe_ingredients.unshift(new_ingredient); // push item to existing array
      if (this.recipe_ingredients[this.recipe_ingredients.length - 1] === "") {
        this.recipe_ingredients.pop();
      }
      this.clean_ingredient_inputs();
    },
    createRecipe(name,comensals) {
      var new_recipe = {
        creator: this.$store.getters.username,
        recipe_name: name,
        ingredients: this.ingredients_list,
        comensales: comensals,
      };
      this.recipe_ingredients= ["", "", "", "", "", "", "", "", "", "", "", "","",""],
      this.ingredients_list=[],
      axios({
        baseURL: this.$store.getters.baseUrl,
        url: "/newRecipe",
        method: "post",
        data: new_recipe,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>



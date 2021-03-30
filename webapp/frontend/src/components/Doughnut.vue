<template>
  <mdb-container>
    <div> {{values}}</div>
    <mdb-doughnut-chart
      :data="doughnutChartData"
      :options="doughnutChartOptions"
      :width="600"
      :height="300"
    ></mdb-doughnut-chart>
  </mdb-container>
</template>

<script>
  import { mdbDoughnutChart, mdbContainer } from "mdbvue";
  export default {
    name: "ChartPage",
    props: {
      values: Array,
    },
    components: {
      mdbDoughnutChart,
      mdbContainer
    },
    data() {
      return {
        doughnutChartData: {
          labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
          datasets: [
            {
              data: [300, 50, 100, 40, 120],
              backgroundColor: [
                "#F7464A",
                "#46BFBD",
                "#FDB45C",
                "#949FB1",
                "#4D5360"
              ],
              hoverBackgroundColor: [
                "#FF5A5E",
                "#5AD3D1",
                "#FFC870",
                "#A8B3C5",
                "#616774"
              ]
            }
          ]
        },
        doughnutChartOptions: {
          responsive: false,
          maintainAspectRatio: false
        }
      };
    }
  };
</script>

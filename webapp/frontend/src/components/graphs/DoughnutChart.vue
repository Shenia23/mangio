<script>
  import { Doughnut } from 'vue-chartjs'
  import ChartJsPluginDataLabels from 'chartjs-plugin-datalabels'
  window.Chart.plugins.register(ChartJsPluginDataLabels);
  //Chart.defaults.global.plugins.datalabels.display = false

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        options: {
          cutoutPercentage: 40,
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: true,
          tooltips: {
              enabled: false
          },
          plugins:{
            datalabels: {
              formatter: function (value) {
                return value + '%'
              },
            }
          }
        },
      }
    },
    props: {
      chartData: Object
    },
    methods: {
        reload(){
            this.renderChart(this.chartData, this.options);
        },
    },
    mounted () {    
      //this.addPlugin(ChartJSPluginDatalabels);
      this.renderChart(this.chartData, this.options);
    },
  }
</script>
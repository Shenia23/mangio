<script>
  import { Radar } from 'vue-chartjs'

  export default {
    extends: Radar,
    data () {
      return {
        name: 'RadarChart',
        options: {

            scales: {
                yAxes: [{
                    display: false,
                }],
            },
            scale: {
              ticks: {
                callback: function(value) {
                    return ""
                    },
                beginAtZero: true
              }
            },
            legend: {
                display: true
            },
            responsive: true,
            maintainAspectRatio: true,
            plugins:{
            datalabels: {
              formatter: function (value) {
                return ''
              },
            }
          }
        }
      }
    },
    props: {
          chartData: Object
        },
    methods:{
        reload(){
            this.renderChart(this.chartData, this.options);
        }
    },
    mounted () {
      this.renderChart(this.chartData, this.options);
    },
  }
</script>
<script>
  import { Radar } from 'vue-chartjs'

  export default {
    extends: Radar,
    data () {
      return {
        name: 'RadarChart',
        options: {
            barValueSpacing: 100,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            legend: {
                display: true
            },
            responsive: true,
            maintainAspectRatio: true,
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
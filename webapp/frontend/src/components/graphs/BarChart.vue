<script>
  import { Bar } from 'vue-chartjs'

  export default {
    extends: Bar,
    data () {
      return {
        name: 'BarChart',
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
            //maintainAspectRatio: false,x
            height: 200,
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
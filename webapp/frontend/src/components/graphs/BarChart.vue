<script>
  import { Bar } from 'vue-chartjs'

  export default {
    extends: Bar,
    data () {
      return {
        name: 'BarChart',
        options: {
            barValueSpacing: 20,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        maxTicksLimit : 5,
                        callback: function(value) {
                        return value + '%'
                        },
                    }
                }]
            },
            legend: {
                display: true
            },
            responsive: true,
            maintainAspectRatio: false,
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
<script>
  import { Doughnut } from 'vue-chartjs'

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        props: {
          chartData: Array
        },
        options: {
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        },
      }
    },
    watch: {
      deep: true,
      chartData: { // watch it
        deep: true,
        handler: function(newVal, oldVal){
          console.log('Prop changed: ', newVal, ' | was: ', oldVal)
          this.chartData = newVal
        }
      }
    },
    methods: {
        reload(){
            this.renderChart(this.chartData, this.options);
        },
    },
    mounted () {
      this.renderChart(this.chartData, this.options);
    },
  }
</script>
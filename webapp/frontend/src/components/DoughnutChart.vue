<script>
  import { Doughnut } from 'vue-chartjs'

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        props: ['chartData'],
        options: {
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        },
      }
    },
    mounted () {
      console.log(this.chartData)
      this.renderChart(this.chartData, this.options)
    },
  }
</script>
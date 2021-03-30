<script>
  import { Doughnut } from 'vue-chartjs'

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        props: {
          new_data: {
            type: Array,
            default: [10,20,30]
          }
        },
        chartData: {
          labels: ["Proteínas",	"Grasas",	"Carbohidratos"],
          datasets: [{
              borderWidth: 1,
              borderColor: [
              '#184d47',
              '#96bb7c',
              '#fad586'              
              ],
              backgroundColor: [
              '#184d47',
              '#96bb7c',
              '#fad586',        
              ],
              data: [300,300,254]
            }]
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
    mounted () {
      console.log(this.new_data)
      this.renderChart(this.chartData, this.options)
    }
  }
</script>
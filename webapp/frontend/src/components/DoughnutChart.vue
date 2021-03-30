<script>
  import { Doughnut } from 'vue-chartjs'

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        props: {
          new_data: Array
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
      console.log('mounted: ',this.new_data)
      console.log(this.props.new_data)
      this.chartData.data = this.new_data
      this.renderChart(this.chartData, this.options)
    },
    created () {
      console.log("created",this.new_data)
    },
    beforeUpdate () {
      console.log('be:',this.new_data)
    }
  }
</script>
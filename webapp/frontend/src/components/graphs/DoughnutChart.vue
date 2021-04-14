<script>
  import { Doughnut } from 'vue-chartjs'

  export default {
    extends: Doughnut,
    data () {
      return {
        name: 'DoughnutChart',
        options: {
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
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
      this.renderChart(this.chartData, this.options);
    },
  }
</script>
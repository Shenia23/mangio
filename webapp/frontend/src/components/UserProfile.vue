<template>
  <div>
    <p>Aquí se realizan las mediciones de la báscula</p>


    <v-btn
      color="success"
      class="mr-4"
      @click="scan"
    >
      Scan
    </v-btn>


  </div> 
</template>

<script>
export default {
  data: () => ({
      name: ''    }),
methods: {
    call_wrappersh: function () {
/*         var exec = require('child process').exec, child;
        child = exec('/home/pablo/Desktop/mangio/app/MiScale/src/wrapper.sh', 
        function (error,stdout,stderr){

            console.log('stdout' + stdout)
            console.log('stderr' + stderr)
            if(error!==null){
                console.log('exec_error:' + error);
            }
        }); */
            }


        }
    }
</script>


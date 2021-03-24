const { createApp, ref, computed } = Vue;
const rider= createApp({
    delimiters: ['[[',']]'],
    data(){
        return {
            pickup1: 'Vasant Kunj',
            pickup2: 'Sarita Vihar',
            dropoff1: 'India Gate',
            dropoff2: 'Feroz Shah Kotla Stadium',
        }
    },
    methods: {
        requestRide(){
            console.log("Hello Ride requested")
            var pickuploc="oh no";
            if($("#pickup").val() === '1')
            {
                pickuploc=this.pickup1;
            }
            else{
                pickuploc=this.pickup2;
            }
            var dropoffloc="oh no no";
            if($("#dropoff").val() === '1')
            {
                dropoffloc=this.dropoff1;
            }
            else{
                dropoffloc=this.dropoff2;
                
            }
            var rfc=$("#flexSwitchCheckDefault").is(":checked");
            console.log(`From ${pickuploc} to ${dropoffloc} rfc: ${rfc}`)
            
        }
    }
})
rider.mount('#view')
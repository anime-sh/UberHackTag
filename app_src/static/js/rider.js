const { createApp, ref, computed } = Vue;
const rider = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            pickup1: 'Vasant Kunj',
            pickup2: 'Sarita Vihar',
            dropoff1: 'India Gate',
            dropoff2: 'Feroz Shah Kotla Stadium',
            showmap: false,
        }
    },
    methods: {
        async requestRide() {
            console.log("Hello Ride requested")
            var pickuploc = "oh no";
            if ($("#pickup").val() === '1') {
                pickuploc = this.pickup1;
            }
            else {
                pickuploc = this.pickup2;
            }
            var dropoffloc = "oh no no";
            if ($("#dropoff").val() === '1') {
                dropoffloc = this.dropoff1;
            }
            else {
                dropoffloc = this.dropoff2;

            }
            var rfc = $("#flexSwitchCheckDefault").is(":checked");
            console.log(`From ${pickuploc} to ${dropoffloc} rfc: ${rfc}`)

            entry={
                source:`pickup${$("#pickup").val()}`,
                dest:`dropoff${$("#dropoff").val()}`
            };
            const requestOptions = {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(entry),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json"
                })
            }
            const response = await fetch(`${window.origin}/rider/booked`,requestOptions);
            const data = await response.json();
            console.log(data)

        }
    }
})
rider.mount('#view')
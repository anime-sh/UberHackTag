const { createApp, ref, computed } = Vue;
const rider = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            pickup1: 'Vasant Kunj',
            pickup2: 'Sarita Vihar',
            dropoff1: 'Feroz Shah Kotla Stadium',
            dropoff2: 'India Gate',
            showmap: false,
            plot_url: 'lmao lmao',
            rfc:false,
            base_fare:undefined,
            extra_fare: undefined,
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
            console.log(`From ${pickuploc} to ${dropoffloc} rfc: ${rfc}`);
            this.rfc=rfc;
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
            console.log(window.location.pathname);
            this.showmap=true;
            this.plot_url=`${window.origin}/gmplot`;
            this.base_fare=data['base'];
            this.extra_fare=data['extra'];
        }
    }
})
rider.mount('#view')
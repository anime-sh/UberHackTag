rider = new Vue({
    el: '#view',
    delimiters: ['[[', ']]'],
    data() {
        return {
            pickup1: 'Vasant Kunj',
            pickup2: 'Sarita Vihar',
            dropoff1: 'Feroz Shah Kotla Stadium',
            dropoff2: 'India Gate',
            showmap: false,
            plot_url: 'lmao lmao',
            rfc: false,
            base_fare: undefined,
            extra_fare: undefined,
            pickuploc: undefined,
            dropoffloc: undefined
        }
    },
    methods: {
        async requestRide() {
            console.log("Hello Ride requested")
            if ($("#pickup").val() === '1') {
                this.pickuploc = this.pickup1;
            }
            else {
                this.pickuploc = this.pickup2;
            }
            if ($("#dropoff").val() === '1') {
                this.dropoffloc = this.dropoff1;
            }
            else {
                this.dropoffloc = this.dropoff2;

            }
            var rfc = $("#flexSwitchCheckDefault").is(":checked");
            console.log(`From ${this.pickuploc} to ${this.dropoffloc} rfc: ${rfc}`);
            this.rfc = rfc;
            entry = {
                source: `pickup${$("#pickup").val()}`,
                dest: `dropoff${$("#dropoff").val()}`
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
            const response = await fetch(`${window.origin}/rider/booked`, requestOptions);
            const data = await response.json();
            console.log(data)
            console.log(window.location.pathname);
            this.plot_url = `${window.origin}/gmplot_${entry.source}_${entry.dest}`;
            this.showmap = true;
            this.base_fare = data['base'];
            this.extra_fare = data['extra'];
        },
        async confirmRide() {
            var rfcmode = 0
            if(this.rfc)
                rfcmode = 1
            window.location.href = "/rider/riding/" + this.base_fare + "/" + this.extra_fare + "/" + rfcmode;
        }
    }
})

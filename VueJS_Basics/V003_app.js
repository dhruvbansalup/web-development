
var app = new Vue({
    el: "#app",
    data: {
        message: "Hello Vue!",
    },
    methods: {
        sayHi: function () {
            this.message = "Hi";
        }
    }
})
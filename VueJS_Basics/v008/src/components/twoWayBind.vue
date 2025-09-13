<template>
    <h1>hi</h1>
    <input type="text" v-model="count"/>
    <h2>{{ count }}</h2>
    <button v-on:click="count++">Count++</button>
<br><br>
    <input v-model="email" type="text" placeholder="email">
    <br>
    <input type="text" v-model="password" placeholder="password">
    <br><button v-on:click="getData()" type="button">Get value</button>
</template>

<script>
export default {
    data(){
        return{
            count:0,
            email:null,
            password:null,
        }
    },
    methods:{
        getData(){
            alert(`Email: ${this.email}\nPassword: ${this.password}`)
        }
    }
}
</script>
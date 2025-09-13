<template>
    <h4>Home</h4>
    <!-- <input type="text" v-model="data" />
    <input type="number" v-model.number="data" />
    <p>Data is {{ data }}</p>
    <p>datatype: {{ typeof (data) }}</p> -->
    <childComponent>
        <template v-slot:slot1>
            <h6>Hello</h6>
        </template>
    </childComponent>

    <p v-for="item in list" :key="item">
        {{ item.id }}
        {{ item.name }}
        {{ item.email }}
    </p>



</template>

<script>

import childComponent from './child.vue'
import axios from 'axios'
export default {
    name: "HomeView",
    components: {
        childComponent,
    },
    data() {
        return {
            data: '',
            list:[]
        }
    },
    async mounted(){
        let result=await axios.get("https://jsonplaceholder.typicode.com/users")
        this.list=result.data;
    }
}
</script>

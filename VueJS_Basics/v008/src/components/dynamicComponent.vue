<template>
    <p></p>
    <dc_1 />
    <dc_2 />
    <dc_3 />

    <component :is="tab" style="color: red;"/>

    <button @click="tab='dc_1'">1</button>
    <button @click="tab='dc_2'">2</button>
    <button @click="tab='dc_3'">3</button>
</template>

<script>

import dc_1 from './dc_1.vue'
import dc_2 from './dc_2.vue'
import dc_3 from './dc_3.vue'

export default {
    components: {
        dc_1, dc_2, dc_3,
    },
    data(){
        return{
            tab: 'dc_1',
        }
    }
}
</script>
<script setup>
import card from '@/components/card.vue'
</script>

<template>
    <div class="grid grid-cols-1 md-cols-2">

        <div class="container-xl m-auto">
            <card>
                <h2 class="text-2xl font-bold">
                    For Developers
                </h2>
                <p class="mt-2 mb-4">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Est id laborum soluta accusamus cu
                </p>
                <a href="" class="inline-block bg-black text-white rounded-lg px-4 py-2 hover:bg-grey-700">
                Browse Jobs
                </a>
            </card>
            <card bg="bg-red-100">
                <h2 class="text-2xl font-bold">
                    For Developers
                </h2>
                <p class="mt-2 mb-4">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Est id laborum soluta accusamus cu
                </p>
                <a href="" class="inline-block bg-black text-white rounded-lg px-4 py-2 hover:bg-grey-700">
                Browse Jobs
                </a>
            </card>
        </div>
    </div>
</template>
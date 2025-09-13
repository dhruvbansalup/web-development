<template>
    <slot name="slot1">
        <h4>This is default child</h4>
    </slot>
    <slot name="slot2">
        <p>This is second slot</p>
    </slot>
</template>

<script>
export default {
    name: 'ChildComponent',
}
</script>
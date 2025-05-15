<template>
    <div class="child">
        <h2>자식 페이지</h2>
        <p>{{child.name}}</p>
    </div>
</template>

<script setup>
const props = defineProps({
    child:Object
})
</script>

<style scoped>
.child {
    margin: 1rem ;
    border: 1px rgb(180, 180, 180) solid;
    background-color: rgb(252, 252, 252);

}
</style>
<template>
    <div class="family">
        <h2>부모 컴포넌트</h2>
        <p>{{family.father}}</p>
        <p>{{family.mother}}</p>
        <ChildPage
        v-for="child in children"
        :key="child.name"
        :child="child"
        />
    </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';
const props = defineProps({
    family: Object
})
const children = props.family.children
</script>

<style scoped>
.family {
    text-align: center;
    border: 1px rgb(196, 196, 196) solid;
    background-color: rgb(243, 243, 243);
    margin: 1rem;
}
</style>
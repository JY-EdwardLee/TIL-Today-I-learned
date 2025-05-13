<template>
    <h1>Parent</h1>
    <p>{{ userName }}</p>
    <Child 
     :user-name="userName"
     parent-name="Bella"
     @change-user-name="$emit('changeUserName')"
    />
</template>

<script setup>
    import Child from '@/components/Child.vue'
    // prop 정보를 정의하는 법
    // 1. 러프한 방식
    // defineProps({
    //     userName : String,
    // })
    // 2. 좀 더 엄격한 방식 (기본값, 유효성 검사 등 추가 가능)
    defineProps({
        userName:{
            type: String,
            required: true,
        }
    })

</script>

<style scoped>

</style>
<template>
    <h5>ChildItem</h5>
    <p>{{ item.id }}</p>
    <p>{{ item.name }}</p>
    <button @click="buttonClick">클릭</button>
</template>

<script setup>
 const props = defineProps({
    item: Object,
 })
 const emit = defineEmits(['someEvent'])
 const buttonClick = function() {
    // {이곳에 복잡한 로직을 작성하는 영역}
    emit('someEvent', props.item, '구아바')
 }
//  console.log(props.item.name)
// 절대, 하위 컴포넌트에서 prop 받은 아이템을 수정하면 안된다.
// item 객체는 radonly라 수정 자체가 불가능
// props.item.name = "파인애플"
// props.item = {id:4, name:"파인애플"}
</script>

<style scoped>

</style>
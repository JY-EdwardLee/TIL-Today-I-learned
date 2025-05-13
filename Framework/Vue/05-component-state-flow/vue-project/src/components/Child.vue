<template>
    <h1>Child</h1>
    <p>
        {{ userName }},
        {{ parentName }}
    </p>
    <!-- ChildItem components는 items 배열의 요소 수만큼 만들 것이다. -->
     <button @click="$emit('changeUserName')">click</button>
    <!-- someEvent를 listen 하고 있어야 한다. -->
    <ChildItem
    v-for="item in items"
    :key="item.id"
    :item="item"
    @some-event="onSomeEvent"
    />
    <ChildItem
    v-for="item in items"
    :key="item.id"
    :item="item"
    @some-event="onSomeEvent"
    />
    <p></p>
</template>

<script setup>
import {ref} from 'vue'
import ChildItem from './ChildItem.vue'
defineProps({
    userName: {
        type: String,
        required: true,
    },
    parentName: String
})
const items = ref([
    {id:1, name: '사과'},
    {id:2, name: '바나나'},
    {id:3, name: '딸기'},
])
const onSomeEvent = function(item, name) {
    console.log('어떤 이벤트가 발생함')
    for (let i=0; i<items.value.length; i+=1){
        if (item.id === items.value[i].id) {
            items.value[i].name = name
        }
    }   
}
</script>

<style scoped>

</style>
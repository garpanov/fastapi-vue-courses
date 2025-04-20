<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const route = useRoute()

const lesson_data = ref()

async function get_info_lesson() {
    const id_course = route.params.id_course
    const id_lesson = route.params.id_lesson

    const { data } = await api.get(`/admin/confirmation/lesson/${id_course}/${id_lesson}`)
    lesson_data.value = data
    console.log(data)
}

onMounted(async () => {
    await get_info_lesson();
    console.log(lesson_data.value);
})
</script>

<template>
    <Header></Header>

    <main class="relative flex flex-col items-center mt-15">
        <div class="text-center">
            <h1 class="text-8xl">Python start</h1>
            <h2 class="mt-10 text-3xl">Lesson {{ lesson_data?.position }}</h2>
        </div>
        <div class="w-7/12 mt-30">
            <p class="text-[#9D9D9D] text-4xl leading-normal">{{ lesson_data?.description }}</p>
        </div>

        <iframe class="my-20" :src='lesson_data?.url_video' width="800" height="500"></iframe>
    </main>

    <Footer></Footer>
</template>

<style scoped>
main {
    background-image: url('/profile/background.png');
    background-size: cover;
    background-position: center;
}

h1,
h2,
.button-confirm {
    color: white;
}

p,
h1,
h2,
.button-confirm {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}
</style>
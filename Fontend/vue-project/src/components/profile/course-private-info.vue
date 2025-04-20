<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const route = useRoute()

const data_lesson = ref({position: '', description: '', url_video: ''})

async function get_info() {
    const course_id = route.params.course_id
    const lesson_id = route.params.lesson_id

    const { data } = await api.get(`/for_profile/about_lesson/${course_id}/${lesson_id}`)

    data_lesson.value = data
}

onMounted(async () => {
    await get_info()
})
</script>

<template>
    <Header></Header>

    <main class="relative flex flex-col items-center mt-15">
        <div class="text-center">
            <h1 class="text-8xl"></h1>
            <h2 class="mt-10 text-3xl">Lesson {{ data_lesson.position }}</h2>
        </div>
        <button
            class="absolute mt-15 ml-350 button-confirm text-shadow-lg text-xl py-2.5 px-6 rounded-2xl bg-[#00C11D] cursor-pointer transition hover:bg-[#00E522] active:bg-[#009E18]">Confirm</button>

        <div class="w-7/12 mt-30">
            <p class="text-[#9D9D9D] text-4xl leading-normal">{{ data_lesson.description }}</p>
        </div>

        <iframe class="my-20" :src='data_lesson.url_video' width="800" height="500"></iframe>
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
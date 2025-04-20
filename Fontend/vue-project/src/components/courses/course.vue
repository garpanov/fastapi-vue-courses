<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

import Header from '../header.vue';
import Footer from '../footer.vue';
import { api } from '../profile/checkAuth';

const route = useRoute()
const router = useRouter()

const data_course = ref({id: 0, name: '', full_description: '', author: '', lessons: [{position: 1, name: '', description: '', isOpen: false}]})

type Lesson = {
    position: number,
    name: string,
    description: string,
    isOpen?: boolean
}

async function join_course() {
    const id_course = route.params.id_course
    
    const response = await api.get(`/for_profile/to_activated_course/${id_course}`)
    router.push({name: 'profile'})
}

async function get_info_course() {
    const id_course = route.params.id_course

    const response = await axios.get(`${import.meta.env.VITE_API_URL}/course/${id_course}`)

    data_course.value = response.data
    data_course.value.lessons = data_course.value.lessons.map((lesson: Lesson) => ({
        ...lesson,
        isOpen: false
    }));

}

onMounted(async () => {
    await get_info_course()
})

</script>

<template>
    <Header></Header>

    <section class="courses-section pt-20">
        <button @click="join_course"
            class="join-button absolute text-white bg-[#00D01F] text-xl py-3 px-6 rounded-3xl right-100 text-shadow-lg mt-3 transition hover:bg-[#00FD25] cursor-pointer active:bg-[#00BE1C] active:scale-98">Join</button>
        <div class="flex flex-col text-center items-center gap-30">
            <h1 class="text-7xl">{{ data_course.name }}</h1>
            <p class="full-description w-4/6 leading-normal text-left text-3xl">{{ data_course.full_description }}</p>
        </div>
        <h2 class="avtor mt-20 text-right w-10/12 text-2xl">by {{ data_course.author }}</h2>

        <div class="flex flex-col text-center items-center mt-40">
            <div class="flex flex-col gap-5">
                <h2 class="learning-program text-5xl">Learning program</h2>
                <p class="p-title-program text-xl">These are the first four lessons</p>
            </div>

            <div class="flex flex-col w-8/12 mt-30 gap-7 text-center mb-20">
                <div :class="{ 'bg-[rgba(62,62,62,0.37)]': !lesson.isOpen, 'bg-[rgba(125,122,122,0.37)]': lesson.isOpen }"
                    class="px-15 py-5 cursor-pointer transition-colors duration-500"
                    v-for="lesson in data_course.lessons">
                    <div @click="lesson.isOpen = !lesson.isOpen" class="flex items-center justify-between">
                        <h3 class="lesson-h3 text-4xl">Lesson {{ lesson.position }}</h3>
                        <img :class="{ 'rotate-0': lesson.isOpen, 'rotate-180': lesson.isOpen }"
                            class="w-17 transition-transform duration-500" src="/courses/arrow.png" alt="arrow">
                    </div>
                    <div v-if="lesson.isOpen">
                        <p class="description-lesson tracking-wide leading-normal text-left text-3xl mt-10">{{ lesson.description }}</p>
                    </div>
                </div>
                <h4 class="text-2xl mt-5">Join the course to unlock videos <br> and additional materials</h4>
            </div>
        </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
.courses-section {
    background-image: url('../../public/courses/background.png');
    background-size: cover;
    background-position: center;
}

h1,
h2,
h3,
p {
    color: white;
}

h1,
.description-lesson {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

.full-description {
    color: #d8d8d8;
    font-family: "Inter", sans-serif;
    font-weight: 500;
}

.join-button {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}

.avtor {
    font-family: "Inter", sans-serif;
    font-weight: 700;
    font-style: italic;
}

.learning-program {
    font-family: "Inter", sans-serif;
    font-weight: 800;
    font-style: italic;
}

.p-title-program {
    font-family: "Inter", sans-serif;
    font-weight: 700;
    color: #DFDFDF;
}

.lesson-h3 {
    font-family: "Roboto", sans-serif;
    font-weight: 700;
    font-style: italic;
}

h4 {
    color: #A0A0A0;
    font-family: "Roboto", sans-serif;
    font-weight: 500;
}
</style>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const router = useRouter()
const route = useRoute()

const full_data = ref({id: 1, name: '', full_description: '', author_name: '', lessons: [{id: 1, position: 1, description: '', completed: false}]})

function detailing_lesson(lesson_id: number) {
    router.push(`/course-private/lesson/${full_data.value.id}/${lesson_id}`)
}

async function get_information_course() {
    const course_id = route.params.course_id
    const { data } = await api.get(`/for_profile/info_course/${course_id}`)
    full_data.value = data
}

onMounted(async () => {
    await get_information_course()
})
</script>

<template>
    <Header></Header>
    <main class="flex flex-col px-20 py-20 items-center">
        <div class="w-8/12 text-center">
            <h1 class="text-7xl">{{ full_data.name }}</h1>
            <p class="full-description mt-20 text-2xl leading-normal">{{ full_data.full_description }}</p>
        </div>
        <div class="w-9/12 text-right mt-20">
            <span class="avtor text-2xl">by {{ full_data.author_name }}</span>
        </div>

        <div class="mt-50 items-center flex flex-col">
            <h2 class="text-6xl">
                Lessons
            </h2>
            <div class="grid grid-cols-3 gap-10 w-11/12 mt-20">
                <div @click="detailing_lesson(lesson['id'])" v-for="lesson in full_data.lessons" class="bg-[#0D0D0D] border border-[#262626] pt-7 pb-9 px-11 shadow-xl/40 rounded-[2.5vw] cursor-pointer hover:bg-[#1E1E1E] transition ">
                    <div class="flex items-center justify-between mr-7">
                        <h3 class="h3-lesson ml-3 text-3xl">Lesson {{ lesson["position"] }}</h3>
                        <img v-if="lesson.completed" class="w-10" src="/profile/accept.png">
                    </div>
                    <p class="p-lesson text-xl mt-5">{{ lesson['description'] }}</p>
                </div>
            </div>
        </div>
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
.h3-lesson,
.avtor {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

.full-description {
    color: #ECECEC;
    font-family: "Inter", sans-serif;
    font-weight: 100;
}

.avtor {
    font-family: "Inter", sans-serif;
    font-weight: 700;
    font-style: italic;
}

h2 {
    color: #ECECEC;
    font-family: "Inter", sans-serif;
    font-weight: 800;
    font-style: italic;
}

.h3-lesson {
    font-family: "Inter", sans-serif;
    font-weight: 800;
}

.p-lesson {
    color: #BABABA;
    font-family: "Inter", sans-serif;
    font-weight: 800;
}
</style>
<script setup lang="ts">
import { useRouter } from 'vue-router';

import check_auth from './checkAuth';
check_auth()

defineProps(['data', 'url_for_lesson'])

const router = useRouter()
function detailing_lesson(id_course: number, id_lesson: number, url_for_lesson: string) {
  router.push(`${url_for_lesson}${id_course}/${id_lesson}`)
}


</script>

<template>
    <div class="flex flex-col text-center items-center gap-30">
        <h1 class="text-7xl">{{ data.name }}</h1>
        <p class="full-description w-4/6 leading-normal text-left text-3xl">{{ data.full_description }}</p>
    </div>
    <h2 class="avtor mt-20 text-right w-10/12 text-2xl">by {{ data.author }}</h2>

    <div class="flex flex-col text-left items-center mt-40">
        <h2 class="learning-program text-6xl">Lessons</h2>
        <div class="grid grid-cols-2 gap-20 w-7/12 mt-20">
            <div @click="detailing_lesson(data.id, lesson['id'], url_for_lesson)" v-for="lesson in data.lessons"
                class="bg-[#0D0D0D] border border-[#262626] pt-7 pb-9 px-11 shadow-xl/40 rounded-[2.5vw] cursor-pointer hover:bg-[#1E1E1E] transition ">
                <div class="flex items-center justify-between mr-7">
                    <h3 class="h3-lesson ml-3 text-3xl">Lesson {{ lesson["position"] }}</h3>
                </div>
                <p class="p-lesson text-2xl mt-5 w-11/12">{{ lesson['name'] }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
h1,
h2,
h3,
p,
.h3-lesson {
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
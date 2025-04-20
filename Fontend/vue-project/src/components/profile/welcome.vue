<script setup lang="ts">
import { useRouter } from 'vue-router';

import Header from '../header.vue';
import Footer from '../footer.vue';
import Aside from './aside.vue';
import check_auth, { api } from './checkAuth';
check_auth()

const courses = [
    {
        'name': 'Python Start', 'short_description': 'This course is for those who want to learn Python from scratch',
        'image_main': '../../public/courses/python.png', 'points': 30, 'author_name': 'Mika', 'id': 1
    }
]

const router = useRouter()

function about_course(id: number) {
    router.push(`/course-private/${id}`)
}

</script>

<template>
    <Header></Header>

    <div class="flex">
        <Aside class="w-1/4"></Aside>
        <main class="border-l border-[#101010] pl-15 pt-15 w-3/4">
            <h1 class="text-8xl">Welcome!</h1>
            <h2 class="text-5xl mt-30 ml-30">Your activated courses:</h2>
            <div class="grid grid-cols-2 ml-20 mr-10 gap-10 mt-20 mb-20">
                <div v-for="course in courses" @click="about_course(course['id'])"
                    class="bg-[#0D0D0D] border-1 border-[#262626] p-10 rounded-[4vw] shadow-xl/80 ring-2 cursor-pointer transition hover:bg-[#171717] hover:-translate-y-0.5">
                    <div class="flex items-center justify-between">
                        <div class="flex flex-col gap-4">
                            <h2 class="h2-courses ml-5 text-3xl">{{ course['name'] }}</h2>
                            <p class="short-description text-lg w-70 h-15">{{ course['short_description'] }}</p>
                        </div>
                        <img class="w-20" :src="course['image_main']" alt="python logo">
                    </div>
                    <div class="flex justify-between ml-5 mr-10 mt-5">
                        <h3 class="text-2xl">{{ course['points'] }} points</h3>
                        <p class="avtor mt-2">by {{ course['author_name'] }}</p>

                    </div>
                </div>
            </div>
        </main>
    </div>

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
.avtor {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
}

h2 {
    font-family: "Paytone One", sans-serif;
    font-weight: 400;
}

.short-description {
    color: #BBB4B4;
}

.h2-courses {
    font-family: "Inter", sans-serif;
    font-weight: 800;
}

h3 {
    color: #EC5AFF;
    font-family: "Inter", sans-serif;
    font-weight: 900;
}

.avtor {
    font-family: "Inter", sans-serif;
    font-weight: 400;
    font-style: italic;
}
</style>
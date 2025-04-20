<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

import Header from '../header.vue'
import Footer from '../footer.vue';

const courses = ref([])

const router = useRouter()

function about_course(id_course: number) {
    router.push(`/course/${id_course}`)
}

async function get_recomend_courses() {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/all_courses`)
    courses.value = response.data
}

onMounted(async () => {
    await get_recomend_courses()
})

</script>

<template>
    <Header></Header>
    <section class="courses-section mt-20 pb-40">
        <div class="flex items-center justify-between pl-40 pr-60">
            <h1 class="text-6xl">Recommended <br> Courses</h1>
            <form>
                <label for="search"
                    class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
                <div class="relative">
                    <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                        <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                        </svg>
                    </div>
                    <input type="search" id="search"
                        class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-3xl bg-[#0F0F0F] focus:ring-blue-500 focus:border-blue-500 dark:border-[#525252] dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Search" required />

                </div>
            </form>
        </div>
        <div class="grid grid-cols-3 gap-10 mx-60 mt-30">
            <div v-for="course in courses"  @click="about_course(course['id'])" class=" w-max bg-[#0D0D0D] border-1 border-[#262626] p-10 rounded-[4vw] shadow-xl/80 ring-2 cursor-pointer transition hover:bg-[#171717] hover:-translate-y-0.5">
                <div class="flex items-center justify-between">
                    <div class="flex flex-col gap-4">
                        <h2 class="h2-courses ml-5 text-3xl">{{ course['name'] }}</h2>
                        <p class="short-description text-lg w-70 h-15">{{ course['short_description'] }}</p>
                    </div>
                    <img class="w-20" :src="course['image_main']" alt="python logo">
                </div>
                <div class="flex justify-between ml-5 mr-10 mt-5">
                    <h3 class="text-2xl">{{ course['points'] }} points</h3>
                    <p class="avtor mt-2">by {{ course['author'] }}</p>

                </div>
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
h2, .avtor{
    color: white;
}

.short-description {
    color: #BBB4B4;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
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

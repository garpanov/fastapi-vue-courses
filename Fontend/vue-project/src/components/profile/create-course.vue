<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router';

import Header from '../header.vue';
import check_auth from './checkAuth';
import axios from 'axios';
import { api } from './checkAuth';
check_auth()

const router = useRouter()

type Lesson = {
    position: string,
    name: string
    description: string,
    url_video: string,
    isOpen: boolean
}

type LessonClean = {
    position: number,
    name: string
    description: string,
    url_video: string
}

type CreateCourse = {
    name: string,
    short_description: string,
    full_description: string,
    image_main: string,
    author: string,
    lessons: LessonClean[]
}

type Errors = {
    name_course: boolean,
    short_description: boolean,
    full_description: boolean,
    image_main: boolean
}

let lessons = ref<Lesson[]>([{ position: '1', name: '', description: '', url_video: '', isOpen: false }])
let lessons_clean = ref<LessonClean[]>([{ position: 1, name: '', description: '', url_video: '' }])


let data = ref<CreateCourse>({ name: '', short_description: '', full_description: '', image_main: '', author: '', lessons: lessons_clean.value })
let data_image = ref<FormData>(new FormData())
let image_error = ref<string>('')

function create_lesson() {
    let lesson_count_next: string = String(lessons.value.length + 1)
    lessons.value.push({ position: lesson_count_next, name: '', description: '', url_video: '', isOpen: true })
}

function delete_lesson(position: string) {
    lessons.value = lessons.value.filter(lesson => lesson.position !== position).map((lesson, index) => ({ ...lesson, position: String(index + 1) }))
}


const handleFileUpload = async (e: Event) => {
    const target = e.target as HTMLInputElement;
    const file = target.files?.[0];

    if (file) {
        image_error.value = file.name
        data_image.value.append('file', file)
        data_image.value.append('upload_preset', 'courses')
    }

}

async function confirm(event: Event) {
    event.preventDefault(); // ⛔ щоб не перезавантажувався браузер
    try {
        const author = localStorage.getItem('login_username')
        
        if (author) {
            data.value.author = author
        }

        data.value.lessons = lessons.value.map(({ isOpen, position, ...rest }) => ({
            ...rest,
            position: Number(position)
        }));

        const res = await axios.post(`${import.meta.env.VITE_CLOUD_RUL}`, data_image.value)

        const data_cloud = res.data
        data.value.image_main = data_cloud.secure_url

        await api.post(`${import.meta.env.VITE_API_URL}/for_profile/create_course`, data.value , { withCredentials: true })
        router.push({ name: 'profile' })
    } catch (error: any) {  // Вказуємо тип 'any' для error
        console.error('Upload Error:', error.response?.data);
    };
}
</script>

<template>
    <Header></Header>

    <main>
        <form @submit.prevent="confirm">
            <section class="px-40 py-20">
                <h1 class="text-8xl">Create course</h1>
                <div class="my-20">
                    <div class="flex justify-between items-center">
                        <div class="w-2/4 relative">
                            <div class="flex gap-10 absolute right-0">
                                <h2 class="text-5xl">Name:</h2>
                                <input v-model="data.name" id="name" aria-describedby="helper-text-explanation" required
                                    minlength="5" maxlength="15"
                                    class="border border-[#A8A8A8] text-md rounded-2xl pl-4 h-13 pr-20   placeholder-[#545454] text-white"
                                    placeholder="Name course">
                            </div>
                        </div>
                        <div class="pl-40 w-2/4">
                            <img src="/courses/create-course/name.png" alt="image name">
                        </div>
                    </div>
                </div>

                <div class="my-20">
                    <div class="flex justify-between items-center">
                        <div class="w-2/4 relative">
                            <div class="flex gap-10 absolute right-0">
                                <h2 class="text-5xl">Short description:</h2>
                                <input v-model="data.short_description" id="short description" required maxlength="40"
                                    aria-describedby="helper-text-explanation"
                                    class="border border-[#A8A8A8] text-md rounded-2xl pl-4 h-13 pr-20   placeholder-[#545454] text-white"
                                    placeholder="Short">
                            </div>
                        </div>
                        <div class="pl-40 w-2/4">
                            <img src="/courses/create-course/short description.png" alt="image short description">
                        </div>
                    </div>
                </div>

                <div class="my-20">
                    <div class="flex justify-between items-center">
                        <div class="w-2/4 relative">
                            <div class="flex gap-10 absolute right-0">
                                <h2 class="text-5xl">Full description:</h2>
                                <textarea v-model="data.full_description" id="description" required
                                    placeholder="Full description" maxlength="400"
                                    class="w-86 h-46 p-4 text-white border border-[#A8A8A8] rounded-xl placeholder-gray-500 resize-none"></textarea>
                            </div>
                        </div>
                        <div class="pl-40 w-2/4">
                            <img src="/courses/create-course/full description.png" alt="image full description">
                        </div>
                    </div>
                </div>

                <div class="mt-60 mb-20">
                    <div class="flex justify-between ">
                        <div class="w-2/4 relative">
                            <div class="flex gap-10 absolute right-0">
                                <h2 class="text-5xl">Image:</h2>
                                <div class="flex flex-col items-center space-x-4">
                                    <label for="file-upload"
                                        class="cursor-pointer flex items-center space-x-2 px-4 py-4 transition hover:opacity-80 bg-gray-600 text-white border border-gray-400 rounded-lg">
                                        <img class="w-8" src="/courses/create-course/download.png" alt="image download">
                                        <span>Select a PNG photo (Min. 150x150)</span>
                                    </label>

                                    <input @change="handleFileUpload" id="file-upload" type="file" accept="image/png"
                                        class="hidden" />
                                    <div v-if="image_error" class="text-left w-11/12 pt-1">
                                        <p class="image_error text-left">{{ image_error }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="pl-40 w-2/4">
                            <img src="/courses/create-course/image.png" alt="image logo">
                        </div>
                    </div>
                </div>
            </section>

            <hr class="border-t border-white">

            <section class="flex flex-col pt-40 pb-20 px-40 items-center" @keydown.enter.prevent>
                <div v-for="lesson in lessons"
                    :class="{ 'bg-[rgba(41,41,41,0.87)]': !lesson['isOpen'], 'bg-[rgba(41,41,41,0.37)]': lesson['isOpen'] }"
                    class="px-15 py-5 mb-20 transition-colors duration-500 w-10/12">
                    <div class="flex items-center justify-between cursor-pointer"
                        @click="lesson['isOpen'] = !lesson['isOpen']">
                        <h3 class="lesson-h3 text-5xl">Lesson {{ lesson['position'] }}</h3>
                        <img :class="{ 'rotate-0': !lesson['isOpen'], 'rotate-180': lesson['isOpen'] }"
                            class="w-17 rotate-0 transition-transform duration-500" src="/courses/arrow.png"
                            alt="arrow">
                    </div>
                    <div v-if="lesson['isOpen']">
                        <div class="my-20">
                            <div class="flex justify-between items-center">
                                <div class="w-2/4 relative">
                                    <div class="flex gap-10 absolute right-0">
                                        <h2 class="text-4xl">Name:</h2>
                                        <input v-model="lesson['name']" id="name" required minlength="5" maxlength="20"
                                            aria-describedby="helper-text-explanation"
                                            class="border border-[#A8A8A8] text-lg rounded-2xl pl-4 h-13 pr-20 placeholder-[#545454] text-white"
                                            placeholder="Name lesson">
                                    </div>
                                </div>
                                <div class="pl-40 w-2/4">
                                    <img class="w-90" src="/courses/create-course/lesson name.png"
                                        alt="image lesson name">
                                </div>
                            </div>
                        </div>

                        <div class="my-20">
                            <div class="flex justify-between items-center">
                                <div class="w-2/4 relative">
                                    <div class="flex gap-10 absolute right-0">
                                        <h2 class="text-4xl">Description:</h2>
                                        <input v-model="lesson['description']" id="short description" required
                                            minlength="10" maxlength="45" aria-describedby="helper-text-explanation"
                                            class="border border-[#A8A8A8] text-lg rounded-2xl pl-4 h-13 pr-20   placeholder-[#545454] text-white"
                                            placeholder="Description lesson">
                                    </div>
                                </div>
                                <div class="pl-40 w-2/4">
                                    <img class="w-70" src="/courses/create-course/lesson description.png"
                                        alt="image lesson description">
                                </div>
                            </div>
                        </div>

                        <div class="my-20">
                            <div class="flex justify-between items-center">
                                <div class="w-2/4 relative">
                                    <div class="flex gap-10 absolute right-0">
                                        <h2 class="text-4xl">URL video:</h2>
                                        <input v-model="lesson['url_video']" id="short description" required
                                            maxlength="500" aria-describedby="helper-text-explanation"
                                            class="border border-[#A8A8A8] text-lg rounded-2xl pl-4 h-13 pr-20   placeholder-[#545454] text-white"
                                            placeholder="Only YouTube">
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div @click="delete_lesson(lesson.position)" type="button"
                            class="flex gap-10 justify-end w-11/12 mt-30 mb-7">
                            <button
                                class="button-confirm bg-[rgba(195,195,195,0.40)] text-white py-4 px-13 text-3xl rounded-3xl cursor-pointer transition hover:bg-[rgba(195,195,195,0.50)] active:bg-[rgba(195,195,195,0.30)]">Delete</button>
                        </div>
                    </div>

                </div>
                <button @click="create_lesson" type="button"
                    class="button-add-lesson text-3xl bg-[rgba(140,140,140,0.37)] mt-20 rounded-2xl py-6 w-5/12 cursor-pointer transition hover:bg-[rgba(140,140,140,0.50)] active:bg-[rgba(140,140,140,0.30)]">Create
                    lesson</button>
            </section>

            <hr class="border-t border-white">

            <section class="py-20">
                <div class="flex justify-center">
                    <div class="flex w-7/12 justify-between">
                        <p class="p-confirm text-xl">After submitting the course, it will go through a review process,
                            <br>
                            and
                            if successful, it will be published on the website.
                        </p>
                        <button
                            class="button-confirm bg-[#B800BA] py-3 px-15 text-3xl rounded-2xl cursor-pointer transition hover:bg-[#D700DA] active:bg-[#9F00A1]">Confirm</button>
                    </div>
                </div>
            </section>
        </form>


    </main>
</template>

<style scoped>
main {
    background-image: url('/profile/background.png');
    background-size: cover;
    background-position: center;
}

h1,
h2,
.lesson-h3,
.button-add-lesson,
.button-confirm {
    color: white;
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 900;
}

h2,
span {
    font-family: "Roboto", sans-serif;
    font-weight: 500;
}

.button-add-lesson,
.p-confirm,
.button-confirm {
    font-family: "Roboto", sans-serif;
    font-weight: 800;
}

.p-confirm {
    color: #8C8C8C;
}

.lesson-h3 {
    font-family: "Roboto", sans-serif;
    font-weight: 700;
    font-style: italic;
}

.image_error {
    color: #8C8C8C;
    font-family: "Roboto", sans-serif;
    font-weight: 400;
}
</style>
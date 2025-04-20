<script setup lang="ts">
import { ref } from 'vue';
import axios, { AxiosError } from 'axios';

import Header from '../header.vue';
import { useRouter } from 'vue-router';

const router = useRouter()

let password = ref<string>('')

type Error_text = {
    status: boolean,
    text: string
}
let error_text = ref<Error_text>()

async function login(email: string | null, password: string) {
    try {
        const result = await axios.post(`${import.meta.env.VITE_API_URL}/auth/token`, { email: email, password: password }, {withCredentials: true})
        error_text.value = { 'status': false, 'text': '' }
        localStorage.setItem('login_username', result.data)
        router.push('/profile')
    } catch (error) {
        if (error instanceof AxiosError) {
            if (error.response?.data.detail == 'Not Found' || error.response?.data.detail == 'Unauthorized') {
                error_text.value = { 'status': true, 'text': 'Incorrect email or password' }
            }

        }
        else {
            error_text.value = { 'status': true, 'text': 'Unknown error, please try again later' }
        }
    }

}

async function handleLogin(event: Event) {
    event.preventDefault(); // ⛔ щоб не перезавантажувався браузер
    await login(sessionStorage.getItem('login-email-174'), password.value)
}
</script>


<template>
    <Header></Header>
    <section class="flex flex-col justify-center items-center mt-20">
        <form @submit.prevent="handleLogin"
            class="flex flex-col items-center w-3/12 px-10 pb-10 border rounded-[2.5vw] border-white">
            <div class="text-left w-full">
                <h1 class="text-7xl py-15">Log in</h1>
            </div>
            <div class="flex text-left w-11/12">
                <label for="helper-text" class="text-login block mb-2 text-xl">Enter password</label>
            </div>
            <input v-model="password" id="helper-text" type="password"
                title="Password must contain letters and numbers"
                aria-describedby="helper-text-explanation"
                class="border border-[#A8A8A8] text-lg rounded-xl block w-11/12 px-2.5 py-3  placeholder-[#545454] text-white"
                placeholder="Password">
                
            <div v-if="error_text?.status" class="text-left w-11/12 pt-1">
                <p class="p-error text-left">{{ error_text.text }}</p>
            </div>

            <button
                class="next-button py-4 w-11/12 mt-10 rounded-2xl bg-[#74005D] text-2xl transition cursor-pointer hover:bg-[#87006C] active:bg-[#680053]">Login</button>

            <div class="flex items-center my-6 w-11/12 mt-10 justify-center">
                <div class="flex-grow py-1 border-t border-white"></div>
                <span class="px-4 mb-2 text-xl">or</span>
                <div class="flex-grow border-t border-white"></div>
            </div>

            <div class="relative border border-[#9A9A9A] rounded-2xl w-11/12 py-3 px-6 text-center cursor-pointer">
                <img class="absolute w-7 mt-0.5" src="/google.png" alt="google logo">
                <h2 class="google relative text-xl mt-0.5">Continue with Google</h2>
            </div>
        </form>
        <RouterLink to="/register">
            <p class="mt-5 text-lg cursor-pointer transition">Create an account</p>
        </RouterLink>

    </section>
</template>


<style scoped>
h1,
h2,
span,
.text-login,
.next-button {
    color: white;
}

p {
    color: #F223F5;
}

.p-error {
    color: rgb(241, 0, 0);
}

h1 {
    font-family: "Roboto", sans-serif;
    font-weight: 600;
}

span {
    font-family: "Roboto", sans-serif;
    font-weight: 400;
}

.text-login,
.next-button {
    font-family: "Roboto", sans-serif;
    font-weight: 500;
}

.google,
p {
    font-family: "Roboto", sans-serif;
    font-weight: 400;
}
</style>
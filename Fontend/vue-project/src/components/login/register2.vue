<script setup lang="ts">
import axios, { AxiosError } from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import Header from '../header.vue';

const router = useRouter()

const username = ref<string>('')
const password = ref<string>('')
const confirm_password = ref<string>('')
const error_password = ref<boolean>(false)

type Error_text = {
    status: boolean,
    text: string
}
let error_text = ref<Error_text>()

async function register(username: string, password: string) {
    try {
        const result = await axios.post(`${import.meta.env.VITE_API_URL}/auth/registration`,
            {'email': sessionStorage.getItem('register-email-174'), 'password': password, 'username': username}, { withCredentials: true })

        localStorage.setItem('login_username', result.data)
        router.push('/profile')
    } catch (error) {
        if (error instanceof AxiosError) {
            if (error.response?.data.detail == 'Email already exists') {
                error_text.value = { 'status': true, 'text': 'Email already exists' }
            }

            else if (error.response?.data.detail == 'Username already exists') {
                error_text.value = { 'status': true, 'text': 'Username already exists' }
            }

            else {
                error_text.value = { 'status': true, 'text': 'Unknown error, please try again later' }
            }
        }
        else {
            error_text.value = { 'status': true, 'text': 'Unknown error, please try again later' }
        }
    }
}

async function handleLogin(event: Event) {
    event.preventDefault();
    if (password.value !== confirm_password.value) {
        error_password.value = true
        return
    }
    error_password.value = false
    await register(username.value, password.value)


}
</script>


<template>
    <Header></Header>
    <section class="flex flex-col justify-center items-center mt-20">
        <form @submit.prevent="handleLogin"
            class="flex flex-col items-center w-3/12 px-10 pb-10 border rounded-[2.5vw] border-white">
            <div class="text-left w-11/12">
                <h1 class="text-5xl py-10 leading-14">Welcome to <br> Satoshi Study</h1>
            </div>

            <div class="flex text-left w-12/12">
                <label for="username" class="text-login block mb-2 text-lg">Username</label>
            </div>
            <input v-model="username" type="text" required minlength="3" id="username"
                aria-describedby="helper-text-explanation"
                class="border border-[#A8A8A8] text-lg rounded-xl block w-12/12 px-2.5 py-3  placeholder-[#545454] text-white"
                placeholder="Username">

            <div class="flex text-left w-12/12 mt-6">
                <label for="create-password" class="text-login block mb-2 text-lg">Create a password</label>
            </div>
            <input v-model="password" required minlength="8" id="create-password" type="password"
                aria-describedby="helper-text-explanation"
                :class="{ 'border-[#A8A8A8]': !error_password, 'border-[#F10000]': error_password }"
                class="border text-lg rounded-xl block w-12/12 px-2.5 py-3  placeholder-[#545454] text-white"
                placeholder="Password">
            <div v-if="error_password" class="text-left w-full pt-1">
                <p class="p-error text-left">
                    Passwords do not match.</p>
            </div>

            <div class="flex text-left w-12/12 mt-6">
                <label for="confirm-password" class="text-login block mb-2 text-lg">Confirm password</label>
            </div>
            <input v-model="confirm_password" required minlength="8" id="confirm-password" type="password"
                aria-describedby="helper-text-explanation"
                :class="{ 'border-[#A8A8A8]': !error_password, 'border-[#F10000]': error_password }"
                class="border text-lg rounded-xl block w-12/12 px-2.5 py-3  placeholder-[#545454] text-white"
                placeholder="Confirm your password">

            <div v-if="error_password" class="text-left w-full pt-1">
                <p class="p-error text-left">
                    Passwords do not match.</p>
            </div>

            <button
                class="next-button py-4 w-12/12 mt-7 rounded-2xl bg-[#74005D] text-2xl transition cursor-pointer hover:bg-[#87006C] active:bg-[#680053]">Register</button>

            <div v-if="error_text?.status" class="text-left w-11/12 pt-1">
                <p class="p-error text-left">{{ error_text.text }}</p>
            </div>

            <div class="flex items-center my-6 w-12/12 mt-10 justify-center">
                <div class="flex-grow py-1 border-t border-white"></div>
                <span class="px-4 mb-2 text-xl">or</span>
                <div class="flex-grow border-t border-white"></div>
            </div>

            <div class="relative border border-[#9A9A9A] rounded-2xl w-12/12 py-3 px-6 text-center cursor-pointer">
                <img class="absolute w-7 mt-0.5" src="/google.png" alt="google logo">
                <h2 class="google relative text-xl mt-0.5">Continue with Google</h2>
            </div>
        </form>
        <RouterLink to="/login">
            <p class="change-login mt-5 text-xl cursor-pointer transition">Log in</p>
        </RouterLink>

    </section>
</template>


<style scoped>
h1,
h2,
span,
.text-login,
.next-button,
.accept-checkbox {
    color: white;
}

.change-login {
    color: #F223F5;
}

.p-error {
    color: rgb(241, 0, 0);
    font-family: "Roboto", sans-serif;
    font-weight: 400;
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
.change-login {
    font-family: "Roboto", sans-serif;
    font-weight: 400;
}

.accept-checkbox {
    font-family: "Roboto", sans-serif;
    font-weight: 300;
}
</style>
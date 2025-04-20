<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

import Header from '../header.vue';

const router = useRouter()
const accept = ref<boolean>(false)
const accept_error = ref<boolean>(false)

const register_session: string | null = sessionStorage.getItem('register-email-174')
let register_email = ref<string>(`${register_session}`)
const error_email = ref<boolean>(false)

async function authentication_request(email: string) {
    await axios.post(`${import.meta.env.VITE_API_URL}/auth/authentication_request_registration`, {email: email})
        .then(response => {
            error_email.value = false;
            router.push('/register/password')
        })
        .catch(error => {
            error_email.value = true
        })

}

async function handleLogin(event: Event) {
    event.preventDefault()
    if (!accept.value) {
        accept_error.value = true
        return
    }
    else {
        accept_error.value = false
        await authentication_request(register_email.value)
        sessionStorage.setItem('register-email-174', register_email.value);
    }
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
                <label for="helper-text" class="text-login block mb-2 text-xl">Email</label>
            </div>
            <input v-model="register_email" id="helper-text" aria-describedby="helper-text-explanation" type="email"
                class="border border-[#A8A8A8] text-lg rounded-xl block w-12/12 px-2.5 py-3  placeholder-[#545454] text-white"
                placeholder="name@example.com">

            <div v-if="error_email" class="text-left w-full pt-1">
                <p class="p-error text-left">
                    This email address is already registered.</p>
            </div>

            <div class="flex w-12/12 mt-7 gap-3">
                <div @click="accept = !accept" :class="{ 'bg-black': !accept, 'bg-[#EAEAEA]': accept }"
                    class="flex size-5 transition-colors rounded-sm items-center jusify-center border border-[#696969] cursor-pointer">
                    <svg v-if="accept" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-check size-5">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                        <path d="M5 12l5 5l10 -10" />
                    </svg>
                </div>
                <p class="accept-checkbox text-md tracking-wide">By creating an account, I agree to <br> Satoshi’s Terms
                    of Service and Privacy Policy.</p>
            </div>

            <div v-if="accept_error" class="text-left w-full pt-1">
                <p class="p-error text-left">
                    You need to accept our terms and privacy policy to create an account.</p>
            </div>

            <button
                class="next-button py-4 w-12/12 mt-7 rounded-2xl bg-[#74005D] text-2xl transition cursor-pointer hover:bg-[#87006C] active:bg-[#680053]">Next</button>

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
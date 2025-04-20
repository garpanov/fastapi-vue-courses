<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const is_login = ref<string | null>(localStorage.getItem('login_username'))

const router = useRouter();

const rout = (hash_word: string) => {
  router.push({ path: '/', hash: hash_word });
}

async function to_profile() {
  try {
    await axios.get(`${import.meta.env.VITE_API_URL}/auth/about_me`, { withCredentials: true })
    router.push({ name: 'profile' })
  } catch(error) {
    localStorage.removeItem('login_username')
    is_login.value = null
    router.push({ name: 'login' })
  }
}

</script>

<template>
  <header class="py-8 pl-20 pr-20 flex w-full justify-between border-b-1 border-white">
    <a href="/">
      <div class="flex gap-5 items-center cursor-pointer">
        <img src="../../public/main/logo.png">
        <h1 class="h1-header text-3xl">Satoshi Study</h1>
      </div>
    </a>
    <nav class="flex items-center">
      <ul class="navig-text flex gap-30">
        <a href="#home" @click="rout('#home')">
          <li class="text-xl cursor-pointer hover:-translate-y-0.5 hover:scale-110 transition">Home</li>
        </a>

        <a href="#about" @click="rout('#about')">
          <li class="text-xl cursor-pointer hover:-translate-y-0.5 hover:scale-110 transition">About</li>
        </a>

        <a href="#contact">
          <li class="text-xl cursor-pointer hover:-translate-y-0.5 hover:scale-110 transition">Contact</li>
        </a>
        <RouterLink to="/courses">
          <li class="text-xl cursor-pointer hover:-translate-y-0.5 hover:scale-110 transition">Courses</li>
        </RouterLink>
      </ul>
    </nav>
    <RouterLink v-if="!is_login" to="/login">
      <button class="text-button-header ml-40 text-shadow-2xs bg-[#BE00AB] text-white py-3.5 px-4.5 text-xl rounded-full cursor-pointer
                  hover:scale-102 hover:bg-[#DC00C6] active:scale-99 active:bg-[#B800A6] transition">Login</button>
    </RouterLink>
    <!-- <RouterLink v-if="is_login" to="/profile">
      <img class="w-11 opacity-80 transition hover:opacity-100 hover:scale-110" src="/profile/isLogin.png">
    </RouterLink> -->
    <img @click="to_profile" v-if="is_login" class="w-11 opacity-80 transition hover:opacity-100 hover:scale-110 cursor-pointer" src="/profile/isLogin.png">

  </header>

</template>

<style scoped>
h1,
li {
  color: white;
}

.h1-header {
  font-family: "Roboto", sans-serif;
  font-weight: 900;
}

.navig-text li {
  font-family: "Roboto", sans-serif;
  font-weight: 400;
}

.text-button-header {
  font-family: "Roboto", sans-serif;
  font-weight: 500;
}
</style>

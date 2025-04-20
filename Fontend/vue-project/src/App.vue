<script setup lang="ts">
import axios from 'axios';
import { onMounted } from 'vue';

axios.interceptors.response.use(
  response => response,
  async error => {
    if (error.response.data.detail == 'Access token expired' && error.response.status === 401) {
      try {
        await axios.get(`${import.meta.env.VITE_API_URL}/auth/refresh`, { withCredentials: true })
        return axios.request({
          ...error.config,
          withCredentials: true
        })

      } catch (refreshError) {
        localStorage.removeItem('login_username')
      }
    }
    return Promise.reject(error);
  }
);

async function preparing() {
  await axios.get(`${import.meta.env.VITE_API_URL}/auth/about_me`, { withCredentials: true })
}

onMounted(preparing)


</script>

<template>
  <router-view />
</template>

<style scoped></style>

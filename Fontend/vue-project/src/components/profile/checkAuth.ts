import axios from "axios";
import router from '../../router/index.ts'

export const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    withCredentials: true
});

api.interceptors.response.use(
    response => response,
    async error => {
        if (error.response.data && error.response.data.detail == 'Access token expired' && error.response.status === 401) {
            try {
                await axios.get(`${import.meta.env.VITE_API_URL}/auth/refresh`, { withCredentials: true })
                return axios.request({
                    ...error.config,
                    withCredentials: true
                })

            } catch (refreshError) {
                localStorage.removeItem('login_username')
                window.location.reload();
                router.push({ name: 'login' })
            }
        }
        return Promise.reject(error);
    }
);

async function check_auth() {
    if (!localStorage.getItem('login_username')) {
        router.push({ name: 'login' })
        return
    }
    try {
        await axios.get(`${import.meta.env.VITE_API_URL}/auth/about_me`, { withCredentials: true })
    } catch (error) {
        router.push({ name: 'login' })
    }
}


export default check_auth
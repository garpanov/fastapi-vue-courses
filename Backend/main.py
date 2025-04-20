from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.auth_reg import router_auth
from for_profile.request import router_profile
from for_admin.request import router_admin
from main_menu.request import router_main

app = FastAPI()
app.include_router(router_main)
app.include_router(router_auth, prefix='/auth')
app.include_router(router_profile, prefix='/for_profile')
app.include_router(router_admin, prefix='/admin')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # або ["*"] для всіх
    allow_credentials=True,
    allow_methods=["*"],  # дозволити всі методи
    allow_headers=["*"],  # дозволити всі заголовки
)

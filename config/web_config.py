# Конфигурация для веб-тестов Stellar Burgers.

BASE_URL = "https://stellarburgers.education-services.ru"
API_BASE_URL = "https://stellarburgers.education-services.ru/api"

# URL путей страниц
PAGE_PATHS = {
    "login": "/login",
    "forgot_password": "/forgot-password",
    "reset_password": "/reset-password",
    "feed": "/feed",
    "profile": "/profile"
}

ENDPOINTS = {
    "register": "/api/auth/register",
    "login": "/api/auth/login"
}


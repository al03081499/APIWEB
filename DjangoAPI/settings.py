INSTALLED_APPS += ["corsheaders", "rest_framework"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ALLOW_ALL_ORIGINS = True

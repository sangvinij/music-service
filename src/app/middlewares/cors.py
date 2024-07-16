from app.settings.settings import settings

cors_settings = {
    "allow_origins": settings.ALLOWED_HOSTS,
    "allow_credentials": True,
    "allow_methods": ["GET", "POST", "PUT", "PATCH", "DELETE"],
    "allow_headers": ["*"],
}

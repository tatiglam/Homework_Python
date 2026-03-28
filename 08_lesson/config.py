import os


class Config:
    BASE_URL = "https://ru.yougile.com/api-v2"
    TOKEN = os.getenv("YOUGILE_TOKEN", "")
    
    @classmethod
    def get_headers(cls):
        if not cls.TOKEN:
            raise ValueError("YOUGILE_TOKEN not set")
        return {
            "Authorization": f"Bearer {cls.TOKEN}",
            "Content-Type": "application/json"
        }

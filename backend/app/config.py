import os
from dotenv import load_dotenv

load_dotenv()

AMAP_KEY = os.getenv("AMAP_KEY", "your_amap_key_here")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@localhost:3306/neighbor_help"
)

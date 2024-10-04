import logging
import redis
import os
from dotenv import load_dotenv




# Start .env vars
load_dotenv()

# |----------|
# | constant |
# |----------|
# --------- Database ----------
PG_PASS = os.getenv("PG_PASS")
PG_USER = os.getenv("PG_USER")
PG_DB = os.getenv("PG_DB")
TEST_PG_DB = os.getenv("TEST_DB")
DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@postgres:5432/{PG_DB}"
# ---------------------------
# ---------- Redis ----------
EXPIRATION_TIME = os.getenv("EXPIRATION_TIME")
REDIS_CLIENT = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
# ---------------------------
# ----------- Mail ----------
MAIL_USER = os.getenv("MAIL_USER")
MAIL_PASS = os.getenv("MAIL_PASS")
# ---------------------------
# --------- Static ----------
UPLOAD_DIR = "static/img/"
# ---------------------------

# |---------|
# | Methods |
# |---------|
# ------------ Log ------------
def setup_logger(name="request_logger") -> logging.Logger:
    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    info_handler = logging.FileHandler('logs/info.txt')
    info_handler.setLevel(logging.INFO)

    error_handler = logging.FileHandler('logs/error.txt')
    error_handler.setLevel(logging.ERROR)

    warning_handler = logging.FileHandler('logs/warning.txt')
    warning_handler.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    info_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(warning_handler)

    return logger
# ---------------------------
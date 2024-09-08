from dotenv import load_dotenv

import os 

# Start .env vars
load_dotenv()

# Data to connect db
PG_PASS = os.getenv("PG_PASS")
PG_USER = os.getenv("PG_USER")
PG_DB = os.getenv("PG_DB")
TEST_PG_DB = os.getenv("TEST_DB")

DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@172.18.0.2:5432/{PG_DB}"
#!/bin/bash

alembic upgrade head

exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker server:app --bind 0.0.0.0:8000
#!/bin/bash

cd ..

alembic upgrade head

cd api

uvicorn main:app --reload

from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from models import Base
from database import engine

from routers.customers import router as router_customer
from routers.tikets import router as router_tickets

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="tz_foxford"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_customer)

app.include_router(router_tickets)

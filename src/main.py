from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from models import Base
from database import engine, get_session
from queries.tickets import fetch_open_ticket_customer, new_ticket

from routers.customers import router as router_customer
from routers.tickets import router as router_tickets
from schemas import TicketCreate

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


@app.post("/tickets/")
def add_new_ticket(model: TicketCreate, session: Session = Depends(get_session)):
    if fetch_open_ticket_customer(model.customer_id, session) is not None:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "У пользователя есть открытый тикет!!!"
        })
    else:
        new_ticket(model, session)
        return {"status": "success"}
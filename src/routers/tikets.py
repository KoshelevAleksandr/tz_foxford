from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_session
from queries import fetch_open_ticket_customer, new_ticket
from schemas import TicketCreate

router = APIRouter(
    prefix="/ticket",
    tags=["Ticket"]
)


@router.post("/tikets/")
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

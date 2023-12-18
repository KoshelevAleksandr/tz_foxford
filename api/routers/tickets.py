from typing import List

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config import TELEGRAMM_TOKEN
from database import get_session
from queries.tickets import get_all_tickets, fetch_ticket, change_ticket_status, get_chat_id_customer_by_ticket
from schemas import TicketRead

router = APIRouter(
    prefix="/ticket",
    tags=["Ticket"]
)


@router.get("/tickets/", response_model=List[TicketRead])
def get_tickets(session: Session = Depends(get_session)):
    return get_all_tickets(session)


@router.get("/tickets/{ticket_id}", response_model=List[TicketRead])
def get_one_ticket(ticket_id, session: Session = Depends(get_session)):
    return fetch_ticket(ticket_id, session)


@router.put("/tickets/{ticket_id}")
def update_ticket(ticket_id, new_status, session: Session = Depends(get_session)):
    change_ticket_status(ticket_id, new_status, session)
    chat_id = get_chat_id_customer_by_ticket(ticket_id, session)
    message = "Здесь напишите свое сообщение"
    url = f"https://api.telegram.org/bot{TELEGRAMM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    return requests.get(url).json()

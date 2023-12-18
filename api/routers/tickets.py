from typing import List

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import TELEGRAMM_TOKEN
from database import get_async_session
from queries.tickets import get_all_tickets, fetch_ticket, change_ticket_status, get_chat_id_customer_by_ticket
from schemas import TicketRead

router = APIRouter(
    prefix="/ticket",
    tags=["Ticket"]
)


@router.get("/tickets/", response_model=List[TicketRead])
async def get_tickets(session: AsyncSession = Depends(get_async_session)):
    result = await get_all_tickets(session)
    return result


@router.get("/tickets/{ticket_id}", response_model=List[TicketRead])
async def get_one_ticket(ticket_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await fetch_ticket(ticket_id, session)
    return result


@router.put("/tickets/{ticket_id}")
async def update_ticket(ticket_id: int, new_status: str, session: AsyncSession = Depends(get_async_session)):
    await change_ticket_status(ticket_id, new_status, session)
    chat_id = await get_chat_id_customer_by_ticket(ticket_id, session)
    message = "Здесь напишите свое сообщение"
    url = f"https://api.telegram.org/bot{TELEGRAMM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    return requests.get(url).json()

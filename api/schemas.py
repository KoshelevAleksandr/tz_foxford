from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class TicketStatus(str, Enum):
    open = "open"
    work = "work"
    close = "close"


class TicketCreate(BaseModel):
    status: TicketStatus
    customer_id: int
    officer_id: int


class TicketRead(TicketCreate):
    id: int
    registered_at: datetime


class CustomerCreate(BaseModel):
    telegramm_id: int
    chat_id: int


class CustomerRead(CustomerCreate):
    id: int

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


# class TicketType(Enum):
#     open = 'open'
#     work = 'work'
#     close = 'close'


class TicketCreate(BaseModel):
    status: str
    customer_id: int
    officer_id: int


class TicketRead(TicketCreate):
    id: int
    created_at: datetime


class CustomerCreate(BaseModel):
    telegramm_id: int
    chat_id: int

    # class Config:
    #     from_attributes = True


class CustomerRead(CustomerCreate):
    id: int
    # tickets: List[TicketRead]

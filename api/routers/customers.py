from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from queries.customers import get_all_customers, fetch_specific_customer, insert_customer
from schemas import CustomerRead, CustomerCreate

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)


@router.get("/customers/", response_model=List[CustomerRead])
def get_customers(session: Session = Depends(get_session)):
    return get_all_customers(session)


@router.get("/customers/{telegramm_id}", response_model=List[CustomerRead])
def get_customer(telegramm_id: int, session: Session = Depends(get_session)):
    return fetch_specific_customer(telegramm_id, session)


@router.post("/customers/")
def add_customers(model: CustomerCreate, session: Session = Depends(get_session)):
    insert_customer(model, session)
    return {"status": "success"}

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from queries.customers import get_all_customers, fetch_specific_customer, insert_customer
from schemas import CustomerRead, CustomerCreate

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)


@router.get("/customers/", response_model=List[CustomerRead])
async def get_customers(session: AsyncSession = Depends(get_async_session)):
    result = await get_all_customers(session)
    return result


@router.get("/customers/{telegramm_id}", response_model=List[CustomerRead])
async def get_customer(telegramm_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await fetch_specific_customer(telegramm_id, session)
    return result


@router.post("/customers/")
async def add_customers(model: CustomerCreate, session: AsyncSession = Depends(get_async_session)):
    result = await insert_customer(model, session)
    return {"status": "success"}

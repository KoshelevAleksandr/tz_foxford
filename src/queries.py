from fastapi import Depends
from sqlalchemy import insert, select, delete
from sqlalchemy.orm import Session

from database import get_session
from models import Customer, Ticket
from schemas import CustomerCreate


def get_all_customers(session):
    query = select(Customer)
    result = session.execute(query)
    return result.scalars()


def get_specific_customer(telegramm_id, session):
    query = select(Customer).where(Customer.telegramm_id == telegramm_id)
    result = session.execute(query)
    return result.scalars()


def insert_customer(model, session):
    stmt = insert(Customer).values(**model.dict())
    result = session.execute(stmt)
    session.commit()
    return result


def delete_customer(model, session):
    stmt = delete(Customer)
    result = session.execute(stmt)
    session.commit()
    print(result.scalars())
    return result


def new_ticket(model, session):
    stmt = insert(Ticket).values(**model.dict())
    result = session.execute(stmt)
    session.commit()
    return result


def fetch_open_ticket_customer(customer, session):
    query = select(Ticket).where(Ticket.customer_id == customer)
    result = session.execute(query)
    return result.scalars().one_or_none()


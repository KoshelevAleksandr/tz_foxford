from sqlalchemy import insert, select, update
from sqlalchemy.orm import joinedload

from models import Ticket


def get_all_tickets(session):
    query = select(Ticket)
    result = session.execute(query)
    return result.scalars()


def fetch_ticket(ticket_id, session):
    query = select(Ticket).where(Ticket.id == ticket_id)
    result = session.execute(query)
    return result.scalars()


def new_ticket(model, session):
    stmt = insert(Ticket).values(**model.dict())
    result = session.execute(stmt)
    session.commit()
    return result


def fetch_open_ticket_customer(customer, session):
    query = select(Ticket).where(Ticket.customer_id == customer, Ticket.status == 'open')
    result = session.execute(query)
    return result.scalars().one_or_none()


def change_ticket_status(ticket_id, new_status, session):
    stmt = update(Ticket).where(Ticket.id == ticket_id).values(status=new_status)
    result = session.execute(stmt)
    session.commit()
    return result


def get_chat_id_customer_by_ticket(ticket_id, session):
    stmt = select(Ticket).options(joinedload(Ticket.customer, innerjoin=True)).where(Ticket.id == ticket_id).order_by(
        Ticket.id)
    ticket = session.execute(stmt).scalars().first()
    chat_id = ticket.customer.telegramm_id
    return chat_id

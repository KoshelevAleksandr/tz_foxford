from sqlalchemy import insert, select, delete

from models import Customer


def get_all_customers(session):
    query = select(Customer)
    result = session.execute(query)
    return result.scalars()


def fetch_specific_customer(telegramm_id, session):
    query = select(Customer).where(Customer.telegramm_id == telegramm_id)
    result = session.execute(query)
    return result.scalars()


def insert_customer(model, session):
    stmt = insert(Customer).values(**model.dict())
    result = session.execute(stmt)
    session.commit()
    return result


def delete_customer(customer_id, session):
    stmt = delete(Customer).where(Customer.id == customer_id)
    result = session.execute(stmt)
    session.commit()
    return result

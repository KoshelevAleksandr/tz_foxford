from sqlalchemy import insert, select, delete

from models import Customer


async def get_all_customers(session):
    query = select(Customer)
    result = (await session.execute(query)).scalars()
    return result


async def fetch_specific_customer(telegramm_id, session):
    query = select(Customer).where(Customer.telegramm_id == telegramm_id)
    result = (await session.execute(query)).scalars()
    return result


async def insert_customer(model, session):
    stmt = insert(Customer).values(**model.dict())
    result = await session.execute(stmt)
    await session.commit()
    return result


async def delete_customer(customer_id, session):
    stmt = delete(Customer).where(Customer.id == customer_id)
    result = await session.execute(stmt)
    await session.commit()
    return result

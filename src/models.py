from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from auth.models import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegramm_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)

    tikets = relationship("Ticket", back_populates="customer")


class Ticket(Base):
    __tablename__ = "tiket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    officer_id = Column(Integer, ForeignKey("user.id"), default=None)

    customer = relationship("Customer", back_populates='tikets')

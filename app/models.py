from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# back_populates is used to tell SQLAlchemy that the relationship is bidirectional aka tells SQLModel that if something changes in this model, it should change that attribute in the other model, and vice versa.


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=True)

    # add "todos" to the back_populates argument of Todos
    todos = relationship("Todos", back_populates="owner")

    address = relationship("Address", back_populates="user_address")


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # add owner to the back_populates argument of Users
    owner = relationship("Users", back_populates="todos")


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postalcode = Column(String)

    user_address = relationship("Users", back_populates="address")

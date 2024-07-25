from .database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship

class User(Base) :
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(Integer, nullable=False)
    
class Product(Base) :
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(300), nullable=False)
    image1 = Column(String(300), nullable=False)
    image2 = Column(String(300), nullable=True)
    image3 = Column(String(300), nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    stock = Column(Integer, nullable=False)
    size = Column(String(20), nullable=False)
    new = Column(Integer, nullable=False)
    
class Order(Base) :
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    products = Column(String(300), nullable=False)
    paid = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(300), nullable=False)
    order_description = Column(String(300), nullable=True)
    method = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=True)
    
class Category(Base) :
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
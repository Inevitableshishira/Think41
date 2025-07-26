from sqlalchemy import Column, Integer, String, Float
from db import Base

# Products Table
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    brand = Column(String)
    retail_price = Column(Float)

# Inventory Items Table
class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    created_at = Column(String)
    sold_at = Column(String)
    product_name = Column(String)

# Order Items Table
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    status = Column(String)
    delivered_at = Column(String)
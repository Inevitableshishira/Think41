from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from db import Base
from datetime import datetime

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
    
class ChatUser(Base):
    __tablename__ = 'chat_users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class ChatSession(Base):
    __tablename__ = 'chat_sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('chat_users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('chat_sessions.id'))
    sender = Column(String)  # 'user' or 'ai'
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

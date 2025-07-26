import pandas as pd
from db import SessionLocal, engine
from models import Product, InventoryItem, OrderItem
from db import Base

# 1. Create DB tables
Base.metadata.create_all(bind=engine)

# 2. Connect to DB
db = SessionLocal()

# 3. Load products.csv
df_products = pd.read_csv("data/products.csv")
for _, row in df_products.iterrows():
    db.add(Product(
        id=row["id"],
        name=row["name"],
        category=row["category"],
        brand=row["brand"],
        retail_price=row["retail_price"]
    ))

# 4. Load inventory_items.csv
df_inventory = pd.read_csv("data/inventory_items.csv")
for _, row in df_inventory.iterrows():
    db.add(InventoryItem(
        id=row["id"],
        product_id=row["product_id"],
        created_at=row["created_at"],
        sold_at=row["sold_at"],
        product_name=row["product_name"]
    ))

# 5. Load order_items.csv
df_orders = pd.read_csv("data/order_items.csv")
for _, row in df_orders.iterrows():
    db.add(OrderItem(
        id=row["id"],
        order_id=row["order_id"],
        product_id=row["product_id"],
        status=row["status"],
        delivered_at=row["delivered_at"]
    ))

# 6. Save to DB
db.commit()
db.close()
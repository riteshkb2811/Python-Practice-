from sqlalchemy import Column, Integer, String, Float
from db import Base

class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    product_price = Column(Float, nullable=False)
    product_stock = Column(Integer, nullable=False)

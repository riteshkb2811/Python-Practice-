from email.policy import default
from pydantic import BaseModel
class Products(BaseModel):
    id:int
    product_name:str   
    product_price:float
    product_stock:int

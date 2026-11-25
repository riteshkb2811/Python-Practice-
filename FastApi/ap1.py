from fastapi import FastAPI,Depends
from model import Products                  # Pydantic schema for validation
from database_models import Base, ProductDB # SQLAlchemy DB models
from db import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

app = FastAPI()

# Creates the tables in MySQL
Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcomne to Ritesh"

product = [
    Products(id=1, product_name="ritesh", product_price=100, product_stock=10),
    Products(id=2, product_name="ritesh", product_price=100, product_stock=10),
    Products(id=3, product_name="ritesh", product_price=100, product_stock=-10),
    Products(id=4, product_name="ritesh", product_price=100, product_stock=10),
    Products(id=5, product_name="ritesh", product_price=100, product_stock=10)
]

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def init():
    db = SessionLocal()
    try:
        # Only populate if the table is empty
        if db.query(ProductDB).count() == 0:
            for i in product:
                db.add(ProductDB(**i.model_dump()))
            db.commit()
    finally:
        db.close()

init()

@app.get("/product")
def abc(db : Session = Depends(get_db)):
    return db.query(ProductDB).all()
     
@app.get("/product/{id}")
def getproduct(id: int,db:Session=Depends(get_db)):
    a=db.query(ProductDB).all()
    for i in a:
        if i.id == id:
            return db.query(ProductDB).filter(ProductDB.id == id).first()
    return "Product not found"

@app.post("/product")
def addProduct(prod: Products,db:Session=Depends(get_db)): 
    db.add(ProductDB(**prod.model_dump()))
    db.commit()
    db.refresh(prod)
    return prod  

@app.put("/product/{id}")
def updateProd(id: int, prod: Products,db:Session=Depends(get_db)):
    db.query(ProductDB).filter(ProductDB.id == id).update({
        ProductDB.product_name: prod.product_name,
        ProductDB.product_price: prod.product_price,
        ProductDB.product_stock: prod.product_stock
    })
    db.commit()
    db.refresh(prod)
    return prod

@app.delete("/product/{id}")
def delprod(id: int,db:Session=Depends(get_db)):
    db.query(ProductDB).filter(ProductDB.id == id).delete()
    db.commit()
    return "Product deleted successfully"

@app.get("/product1")
def getname(name:str=None):
      return {"Name":name}    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ap1:app", host="localhost", port=8000, reload=True)

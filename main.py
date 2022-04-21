import uvicorn
from fastapi import FastAPI
from product_module import product_controller

# from database import SessionLocal

app = FastAPI()
app.include_router(product_controller.router)

# db = SessionLocal()

if __name__ == '__main__':
    uvicorn.run(app, port=4000)

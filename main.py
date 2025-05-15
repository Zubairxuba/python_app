from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from router import router
from database import Base, engine
from models.userModel import User
from models.blogsModel import Blog
from models.commentModel import Comment


app = FastAPI()

# Initialize database on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# Include the router
app.include_router(router)

# Create handler for AWS Lambda
def handler(event, context):
    return app(event, context)
from typing import List, Optional
from sqlalchemy.orm import Session
from models.userModel import User as UserModel
from domain.models import User
from repositories.baseRepository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)
    
    def get_all(self):
        db_users = self.db.query(UserModel).all()
        if db_users:
            return db_users
        else:
            return []
    
    def get_by_id(self, id: int):
        db_user = self.db.query(UserModel).filter(UserModel.id == id).first()
        return db_user

    def create(self, user: User) -> User:
        db_user = UserModel(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def check_email(self, email: str):
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return db_user is not None


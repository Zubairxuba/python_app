from typing import List, Optional
from domain.models import User
from repositories.userRepository import UserRepository

class UserService :
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def get_all_users(self):
        return self.user_repository.get_all()
    
    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, name: str, email: str):
        if not name or not email:
            raise ValueError("Name and email are required")
        
        existing_email = self.user_repository.check_email(email)

        if existing_email:
            return {"error": "User with this email already exists"}

        print("user_repository")
        print(name, email)
        # Create a User object before passing to repository
        user = User(name=name, email=email)
        return self.user_repository.create(user)
    
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from models.blogsModel import Blog
from repositories.baseRepository import BaseRepository

class BlogRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)
    
    def get_all(self):
        return self.db.query(Blog).all()
    
    def get_by_id(self, id: int):
        return self.db.query(Blog).options(joinedload(Blog.author), joinedload(Blog.comments)).filter(Blog.id == id).first()
    
    def create_blog(self, blog: Blog) -> Blog:
        db_blog = Blog(title=blog.title, content=blog.content, userId=blog.userId)

        print("blog==========================================================================+++++++++++++++++++++++++++++++++++++++++++++=" )
        self.db.add(db_blog)
        self.db.commit()
        self.db.refresh(db_blog)
        return db_blog
    

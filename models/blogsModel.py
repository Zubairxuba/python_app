from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
        __tablename__ = "blogs"
        
        id = Column(Integer, primary_key=True, index=True)
        title = Column(String, index=True)
        content = Column(String, index=True)
        userId = Column(Integer, ForeignKey("users.id"))
        
        author = relationship("User", back_populates="blogs")
        comments = relationship("Comment", back_populates="blog")
        
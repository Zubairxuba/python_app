from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Comment(Base):
            __tablename__ = "comments"
            id = Column(Integer, primary_key=True, index=True)
            text = Column(String, index=True)
            blogId = Column(Integer, ForeignKey("blogs.id"))
            userId = Column(Integer, ForeignKey("users.id"))
            user = relationship("User", back_populates="comments")
            blog = relationship("Blog", back_populates="comments")
            
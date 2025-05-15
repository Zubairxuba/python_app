from sqlalchemy.orm import Session, joinedload
from models.commentModel import Comment
from repositories.baseRepository import BaseRepository

class CommentRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)
    
    def get_all(self):
        return self.db.query(Comment).all()

    def create(self, comment: Comment):
        db_comment = Comment(text=comment.text, blogId=comment.blogId, userId=comment.userId)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return db_comment
    
    
    def get_comment_by_id(self, commentId: int):
        return self.db.query(Comment).options(joinedload(Comment.user), joinedload(Comment.blog)).filter(Comment.id == commentId).first()
    

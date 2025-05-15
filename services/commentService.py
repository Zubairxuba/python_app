from domain.models import Comment
from repositories.commentsRepository import CommentRepository

class CommentService:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository
    
    def create_comment(self, text: str, blogId: int, userId: int):
        comment = Comment(text=text, blogId=blogId, userId=userId)
        return self.comment_repository.create(comment)
    
    def get_comment(self, commentId: int):
        return self.comment_repository.get_by_id(commentId)

    def get_blog_comments(self, blogId: int):
        return self.comment_repository.get_by_blog_id(blogId)  
    
    def get_user_comments(self, userId: int):
        return self.comment_repository.get_by_user_id(userId)  
    
    def get_all_comments(self):
        return self.comment_repository.get_all()    
    
    def get_comment_by_id(self, commentId: int):
        return self.comment_repository.get_comment_by_id(commentId)
    
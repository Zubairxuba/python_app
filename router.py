from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.userModel import User
from models.blogsModel import Blog
from models.commentModel import Comment
from database import SessionLocal
from services.userService import UserService
from services.blogService import BlogService
from services.commentService import CommentService
from repositories.userRepository import UserRepository
from repositories.blogsRepository import BlogRepository
from repositories.commentsRepository import CommentRepository
from pydantic import BaseModel

router = APIRouter()

# Request Models
class UserCreate(BaseModel):
    name: str
    # email: str

class BlogCreate(BaseModel):
    title: str
    content: str
    userId: int

class CommentCreate(BaseModel):
    text: str
    blogId: int
    userId: int

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User routes
@router.get("/users/")
def get_users(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.get_all_users()

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.create_user(user.name, user.email)

# Blog routes
@router.get("/blogs/")
def get_blogs(db: Session = Depends(get_db)):
    blog_repository = BlogRepository(db)
    blog_service = BlogService(blog_repository)
    return blog_service.get_all_blogs()


# get blogs by id with its author and comments
@router.get("/blogs/{blog_id}/")
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog_repository = BlogRepository(db)
    blog_service = BlogService(blog_repository)
    return blog_service.get_blog_by_id(blog_id)


@router.post("/blogs/")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    print("blog==========================================================================+++++++++++++++++++++++++++++++++++++++++++++=" )
    blog_repository = BlogRepository(db)
    blog_service = BlogService(blog_repository)
    return blog_service.create_blog(blog.title, blog.content, blog.userId)






# Comment routes
@router.get("/comments/")
def get_comments(db: Session = Depends(get_db)):
    comment_repository = CommentRepository(db)
    comment_service = CommentService(comment_repository)
    return comment_service.get_all_comments()


@router.get("/comments/{comment_id}/")
def get_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    comment_repository = CommentRepository(db)
    comment_service = CommentService(comment_repository)
    return comment_service.get_comment_by_id(comment_id)



@router.post("/comments/")
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    comment_repository = CommentRepository(db)
    comment_service = CommentService(comment_repository)
    return comment_service.create_comment(comment.text, comment.blogId, comment.userId)

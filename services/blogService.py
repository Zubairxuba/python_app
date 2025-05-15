
from repositories.blogsRepository import BlogRepository 
from domain.models import Blog
class BlogService:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository
    
    def create_blog(self, title: str, content: str, user_id: int):
        print("blog_repository")
        print(title, content, user_id)
        blog = Blog(title=title, content=content, userId=user_id)
        return self.blog_repository.create_blog(blog)

    def get_blog(self, blog_id: int):
        return self.blog_repository.get_by_id(blog_id)
    
    def get_all_blogs(self):
        return self.blog_repository.get_all()
    
    def get_blog_by_id(self, blog_id: int):
        return self.blog_repository.get_by_id(blog_id)
    
    
    
    
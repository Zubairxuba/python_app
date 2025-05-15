from dataclasses import dataclass
from typing import List, Optional

@dataclass
class User:
    name: str
    email: str
    id: Optional[int] = None
    blogs: List['Blog'] = None
    comments: List['Comment'] = None

@dataclass
class Blog:
    title: str
    content: str
    userId: int
    author: Optional[User] = None
    comments: List['Comment'] = None

@dataclass
class Comment:
    text: str
    blogId: int
    userId: int
    user: Optional[User] = None
    blog: Optional[Blog] = None 
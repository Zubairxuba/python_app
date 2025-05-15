from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[T]:
        raise NotImplementedError
    
    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError
    
    def create(self, entity: T) -> T:
        raise NotImplementedError
    
    def update(self, entity: T) -> T:
        raise NotImplementedError
    
    def delete(self, id: int) -> bool:
        raise NotImplementedError 
from pydantic import BaseModel
from typing import Optional

# description: Optional[str]          # type allows None, but field is still REQUIRED
# description: Optional[str] = None   # type allows None, AND it's optional to provide
# description: str = None             # ⚠️ type says str only, but default breaks that rule
class StudentBase(BaseModel):
    studentName: str
    studentAdd: Optional[str] = None

class CreateStudent(StudentBase):
    pass

class UpdateStudent(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int

# pass means "add nothing new, just inherit everything from ItemBase

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

# class ItemUpdate(ItemBase):
#     name: Optional[str] = None   # allow updating only some fields, not all


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True   # lets Pydantic read SQLAlchemy objects

# With from_attributes = True, you're telling Pydantic: "It's fine, just reach into this object's .name, .id, .price attributes directly instead of expecting a dict
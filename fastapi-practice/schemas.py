from pydantic import BaseModel
from typing import Optional

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
%%file models.py
import pydantic
from datetime import datetime

class User(pydantic.BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: pydantic.EmailStr
    password: str
    phone: str = ""
    userStatus: int
  
class Category(pydantic.BaseModel):
    id: int
    name: str

class Pet(pydantic.BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list
    tags: list
    status: str = pydantic.Field(..., regex="^(available|pending|sold)$")

class Order(pydantic.BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: datetime
    status: str = pydantic.Field(..., regex="^(placed|approved|delivered)$")
    complete: bool

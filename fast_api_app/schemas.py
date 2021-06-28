from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

#Farm Visited
class FarmsVisitedBase(BaseModel):
    frm_visited_date : datetime
    FARM_frm_visited_id: int
    USER_frm_visited_id : int

class FarmVisitedCreate(FarmsVisitedBase):
    pass

class  FarmVisited(FarmsVisitedBase):
    frm_visited_id: int
    class Config:
        orm_mode = True
#Farm
class FarmBase(BaseModel):
    frm_name: str
    frm_created: datetime

class FarmCreate(FarmBase):
    pass

class Farm(FarmBase):
    frm_id: int
    FARM_TYPES_frm_id : int
    REGION_frm_id: int

    class Config:
        orm_mode = True

#FarmType
class FarmTypeBase(BaseModel):
    frm_type_name : str
    frm_type_created: datetime

class FarmTypeCreate(FarmTypeBase):
    pass

class FarmType(FarmTypeBase):
    frm_type_id: int
    frm_type_enabled: bool

    class Config:
        orm_mode = True

#Region
class RegionBase(BaseModel):
    reg_name: str
    reg_created: datetime

class RegionCreate(RegionBase):
    pass

class Region(RegionBase):
    reg_id: int

    class Config:
        orm_mode = True


#Item
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


#User 
class UserBase(BaseModel):
    email: str
    usr_username : str
    password: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    usr_username: str

    class Config:
        orm_mode = True

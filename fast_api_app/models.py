from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, JSON, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import insert

from .database import Base




class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(32), unique=True, index=True)
    usr_username = Column(String(45))
    hashed_password = Column(String(32))
    usr_name = Column(String(45))
    usr_lastname = Column(String(45))
    usr_created = Column(TIMESTAMP)
    usr_updated = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")



class Item(Base):

    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32), index=True)
    description = Column(String(32), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class FarmType(Base):
        __tablename__ = 'farm_types'

        frm_type_id = Column(Integer, primary_key=True)
        frm_type_name = Column(String(45), nullable=False)
        frm_type_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        frm_type_enabled = Column(Integer, nullable=False, default=True)

        
class Region(Base):
        __tablename__ = 'regions'

        reg_id = Column(Integer, primary_key=True)
        reg_name = Column(String(45), nullable=False)
        reg_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        reg_updated = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        reg_enabled = Column(Integer, nullable=False,server_default=text("1"))



class Farm(Base):
        __tablename__ = 'farms'

        frm_id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
        frm_name = Column(String(45), nullable=False)
        frm_restriction = Column(JSON)
        frm_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        frm_updated = Column(TIMESTAMP)
        frm_enabled = Column(Integer, nullable=False, default=1)
        FARM_TYPES_frm_id = Column(ForeignKey('farm_types.frm_type_id'), primary_key=True, nullable=False, index=True)
        REGION_frm_id = Column(ForeignKey('regions.reg_id'), primary_key=True, nullable=False, index=True)

        FARM_TYPES_frm = relationship('FarmType')
        REGION_frm = relationship('Region')


class FarmsVisited(Base):
        __tablename__ = 'farms_visited'

        frm_visited_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
        frm_visited_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
        FARM_frm_visited_id = Column(ForeignKey('farms.frm_id'), primary_key=True, nullable=False, index=True)
        USER_frm_visited_id = Column(ForeignKey('users.id'), primary_key=True, nullable=False, index=True)

        FARM_frm_visited = relationship('Farm')
        USER_frm_visited = relationship('User')

    # coding: utf-8
"""     from sqlalchemy import CHAR, Column, ForeignKey, JSON, String, TIMESTAMP, text
    from sqlalchemy.dialects.mysql import BIT, Integer, TINYINT
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    metadata = Base.metadata


    class FarmType(Base):
        __tablename__ = 'farm_types'

        frm_type_id = Column(TINYINT, primary_key=True)
        frm_type_name = Column(String(45), nullable=False)
        frm_type_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        frm_type_enabled = Column(BIT(2), nullable=False)


    class Region(Base):
        __tablename__ = 'regions'

        reg_id = Column(TINYINT, primary_key=True)
        reg_name = Column(String(45), nullable=False)
        reg_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        reg_updated = Column(TIMESTAMP)
        reg_enabled = Column(BIT(2))


    class Farm(Base):
        __tablename__ = 'farms'

        frm_id = Column(Integer, primary_key=True, nullable=False)
        frm_name = Column(String(45), nullable=False)
        frm_restriction = Column(JSON)
        frm_created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
        frm_updated = Column(TIMESTAMP)
        frm_enabled = Column(BIT(2), nullable=False)
        REGION_frm_id = Column(ForeignKey('regions.reg_id'), primary_key=True, nullable=False, index=True)
        FARM_TYPES_frm_id = Column(ForeignKey('farm_types.frm_type_id'), primary_key=True, nullable=False, index=True)

        FARM_TYPES_frm = relationship('FarmType')
        REGION_frm = relationship('Region')


    class User(Base):
        __tablename__ = 'users'

        usr_id = Column(INTEGER, primary_key=True, nullable=False)
        usr_username = Column(String(45), nullable=False)
        usr_password = Column(CHAR(32))
        user_name = Column(String(45))
        usr_lastname = Column(String(45))
        usr_created = Column(TIMESTAMP)
        usr_updated = Column(TIMESTAMP)
        REGION_usr_id = Column(ForeignKey('regions.reg_id'), primary_key=True, nullable=False, index=True)

        REGION_usr = relationship('Region')


    class FarmsVisited(Base):
        __tablename__ = 'farms_visited'

        frm_visited_id = Column(INTEGER, primary_key=True, nullable=False)
        frm_visited_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
        FARM_frm_visited_id = Column(ForeignKey('farms.frm_id'), primary_key=True, nullable=False, index=True)
        USER_frm_visited_id = Column(ForeignKey('users.usr_id'), primary_key=True, nullable=False, index=True)

        FARM_frm_visited = relationship('Farm')
        USER_frm_visited = relationship('User') """
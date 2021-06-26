from sqlalchemy.orm import Session



from . import models, schemas




def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, usr_username=user.usr_username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Regions
def get_regions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Region).offset(skip).limit(limit).all()

def get_region(db: Session, reg_id: int):
    return db.query(models.Region).filter(models.Region.reg_id == reg_id).first()


def create_region(db: Session, region: schemas.RegionCreate):
    db_region = models.Region(reg_name=region.reg_name, reg_created=region.reg_created )
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region
    
#Farms Visited
def create_farm_visited(db: Session, farm_visited: schemas.FarmVisitedCreate):
    db_farm_visited = models.FarmsVisited(frm_visited_date=farm_visited.frm_visited_date, FARM_frm_visited_id=farm_visited.FARM_frm_visited_id, USER_frm_visited_id=farm_visited.USER_frm_visited_id)
    db.add(db_farm_visited)
    db.commit()
    db.refresh(db_farm_visited)
    return db_farm_visited

def get_farm_visited(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.FarmsVisited).offset(skip).limit(limit).all()

#Granjas, Typo de Granjas, Regiones
def create_region_farm(db: Session, farm: schemas.FarmCreate, reg_id: int, frm_type_id: int):
    db_farm = models.Farm(**farm.dict(), REGION_frm_id=reg_id, FARM_TYPES_frm_id=frm_type_id)
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm


def create_farm_type(db: Session, farm_type: schemas.FarmTypeCreate):
    db_farm_type = models.FarmType(frm_type_name=farm_type.frm_type_name, frm_type_created=farm_type.frm_type_created)
    db.add(db_farm_type)
    db.commit()
    db.refresh(db_farm_type)
    return db_farm_type


def get_farm_type(db: Session, farm_type_id: int):
    return db.query(models.FarmType).filter(models.FarmType.frm_type_id == farm_type_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



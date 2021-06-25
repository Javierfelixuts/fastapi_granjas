from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI(debug=True)


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://10.0.0.24:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Agregar un usuario unico
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users




@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


#REGION
#Obtener una region por medio del id
@app.get('/region/{reg_id}', response_model=schemas.Region)
def read_region(reg_id: int, db: Session = Depends(get_db)):
    db_region = crud.get_region(db, reg_id=reg_id)
    return db_region

#Obtener un listado de regions con un rango 0 - 100
@app.get("/regions/", response_model=List[schemas.Region])
def read_regions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    regions = crud.get_regions(db, skip=skip, limit=limit)
    return regions

#Agregar una region
@app.post("/regions/", response_model=schemas.Region)
def create_region(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    db_region = crud.create_region(db=db, region=region)

    return db_region


#Agreagr item
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
#Agregar Granja sabiendo el id de la region
@app.post("/regions/{reg_id}/farms/{frm_type_id}", response_model=schemas.Farm)
def create_farm_for_region(
    reg_id: int, frm_type_id: int, farm: schemas.FarmCreate, db: Session = Depends(get_db)
):
    return crud.create_region_farm(db=db, farm=farm, reg_id=reg_id, frm_type_id=frm_type_id)

#Agregar un tipo de granja
@app.post("/farm_type/", response_model=schemas.FarmType)
def create_farm_type(farm_type: schemas.FarmTypeCreate, db: Session = Depends(get_db)):
    db_farm_type = crud.create_farm_type(db=db, farm_type=farm_type)

    return db_farm_type

@app.post("/farm_visited/", response_model=schemas.FarmVisited)
def create_far_visited(farm_visited: schemas.FarmVisitedCreate, db: Session = Depends(get_db)):
    db_farm_visited = crud.create_farm_visited(db=db, farm_visited=farm_visited)

    return db_farm_visited

@app.get("/farm_visited/", response_model=List[schemas.FarmVisited])
def read_farm_visited(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    farm_visited = crud.get_farm_visited(db, skip=skip, limit=limit)
    return farm_visited


@app.get("/farm_type/{farm_type_id}", response_model=schemas.FarmType)
def read_farm_type(farm_type_id: int, db: Session = Depends(get_db)):
    db_farm_type = crud.get_farm_type(db, farm_type_id=farm_type_id)
    return db_farm_type


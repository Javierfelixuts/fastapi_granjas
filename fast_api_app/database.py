from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ojaialim@localhost:@162.241.62.125:2083/ojaialim_visita_granjas"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://eigvzozhsppyzp:48666d080fd22f82f7a643f44a9edfb187f4022eac4c0e737cb10891b629486d@ec2-3-214-136-47.compute-1.amazonaws.com:5432/d1ftdum8f76d8f"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

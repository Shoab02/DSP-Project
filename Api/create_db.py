from db import Base,engine
from db_model import Car


print("Creating database ...")


Base.metadata.create_all(engine)
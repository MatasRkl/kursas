from class_material.db_alchemy_paskaita import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/projects.db')
Session = sessionmaker(bind=engine)
session = Session()

project = Project(
    name='Nike jacket',
    price='5.99'
)

session.add(project)
session.commit()
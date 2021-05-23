from sqlalchemy import Column, Integer, String, Float

from app.utils.session import Base


class BeerParamsModel(Base):
    __tablename__ = 'BeerParams'
    # __table_args__ = {'schema': 'beer'}  # Not available via sqllite
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  # Put constraint for the name to be unique
    percentage_alcohol = Column(Float, nullable=False)
    color = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __init__(self, name, percentage_alcohol, color, type):
        self.name = name
        self.percentage_alcohol = percentage_alcohol
        self.color = color
        self.type = type

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return str(cls.__name__).lower() + "s"

from .companies import Company
from .jobs import Job
from .users import User
from .resume import Resume
from .aplications import Application



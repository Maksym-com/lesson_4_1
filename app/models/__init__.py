from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return str(cls.__name__).lower() + "s"
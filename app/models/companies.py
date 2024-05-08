from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

from . import Base


class Company(Base, UserMixin):
    __tablename__ = 'companies'
    id: Mapped['int'] = mapped_column(primary_key=True)
    name: Mapped['str'] = mapped_column()
    email: Mapped['str'] = mapped_column(unique=True)
    password: Mapped['str'] = mapped_column(String(24))
    description: Mapped['str'] = mapped_column(String(1000), nullable=True)
    address: Mapped['str'] = mapped_column(nullable=True)
    phone: Mapped['str'] = mapped_column(nullable=True)
    website: Mapped['str'] = mapped_column(nullable=True)
    users = relationship("User", back_populates="company")
    jobs = relationship("Job", back_populates="company")
    date_joined = mapped_column(DateTime)
    is_active: Mapped['bool'] = mapped_column(default=True)



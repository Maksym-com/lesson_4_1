from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from flask_login import UserMixin
from . import Base


class User(Base, UserMixin):
    id: Mapped['int'] = mapped_column(primary_key=True)
    username: Mapped['str'] = mapped_column(unique=True)
    name: Mapped['str'] = mapped_column()
    last_name: Mapped['str'] = mapped_column()
    birth_date = mapped_column(DateTime)
    email: Mapped['str'] = mapped_column(unique=True)
    password: Mapped['str'] = mapped_column()
    company_id: Mapped['int'] = mapped_column(Integer, ForeignKey('companies.id'), nullable=True)
    company = relationship("Company", back_populates="users")
    resumes = relationship("Resume", back_populates="user")
    applications = relationship("Application", back_populates="user")
    img: Mapped['str'] = mapped_column(nullable=True)
    date_joined = mapped_column(DateTime)
    is_active: Mapped["bool"] = mapped_column(default=True)

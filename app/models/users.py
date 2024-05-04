from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from . import Base

class User(Base):
    user_id: Mapped['int'] = mapped_column(primary_key=True)
    username: Mapped['str'] = mapped_column(unique=True)
    name: Mapped['str'] = mapped_column()
    last_name: Mapped['str'] = mapped_column()
    age: Mapped['int'] = mapped_column()
    email: Mapped['str'] = mapped_column()
    password: Mapped['str'] = mapped_column()
    company_id: Mapped['int'] = mapped_column(Integer, ForeignKey('companies.company_id'), nullable=True)
    company = relationship("Company", back_populates="users")
    resumes = relationship("Resume", back_populates="user")
    applications = relationship("Application", back_populates="user")
    date_joined = mapped_column(DateTime)
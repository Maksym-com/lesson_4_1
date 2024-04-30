from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from . import Base

class User(Base):
    user_id: Mapped['int'] = mapped_column(PrimaryKey=True)
    name: Mapped['str'] = mapped_column()
    last_name: Mapped['str'] = mapped_column()
    age: Mapped['int'] = mapped_column()
    email: Mapped['str'] = mapped_column()
    password: Mapped['str'] = mapped_column()
    company_id: Mapped['int'] = mapped_column(Integer, ForeignKey('companies.company_id'))
    company = relationship("Company", back_populates="users")
    resume = relationship("Resume")
    date_joined = mapped_column(DateTime)
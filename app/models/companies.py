from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import Mapped, mapped_column
from . import Base

class Company(Base):
    __tablename__ = 'companies'
    company_id: Mapped['int'] = mapped_column(primary_key=True)
    name: Mapped['str'] = mapped_column(String(24), Unique=True)
    email: Mapped['str'] = mapped_column(Unique=True)
    password: Mapped['str'] = mapped_column(String(24))
    description: Mapped['str'] = mapped_column(String(1000))
    address: Mapped['str'] = mapped_column()
    phone: Mapped['str'] = mapped_column()
    website: Mapped['str'] = mapped_column()
    users = relationship("User", back_populates="company")




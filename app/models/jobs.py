from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

class Job(Base):
    job_id: Mapped['int'] = mapped_column(primary_key=True)
    title: Mapped['str'] = mapped_column()
    description: Mapped['str'] = mapped_column()
    requirements: Mapped['str'] = mapped_column()
    publication_date = mapped_column(DateTime)
    company_id: Mapped['int'] = mapped_column(ForeignKey('companies.company_id'))
    company = relationship("Company", back_populates="jobs")
    applications = relationship("Application", back_populates="job")
    category: Mapped['str'] = mapped_column()
    experience: Mapped['int'] = mapped_column()
    sphere: Mapped['str'] = mapped_column()
    location: Mapped['str'] = mapped_column()
    salary: Mapped['int'] = mapped_column()

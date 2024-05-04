from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

class Application(Base):
    application_id: Mapped['int'] = mapped_column(primary_key=True)
    job_id: Mapped['int'] = mapped_column(ForeignKey('jobs.job_id'))
    user_id: Mapped['int'] = mapped_column(ForeignKey('users.user_id'))
    application_date = mapped_column(DateTime)
    status: Mapped['int'] = mapped_column()
    job = relationship("Job", back_populates="applications")
    user = relationship("User", back_populates="applications")
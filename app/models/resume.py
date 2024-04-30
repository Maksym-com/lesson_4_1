from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

class Resume(Base):
    resume_id: Mapped['int']
    name: Mapped['str']
    last_name: Mapped['str']
    email: Mapped['str']
    work_experience: Mapped['str']
    skills: Mapped['str']
    education: Mapped['str']
    user_id: Mapped['int'] = mapped_column(ForeignKey('users.user_id'))
    user = relationship("User", back_populates="resumes")
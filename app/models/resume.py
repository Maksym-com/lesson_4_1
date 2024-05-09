from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Resume(Base):
    resume_id: Mapped['int'] = mapped_column(primary_key=True)
    name: Mapped['str']
    last_name: Mapped['str']
    email: Mapped['str']
    work_experience: Mapped['str']
    skills: Mapped['str']
    education: Mapped['str']
    user_id: Mapped['int'] = mapped_column(ForeignKey('users.id'))
    user = relationship("User", back_populates="resumes")

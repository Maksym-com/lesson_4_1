from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from . import Base


class Message(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    sender_email: Mapped['str'] = mapped_column()
    receiver_email: Mapped['str'] = mapped_column()
    text: Mapped['str'] = mapped_column()
    title: Mapped['str'] = mapped_column()
    date = mapped_column(DateTime)


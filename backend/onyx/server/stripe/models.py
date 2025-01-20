from sqlalchemy.orm import DeclarativeBase
import sqlalchemy

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    sessionmaker,
    mapped_column,
    validates,
)
from sqlalchemy import String


class Base(DeclarativeBase):
    __abstract__ = True


class StripePaymentModel(Base):
    __tablename__ = "stripes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)

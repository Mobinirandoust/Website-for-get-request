from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Landsat7(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()
    link_dl:Mapped[str] = mapped_column(default="null")

class Landsat8(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()
    link_dl:Mapped[str] = mapped_column(default="null")

class Landsat9(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int] = mapped_column(unique=True)
    band1:Mapped[str] = mapped_column()
    band2:Mapped[str] = mapped_column()
    band3:Mapped[str] = mapped_column()
    band4:Mapped[str] = mapped_column()
    band5:Mapped[str] = mapped_column()
    band6:Mapped[str] = mapped_column()
    band7:Mapped[str] = mapped_column()
    city:Mapped[str] = mapped_column()
    date:Mapped[str] = mapped_column()
    takmili:Mapped[str] = mapped_column()
    link_dl:Mapped[str] = mapped_column(default="null")

# class AdminUser(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     Manger: Mapped[int] = mapped_column(default="mobin_iran_doust")
#     Password: Mapped[int] = mapped_column(default="mobin_iran_doust")
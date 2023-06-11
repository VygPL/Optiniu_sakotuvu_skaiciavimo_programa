from typing import Any
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_engine('sqlite:///linijos_parametrai.db', echo=True)

class Base(DeclarativeBase):
    pass

class Linijos_Duombaze(Base):
    __tablename__ = 'Linijos_Parametrai'
    id: Mapped[int] = mapped_column(primary_key=True)
    atstumas: Mapped[float] = mapped_column(nullable=False)
    slopinimas_km: Mapped[float] = mapped_column()
    signalo_slop : Mapped[float] = mapped_column()
    galios_nuostoliai : Mapped[float] = mapped_column()
    slopinimas_sudejus_galios_nuostolius : Mapped[float] = mapped_column()
    parametras_R : Mapped[float] = mapped_column()
    parametras_Q : Mapped[float] = mapped_column()

    def __init__(self, atstumas, slopinimas_km, signalo_slop, galios_nuostoliai,slopinimas_sudejus_galios_nuostolius, parametras_R, parametras_Q):
        self.atstumas = atstumas
        self.slopinimas_km = slopinimas_km
        self.signalo_slop = signalo_slop
        self.galios_nuostoliai = galios_nuostoliai
        self.slopinimas_sudejus_galios_nuostolius = slopinimas_sudejus_galios_nuostolius
        self.parametras_R = parametras_R
        self.parametras_Q = parametras_Q

    def __repr__(self) -> str:
        return f"{self.id}, {self.atstumas}, {self.slopinimas_km}, {self.signalo_slop},{self.galios_nuostoliai}, {self.slopinimas_sudejus_galios_nuostolius}, {self.parametras_R}, {self.parametras_Q}"
    

Base.metadata.create_all(engine)
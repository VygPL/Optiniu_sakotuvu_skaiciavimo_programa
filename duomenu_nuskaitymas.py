from sqlalchemy.orm import sessionmaker
from Linijos_Duombaze import *

Session = sessionmaker(bind = engine)
sesija = Session()

while True:
    pasirinkimas = int(input("Pasirinkite veiksma: 1 nuskaityti, 2 irasyti, 3 istrinti eilute, 4 iseina is programos: "))

    if pasirinkimas == 1:
        lin_duom = sesija.query(Linijos_Duombaze).all()
        print("---------------------")
        for duomenys in lin_duom:
            print(duomenys)
        print("---------------------")

    if pasirinkimas == 2:
        atstumas = float(input("Iveskite atstuma: "))
        slopinimas_km = float(input("Iveskite slopinima i km: "))
        signalo_slop = float(input("Iveskite signalo slopinima: "))
        galios_nuostoliai = float(input("Iveskite galios nuostolius: "))
        slopinimas_sudejus_galios_nuostolius = float(input("Iveskite slopinimo ir galios nuostoliu suma: "))
        parametras_R = float(input("Iveskite parametra R: "))
        parametras_Q = float(input("Iveskite parametra Q: "))
        linijos_duom = Linijos_Duombaze(atstumas, slopinimas_km, signalo_slop,galios_nuostoliai,slopinimas_sudejus_galios_nuostolius,parametras_R,parametras_Q)
        sesija.add(linijos_duom)
        sesija.commit()

    if pasirinkimas == 3:
        eislute_istrinti = int(input("Kuria eilute norite istrinti: "))
        eilutes_duom = sesija.query(Linijos_Duombaze).filter_by(id=eislute_istrinti).one()
        sesija.delete(eilutes_duom)
        sesija.commit()

    if pasirinkimas == 4:
        break
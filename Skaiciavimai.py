import math
from sqlalchemy.orm import sessionmaker
from Linijos_Duombaze import *

Session = sessionmaker(bind = engine)
sesija = Session()

class Signalu_Formules:
        
    def sudetis(self, skaicius1, skaicius2):
        return skaicius1 + skaicius2
     
    def atimtis_is_1(self, kintamasis_is_1):
        return 1 - kintamasis_is_1

    def signalo_slopinimas(self, atstumas, slop_koef):
        slop_s = slop_koef * atstumas
        return slop_s
    
    def signalo_slopinimas_c10(self, sig_s_10, sig_s_11):
        """
        Signalo slopinimas C10
        """
        s_skirtumas = (sig_s_11 - sig_s_10) / 10
        laipnis1 = pow(10, s_skirtumas)
        laipnis2 = 1 + laipnis1
        vieneto_dalyba = 1 / laipnis2
        logaritmas = math.log(vieneto_dalyba, 10)
        return logaritmas * (-10)
    
    def signalo_slopinimas_c11(self, sig_s_10, sig_s_11):
        """
        Signalo slopinimas C11
        """
        s_skirtumas = (sig_s_10 - sig_s_11) / 10
        laipnis1 = pow(10, s_skirtumas)
        laipnis2 = 1 + laipnis1
        vieneto_dalyba = 1 / laipnis2
        logaritmas = math.log(vieneto_dalyba, 10)
        return logaritmas * (-10)
    
    def bendr_slop_galiu_suma(self, parametras_SnEn):
        suma = 0.0
        sumos_sar = []
        for duom_f in parametras_SnEn:
            suma = suma + duom_f
            sumos_sar.append(suma)
        return sumos_sar
    
    def s_dalinta_10_minus(self, Sn_plius_Cn, suma_Sn_plius_E, Cn0dB):
        """
        Skaiciuoja parametra 10 laipsniu(-S/10)
        """
        atimtis1 = (Sn_plius_Cn - suma_Sn_plius_E - Cn0dB)/10
        laipsnis = math.pow(10, atimtis1)
        return laipsnis 

    def s_dalinta_10_plius(self, Sn_plius_Cn, suma_Sn_plius_E, Cn0dB):
        """
        Skaiciuoja parametra 10 laipsniu(S/10)
        """
        sudetis1 = (suma_Sn_plius_E + Cn0dB - Sn_plius_Cn)/10
        sudetis2_apvalinta = round(sudetis1, 5)
        laipsnis = math.pow(10, sudetis2_apvalinta)
        return laipsnis
    
    def signalo_slop_Cn0(self, s_dal_10_laips_10):
        """
        Daliklių slopinimas atsakos kryptyje Cn0
        """
        formuleCn0 = 1 / (s_dal_10_laips_10 + 1)
        return formuleCn0

    def signalo_slop_Cn0_dB(self, signalo_slop_Cn0):
        formule_dB = -10 * math.log(signalo_slop_Cn0, 10)
        return formule_dB
    
    def signalo_slop_Cn1(self, sig_slop_sn1):
        """
        Daliklių slopinimas atsakos kryptyje Cn1
        """
        formule_cn1 = 1 / (sig_slop_sn1+ 1)
        return formule_cn1
    
    def signalo_slop_Cn1_dB(self, sig_slop_cn1_dB):
        formule_cn1_dB = -10 * math.log(sig_slop_cn1_dB, 10)
        return formule_cn1_dB

    def parametras_R(self, kint_cn0_dB):
        formule_R = math.pow(10, (-kint_cn0_dB / 10))
        return formule_R

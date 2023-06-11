import tkinter as tk
from Skaiciavimai import *
from Linijos_Duombaze import *

class Pirminis_langas:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.pav_skaic = tk.Button(self.frame, text = 'Pavyzdiniai skaičiavimai', width = 25, command = self.new_window,)
        self.skaic_ivedimas = tk.Button(self.frame, text = 'Skaiciavimo įvedimas', width = 25, command= self.skaiciavimo_lango_linkas)
        self.iseiti_pagr_meniu = tk.Button(self.frame, text = 'Išeiti iš programos', width = 25, command = self.close_windows,)

        
        self.pav_skaic.pack()
        self.skaic_ivedimas.pack()
        self.iseiti_pagr_meniu.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
        self.new_window

    def new_window(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Pavyzdinis_langas(self.master)
        self.master.geometry('700x450')
        self.master.title("Optinių šakotuvų parametrų skaičiavimas")
        self.master.mainloop()

    def skaiciavimo_lango_linkas(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Skaiciavimo_langas(self.master) 
        self.master.geometry('900x500')
        self.master.title("Optinių šakotuvų parametrų skaičiavimas")
        self.master.mainloop()


class Pavyzdinis_langas:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame3 = tk.Frame(self.master)


        self.isejimo_mygtukas = tk.Button(self.frame, text = 'Išeiti', width = 15, command = self.close_windows)
        self.grizti_mygtukas = tk.Button(self.frame, text = 'Grįžti', width = 15, command = self.grizti_i_meniu)

        self.grizti_mygtukas.grid(row = 0, column=1)
        self.isejimo_mygtukas.grid(row=0, column=0)

        self.frame.grid(row=0, column=0)
        self.frame2.grid(row=1, column=0)
        self.frame3.grid(row=2, column=0)

        lin_duombaze = sesija.query(Linijos_Duombaze).all()

        pav_sarasas_atstumas = []
        pav_sarasas_slopinimas = []
        pav_sarasas_galia = []
        pav_sarasas_R = []
        pav_sarasas_Q = []

        for duom in lin_duombaze:
            pav_sarasas_atstumas.append(duom.atstumas)

        for duom in lin_duombaze:
            pav_sarasas_slopinimas.append(duom.slopinimas_km)

        for duom in lin_duombaze:
            pav_sarasas_galia.append(duom.galios_nuostoliai)

        for duom in lin_duombaze:
            pav_sarasas_R.append(duom.parametras_R)

        for duom in lin_duombaze:
            pav_sarasas_Q.append(duom.parametras_Q)

        self.atstumo_antraste_pav = tk.Label(self.frame2, text='Atstumas (L)')
        self.atstumo_antraste_pav.grid(column=0, row=0)

        self.slopinimo_antraste_pav = tk.Label(self.frame2, text='Slopinimas (Km)')
        self.slopinimo_antraste_pav.grid(column=1, row=0)

        self.galios_antraste_pav = tk.Label(self.frame2, text='Galios nuostoliai (E)')
        self.galios_antraste_pav.grid(column=2, row=0)

        self.r_antraste_pav = tk.Label(self.frame2, text='Parametras (R)')
        self.r_antraste_pav.grid(column=3, row=0)

        self.q_antraste_pav = tk.Label(self.frame2, text='Parametras (Q)')
        self.q_antraste_pav.grid(column=4, row=0)

        indeksas_R = 0 
        while indeksas_R < 12:
            self.atsakymai_atstumo = tk.Entry(self.frame3, width=20)
            self.atsakymai_atstumo.delete(0)
            self.atsakymai_atstumo.insert(0, pav_sarasas_atstumas[indeksas_R])
            self.atsakymai_atstumo.grid(row=indeksas_R, column=0, pady=5, padx=5)
            indeksas_R = indeksas_R + 1
        
        indeksas_R = 0 
        while indeksas_R < 12:
            self.atsakymai_slopinimo = tk.Entry(self.frame3, width=20)
            self.atsakymai_slopinimo.delete(0)
            self.atsakymai_slopinimo.insert(0, pav_sarasas_slopinimas[indeksas_R])
            self.atsakymai_slopinimo.grid(row=indeksas_R, column=1, pady=5, padx=5)
            indeksas_R = indeksas_R + 1

        indeksas_R = 0 
        while indeksas_R < 12:
            self.atsakymai_galios = tk.Entry(self.frame3, width=20)
            self.atsakymai_galios.delete(0)
            self.atsakymai_galios.insert(0, pav_sarasas_galia[indeksas_R])
            self.atsakymai_galios.grid(row=indeksas_R, column=2, pady=5, padx=5)
            indeksas_R = indeksas_R + 1

        indeksas_R = 0 
        while indeksas_R < 12:
            self.atsakymai_R_pav = tk.Entry(self.frame3, width=20)
            self.atsakymai_R_pav.delete(0)
            self.atsakymai_R_pav.insert(0, pav_sarasas_R[indeksas_R])
            self.atsakymai_R_pav.grid(row=indeksas_R, column=3, pady=5, padx=5)
            indeksas_R = indeksas_R + 1

        indeksas_R = 0 
        while indeksas_R < 12:
            self.atsakymai_Q_pav = tk.Entry(self.frame3, width=20)
            self.atsakymai_Q_pav.delete(0)
            self.atsakymai_Q_pav.insert(0, pav_sarasas_Q[indeksas_R])
            self.atsakymai_Q_pav.grid(row=indeksas_R, column=4, pady=5, padx=5)
            indeksas_R = indeksas_R + 1
        

    def close_windows(self):
        self.master.destroy()

    def grizti_i_meniu(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Pirminis_langas(self.master)
        self.master.geometry('700x450')
        self.master.title("Optinių šakotuvų parametrų skaičiavimas")
        self.master.mainloop()

class Skaiciavimo_langas:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame1 = tk.Frame(self.master)
      
        self.frame2 =tk.Frame(self.master)

        self.frame3 =tk.Frame(self.master)
        self.frame4 =tk.Frame(self.master)
        self.frame5 =tk.Frame(self.master)

        self.isejimo_mygtukas = tk.Button(self.frame, text = 'Išeiti', width = 15, command = self.close_windows)
        self.grizti_mygtukas = tk.Button(self.frame, text = 'Grįžti', width = 15, command = self.grizti_i_meniu)

        self.antraste_ivedimo = tk.Label(self.frame1, text="Įvesti norimą kiekį šakotuvų:")
        self.ivedimas = tk.Entry(self.frame1, width = 15)
        self.ivedimo_mygtukas = tk.Button(self.frame1, text = 'Įvesti', width = 15, command=self.ivedimo_lauku_generavimas)
        self.skaiciuoti_mygtukas = tk.Button(self.frame1, text="Skaičiuoti", width=15, command=self.sarasu_skaiciavimas)
        
        self.grizti_mygtukas.grid(row = 0, column=0)
        self.isejimo_mygtukas.grid(row=1, column=0)
        
        self.antraste_ivedimo.grid(row=0, column = 0)
        self.ivedimas.grid(row = 0, column = 1)
        self.ivedimo_mygtukas.grid(row = 0, column = 2)
        self.skaiciuoti_mygtukas.grid(row=0, column=3)

        self.frame.grid(row=0, column=0)
        self.frame1.grid(row=0, column=1, padx=20, pady= 20)

        #lenteles
        self.frame2.grid(row=1, column=1)
        self.frame3.grid(row=2, column=1)
        self.frame4.grid(row=2, column=2)
        self.frame5.grid(row=1, column=2)
        
    

    def ivedimo_lauku_generavimas(self):

        global sarasas_atstumo
        global sarasas_slopinimo 
        global sarasas_galios 

        sarasas_atstumo = []
        sarasas_slopinimo = []
        sarasas_galios = []


        ivedimo_kint = int(self.ivedimas.get())

        self.atstumo_antraste = tk.Label(self.frame2, text='Atstumas (L)')
        self.atstumo_antraste.grid(column=0, row=0)
        

        self.slopinimas_i_km = tk.Label(self.frame2, text='Slopinimas Km(a)')
        self.slopinimas_i_km.grid(column=1, row=0, padx=25)

        self.galios_antraste = tk.Label(self.frame2, text='Galia (E)')
        self.galios_antraste.grid(column=2, row=0, padx=15)

        for y in range(ivedimo_kint):

            self.ivestis_atstumo= tk.Entry(self.frame3, width=15)
            sarasas_atstumo.append(self.ivestis_atstumo)
            self.ivestis_atstumo.grid(row=y, column=0, pady=5, padx=5)

        for y in range(ivedimo_kint):
            self.ivestis_slopinimo = tk.Entry(self.frame3, width=15)
            sarasas_slopinimo.append(self.ivestis_slopinimo)
            self.ivestis_slopinimo.grid(row=y, column=1, pady=5, padx=5)
            

        for y in range(ivedimo_kint):
            self.ivestis_galia = tk.Entry(self.frame3, width=15)
            sarasas_galios.append(self.ivestis_galia)
            self.ivestis_galia.grid(row=y, column=2, pady=5, padx=5)

    def sarasu_skaiciavimas(self):

        ivedimo_kint = int(self.ivedimas.get())

        global sarasas_R
        global sarasas_Q
        global sarasas_Cn0_dB
        global sarasas_Cn1_dB

        sarasas_slopinimo_atsakymams = []
        sarasas_parametrui_Sn_plius_En = []
        sarasas_parametrui_Sn_plius_En_bendros_sumos = []
        sarasas_Sn_minus = []
        sarasas_Sn_plius = []
        sarasas_Cn0 = []
        sarasas_Cn0_dB = []
        sarasas_Cn0_suma = []
        sarasas_Cn1 = []
        sarasas_Cn1_dB = []
        sarasas_R = []
        sarasas_Q = []

        skaiciavimo_objektas = Signalu_Formules()

        for x, y in zip(sarasas_atstumo, sarasas_slopinimo):
            kintamasis1_atstumas = float(x.get())
            kintamasis2_slopinimas = float(y.get())
            sarasas_slopinimo_atsakymams.append(skaiciavimo_objektas.signalo_slopinimas(kintamasis1_atstumas,kintamasis2_slopinimas))

        for x, y in zip(sarasas_slopinimo_atsakymams, sarasas_galios):
            kintamasis_galia =  float(y.get())
            sarasas_parametrui_Sn_plius_En.append(skaiciavimo_objektas.sudetis(kintamasis_galia, x))

        suma1 = 0.0
        for x in sarasas_parametrui_Sn_plius_En:
            suma1 = skaiciavimo_objektas.sudetis(suma1, x)
            sarasas_parametrui_Sn_plius_En_bendros_sumos.append(suma1)
      
        sarasas_Sn_minus.append(skaiciavimo_objektas.s_dalinta_10_minus(0,0,0))
        
        indeksas = 1
        indeksas_ivedimam = 0
        kitamasis_Cn0_suma = 0.0

        while indeksas <= ivedimo_kint + 1:
            kintamasis_Cn0 = skaiciavimo_objektas.signalo_slop_Cn0(sarasas_Sn_minus[indeksas_ivedimam])
            sarasas_Cn0.append(kintamasis_Cn0)
            kitamasis_Cn0_dB = skaiciavimo_objektas.signalo_slop_Cn0_dB(kintamasis_Cn0)
            sarasas_Cn0_dB.append(kitamasis_Cn0_dB)
            kitamasis_Cn0_suma = skaiciavimo_objektas.sudetis(kitamasis_Cn0_suma, sarasas_Cn0_dB[indeksas_ivedimam])
            sarasas_Cn0_suma.append(kitamasis_Cn0_suma)
            kintamasis_sn_minus_laik = skaiciavimo_objektas.s_dalinta_10_minus(0, sarasas_parametrui_Sn_plius_En_bendros_sumos[indeksas_ivedimam], kitamasis_Cn0_suma)
            sarasas_Sn_minus.append(kintamasis_sn_minus_laik)
            
            indeksas = indeksas + 1
            indeksas_ivedimam = indeksas_ivedimam + 1
            if indeksas_ivedimam == ivedimo_kint:
                break

        sarasas_Sn_plius.append(skaiciavimo_objektas.s_dalinta_10_plius(0,0,0))

        indeksas = 1
        indeksas_ivedimam = 0

        while indeksas <= ivedimo_kint +1:
            kintamasis_cn1 = skaiciavimo_objektas.signalo_slop_Cn1(sarasas_Sn_plius[indeksas_ivedimam])
            sarasas_Cn1.append(kintamasis_cn1)
            kitamasis_Cn1_dB = skaiciavimo_objektas.signalo_slop_Cn1_dB(kintamasis_cn1)
            sarasas_Cn1_dB.append(kitamasis_Cn1_dB)
            kintamasis_sn_plius_laik = skaiciavimo_objektas.s_dalinta_10_plius(0, sarasas_parametrui_Sn_plius_En_bendros_sumos[indeksas_ivedimam], sarasas_Cn0_suma[indeksas_ivedimam])
            sarasas_Sn_plius.append(kintamasis_sn_plius_laik)

            indeksas = indeksas + 1
            indeksas_ivedimam = indeksas_ivedimam + 1
            if indeksas_ivedimam == ivedimo_kint:
                break

        for x in sarasas_Cn0_dB:
            kintamasis_R = skaiciavimo_objektas.parametras_R(x)
            sarasas_R.append(kintamasis_R)

        for x in sarasas_R:
            kintamasis_Q = skaiciavimo_objektas.atimtis_is_1(x)
            sarasas_Q.append(kintamasis_Q)

        atsakymu_iskvietimas = self.sarasu_atvaizdavimas()
    
    def sarasu_atvaizdavimas(self):

        ivedimo_kint = int(self.ivedimas.get())

        self.antraste_R = tk.Label(self.frame5, text='R:', padx= 40)
        self.antraste_R.grid(column=0, row=0)

        self.antraste_Q = tk.Label(self.frame5, text='Q:')
        self.antraste_Q.grid(column=1, row=0)


        indeksas_R = 0 
        while indeksas_R < ivedimo_kint:
            self.atsakymai_R= tk.Entry(self.frame4, width=20)
            self.atsakymai_R.delete(0)
            self.atsakymai_R.insert(0, sarasas_R[indeksas_R])
            self.atsakymai_R.grid(row=indeksas_R, column=3, pady=5, padx=5)
            indeksas_R = indeksas_R + 1

        indeksas = 0 
        while indeksas < ivedimo_kint:
            self.atsakymai_Q= tk.Entry(self.frame4, width=20)
            self.atsakymai_Q.delete(0)
            self.atsakymai_Q.insert(0, sarasas_Q[indeksas])
            self.atsakymai_Q.grid(row=indeksas, column=4, pady=5, padx=5)
            indeksas = indeksas + 1

    def close_windows(self):
        self.master.destroy()

    def grizti_i_meniu(self):
        self.master.destroy() 
        self.master = tk.Tk() 
        self.app = Pirminis_langas(self.master)
        self.master.geometry('700x450')
        self.master.title("Optinių šakotuvų parametrų skaičiavimas")
        self.master.mainloop()


def main(): 
    root = tk.Tk()
    root.geometry('700x450')
    app = Pirminis_langas(root)
    root.title("Optinių šakotuvų parametrų skaičiavimas")
    root.mainloop()



if __name__ == '__main__':
    main()

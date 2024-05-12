from abc import ABC, abstractmethod

class Szoba(ABC):

    def __init__(self, ar, szobaszam):
        self.szoba_ar = ar
        self.szoba_szam = szobaszam

    @abstractmethod
    def kiir(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, wifi):
        super().__init__(ar, szobaszam)
        self.wifi = wifi

    def kiir(self):
        print(f"A {self.szoba_szam} számú egyágyas szoba: {self.szoba_ar} Ft./éjszaka, WI-FI: {self.wifi} /nap.")

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kandallo):
        super().__init__(ar, szobaszam)
        self.kandallo = kandallo

    def kiir(self):
        print(f"A {self.szoba_szam} számú kétágyas szoba: {self.szoba_ar} Ft./éjszaka, Kandallo: {self.kandallo}.")
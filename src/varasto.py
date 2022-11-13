"""luokka varasto"""
class Varasto:
    """luokka varasto, millä tilavuus ja saldo"""
    def __init__(self, tilavuus, alku_saldo = 0):
        """Inittaa luokka"""
        self.tilavuus = max(0.0,tilavuus)
        self.saldo = min(max(0.0,alku_saldo),tilavuus)

    def paljonko_mahtuu(self):
        """Tarkista paljonko mahtuu"""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """lisaa saldoa varastoon"""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ota varastosta saldoa"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Palauta paljonko saldoa ja tilaa"""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
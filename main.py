class HotBeverage():
    def wasserKochen(self):
        print("wasser wird gekocht")
    def vorbereiten(self):
        pass
    def eingiessen(self):
        print(self.__class__.__name__, "eingiessen")
    def toppingHinzufuegen(self):
        pass
    def routine(self):
        self.wasserKochen()
        self.vorbereiten()
        self.eingiessen()
        self.toppingHinzufuegen()
class Kaffee(HotBeverage):
    def vorbereiten(self):
        print("Kaffee aufbruehen")
    def toppingHinzufuegen(self):
        print("Zucker und Milch hinzufuegen")
class Tee(HotBeverage):
    def vorbereiten(self):
        print("Tee ziehen lassen")
    def toppingHinzufuegen(self):
        print("Zitrone hinzufuegen")
kaffee = Kaffee()
kaffee.routine()
tee = Tee()
tee.routine()
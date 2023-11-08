import random
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("layout.ui", self)
        self.ui.rezerwoj.clicked.connect(self.rezerwacja)
        self.show()

    def rezerwacja(self):
        imie = self.ui.odpImie.text()
        nazwisko = self.ui.odpNazwisko.text()
        specjalizacja=""
        cena = 0
        zailedniwizyta=0
        if self.ui.internista.isChecked():
            specjalizacja = "internista"
        elif self.ui.pediatra.isChecked():
            specjalizacja = "pediatra"
        elif self.ui.dermatolog.isChecked():
            specjalizacja = "dermatolog"
        if self.ui.czyprywatna.isChecked():
            cena = 200
            zailedniwizyta = int(random.uniform(0, 14))
        else:
            zailedniwizyta = int(random.uniform(0, 1000))
        self.ui.wynikrezerwacji.setText("Pomyślnie zarezerwowano wizytę u lekarza: " + specjalizacja + ".\n Termin wizyty przypada za: " + str(zailedniwizyta) + " dni.\n Koszt wizyty: " + str(cena) + ". ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())



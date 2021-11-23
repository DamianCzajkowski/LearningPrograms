import numpy as np
from PIL import Image


class WyrownanieHistogramu:

    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku
        self.plik = None
        self.tablica_obrazu = None
        self.skumulowany_histogram = None
        self.mapa_transformacji = None
        self.wyrownany_obraz = None

    def _wczytaj_plik(self):
        try:
            self.plik = Image.open(self.nazwa_pliku)
        except FileNotFoundError:
            print("Nie ma takiego pliku")

    def _konwertuj_plik(self):
        szary_obraz = self.plik.convert(mode='L')

        self.tablica_obrazu = np.asarray(szary_obraz)

    def _wyrownaj_plik(self):

        histogram = np.bincount(self.tablica_obrazu.flatten(), minlength=256)

        ilosc_pikseli = np.sum(histogram)
        histogram = histogram/ilosc_pikseli

        self.skumulowany_histogram = np.cumsum(histogram)

    def _mapowanie_pikseli(self):

        self.mapa_transformacji = np.floor(
            255 * self.skumulowany_histogram).astype(np.uint8)

    def _transformacja_histogramu(self):

        obraz_jako_lista = list(self.tablica_obrazu.flatten())

        wyrownany_obraz_jako_lista = [
            self.mapa_transformacji[p] for p in obraz_jako_lista]

        self.wyrownany_obraz = np.reshape(np.asarray(
            wyrownany_obraz_jako_lista), self.tablica_obrazu.shape)

    def _zapisz_wyrownany_obraz(self):
        wyrownany_plik = Image.fromarray(self.wyrownany_obraz, mode='L')
        wyrownany_plik.save(f"wyrownany_{self.nazwa_pliku}")

    def wyrownaj(self):
        self._wczytaj_plik()
        self._konwertuj_plik()
        self._wyrownaj_plik()
        self._mapowanie_pikseli()
        self._transformacja_histogramu()
        self._zapisz_wyrownany_obraz()


if __name__ == "__main__":
    nazwa_pliku = input('Podaj nazwę pliku do wyrównania: ')
    histogram = WyrownanieHistogramu(nazwa_pliku)
    histogram.wyrownaj()

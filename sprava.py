from pojisteny import Pojisteny


class Sprava:
    def __init__(self):
        self.pojisteni = []

    def pridat_pojisteneho(self, jmeno, prijmeni, telefon, vek):
        """
        Přidá nového pojištěného
        :param jmeno: Jméno pojištěného
        :param prijmeni: Příjmení pojištěného
        :param telefon: Telefonní číslo pojištěného
        :param vek: Věk pojištěného
        """
        novy_pojisteny = Pojisteny(jmeno, prijmeni, telefon, vek)
        self.pojisteni.append(novy_pojisteny)

    def vypsat_pojistene(self):
        """
        Vypíše všechny pojištěné v seznamu
        """
        if self.pojisteni:
            for pojisteni in self.pojisteni:
                print(pojisteni)
        else:
            print("Zatím nejsou evidováni žádní pojištěnci.")

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        """
        Vyhledá pojištěné podle jména a příjmení ze seznamu
        :param jmeno: Jméno hledaného pojištěného
        :param prijmeni: Příjmení hledaného pojištěného
        """
        vyhledat = [pojisteny for pojisteny in self.pojisteni if
                    pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni]
        if vyhledat:
            for pojisteni in vyhledat:
                print(pojisteni)
        else:
            print("Hledaný pojištěný nebyl nalezen.")

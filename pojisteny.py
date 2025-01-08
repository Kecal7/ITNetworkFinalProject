class Pojisteny:
    def __init__(self, jmeno, prijmeni, telefon, vek):
        """
        Zavedení nového pojištěného
        :param jmeno: Jméno pojištěného
        :param prijmeni: Příjmení pojištěného
        :param telefon: Telefonní číslo pojištěného
        :param vek: Věk pojištěného
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, telefon: {self.telefon}, věk: {self.vek}"

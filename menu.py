from sprava import Sprava
sprava = Sprava()


def spravne_jmeno_prijmeni(jmeno_vstup):
    """
    Kontroluje, zda uživatel zadal pouze abecední znaky
    :param jmeno_vstup: Vstup pro jméno a příjmení
    :return: True, pokud obsahuje pouze abecední znaky, jinak False
    """
    return jmeno_vstup.isalpha()


def spravne_cislo(cislo_vstup):
    """
    Kontroluje, zda uživatel zadal pouze čísla
    :param cislo_vstup: Vstup pro telefonní číslo a věk
    :return: True, pokud obsahuje pouze číslice, jinak False
    """
    return cislo_vstup.isdigit()


class Menu:  # uživatelské menu
    vyber = None
    while vyber != "4":  # úvod uživatelského menu
        print("\n-------------------------")
        print("Evidence pojištěných")
        print("-------------------------\n")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        vyber = input("Vyberte akci: ")  # jednotlivé akce uživatelského menu

        if vyber == "1":  # přidání pojištěného
            jmeno = ""
            while not spravne_jmeno_prijmeni(jmeno):
                jmeno = input("Zadejte jméno pojištěného: ")
                if not spravne_jmeno_prijmeni(jmeno):
                    print("Jméno může obsahovat pouze abecední znaky. Zkuste to prosím opět.")

            prijmeni = ""
            while not spravne_jmeno_prijmeni(prijmeni):
                prijmeni = input("Zadejte příjmení pojištěného: ")
                if not spravne_jmeno_prijmeni(prijmeni):
                    print("Příjmení může obsahovat pouze abecední znaky. Zkuste to prosím opět.")

            telefon = ""
            while not spravne_cislo(telefon):
                telefon = input("Zadejte telefonní číslo pojištěného: ")
                if not spravne_cislo(telefon):
                    print("Telefonní číslo musí obsahovat pouze číslice. "
                          "V případě, že zadáváte i předvolbu, použijte verzi s dvěma nuly namísto znaménka. "
                          "Zkuste to prosím znovu.")

            vek = ""
            while not spravne_cislo(vek):
                vek = input("Zadejte věk pojištěného: ")
                if not spravne_cislo(vek):
                    print("Věk pojištěného musí obsahovat pouze číslice. Zkuste to prosím znovu.")

            sprava.pridat_pojisteneho(jmeno, prijmeni, telefon, vek)  # přidání nového pojištěného do seznamu

        elif vyber == "2":  # výpis všech pojištěných
            sprava.vypsat_pojistene()

        elif vyber == "3":  # vyhledání pojištěného
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení pojištěného: ")
            sprava.vyhledat_pojisteneho(jmeno, prijmeni)

        elif vyber == "4":  # konec programu
            print("Děkujeme za použití aplikace, nashledanou!")
        else:  # ošetření chyby
            print("Nesprávný výběr akce, prosíme opakujte.")

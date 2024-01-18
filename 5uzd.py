def ievadi_vardu():
    return input("Ievadiet savu vārdu: ")

def ieraksti_faila(vards, fails):
    try:
        with open(fails, 'w') as f:
            f.write(vards)
        print("Veiksmīgi ierakstīts failā.")
    except IOError as e:
        print(f"Kļūda: Nevarēja ierakstīt failā. {e}")
    except Exception as e:
        print(f"Kļūda: Nezināma kļūda. {e}")

def main():
    vards = ievadi_vardu()
    fails = "5uzd.txt"
    ieraksti_faila(vards, fails)

if __name__ == "__main__":
    main()

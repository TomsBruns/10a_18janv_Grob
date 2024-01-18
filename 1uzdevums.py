def lasit_un_drukaj_failu( fails_nosaukums ):
    try:
        with open(fails_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs: Šodiena")
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print("Kļūda:", e)

fails_nosaukums = '1uzd.txt'
lasit_un_drukaj_failu(fails_nosaukums)

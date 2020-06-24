define k = Character ("Kloth")

label leiche:
    $ leiche = True
    scene leiche

    show kloth aengstlich1

    k "Ich muss mit dir sprechen."

    menu:
        "Gespräch zustimmen":
            jump zustimmen
        "Gespräch ablehnen":
            jump ablehnen
        "Gespräch auf später verschieben":
            jump verschieben

label zustimmen:
    #sequenz

    k "Monolog_zustimmen"

    jump treppenhaus2

label ablehnen:

    #sequenz

    k "Monolog_ablehnen"

    jump treppenhaus2

label verschieben:

    #sequenz

    k "Hörst du mir jetzt doch bitte zu?"

    #menu:
        #"Ja":

        #"Nein"
    jump treppenhaus2

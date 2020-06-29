define k = Character ("Kloth")

label letzterTag:
    $ leiche = True
    scene treppenhaus2

    show kloth aengstlich1

    k "Atropos!"
    a "Kloth, was ist los?"
    k "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"
    a "Beruhige dich erst einmal und atme tief durch. Was ist passiert?"
    k "Nicht hier … es könnte jemand kommen und dann…"
    a "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

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

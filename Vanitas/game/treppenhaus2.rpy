
default plakat = False
default leiche = False

screen verlassen():
    frame:
        xalign 0.75 ypos 150
        hbox:
            textbutton "PFEIL":
                action Jump ("credits")

label treppenhaus2:

    hide screen pfeiltreppe

    scene treppenhaus2

    "Möchtest du dich genauer umschauen?"

    if plakat:
        if leiche:

            call screen verlassen

        else:

            menu:
                "Leiche":
                    jump leiche

    else:
        if leiche:

            show screen verlassen

            menu:
                "Plakate":
                    jump plakate2
        else:
            menu:
                "Leiche":
                    jump leiche
                "Plakate":
                    jump plakate2


label plakate2:

    scene plakate2

    $ plakat = True

    b "Monolog"

    jump treppenhaus2

label credits:

    scene credits

    "Danke fürs Spielen"

    return

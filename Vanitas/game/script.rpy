define b = Character("Bob")

screen pfeilweiter():
    frame:
        xalign 1.0 ypos 500
        hbox:
            textbutton "--->":
                action Jump ("weiter")

screen pfeiltreppe():
    frame:
        xalign 0.75 ypos 150
        hbox:
            textbutton "PFEIL":
                action Jump ("treppenhaus2")
label start:

    scene anfangliste

    "Hier sind alle wichtige Hinweise zu sehen, um den Prototypen verstehen zu können."

    call screen pfeilweiter

label weiter:

    scene treppenhaus1

    "Was möchtest du machen?"

    show screen pfeiltreppe

    menu:
        "Konversation mit Kollegen":
            jump konversation

        "Plakatte anschauen":
            jump plakate

label konversation:

    hide screen pfeiltreppe

    $ konversation = True

    scene kollegen
    with zoomin

    b "Gespräch mit Kollegen"
    "Kollege" "bla bla bla"

    jump treppenhaus1


label plakate:

    hide screen pfeiltreppe

    $ konversation = False

    scene plakate

    b "Monolog"

    jump treppenhaus1

label treppenhaus1:

    scene treppenhaus1

    show screen pfeiltreppe

    if konversation:

        menu:
            "Plakate anschauen":
                jump treppenhausOhneMenu

    else:

        menu:
            "Konversation mit Kollegen":
                jump treppenhausOhneMenu

label treppenhausOhneMenu:

    "Hier gibt es nichts mehr zum anschauen"

    call screen pfeiltreppe

    # This ends the game.

    #return

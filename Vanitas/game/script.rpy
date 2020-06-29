define a = Character("Atropos")
default glitchfertig = False
image pfeil_rechts = Transform ("pfeil",rotate = 180)
image pfeil_rechts_blau = Transform ("pfeilblau",rotate = 180)
image pfeil_unten = Transform ("pfeil",rotate = 180)
image pfeil_unten_blau = Transform ("pfeilblau",rotate = 180)

image glitch:
        "glitch1"
        pause .09
        "glitch2"
        pause .09
        repeat 3

screen pfeiltreppe():
    frame:
        xpos 1500 ypos 800
        imagebutton:
            idle "pfeil_rechts"
            hover "pfeil_rechts_blau"
            action Jump ("treppenhaus2")

screen pfeil_rechts():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "pfeil_rechts"
            hover "pfeil_rechts_blau"
            #background
            action Jump ("weiter")

screen pfeil_unten():
    frame:
        xpos 1600 ypos 890
        imagebutton:
            idle "pfeil_rechts"
            hover "pfeil_rechts_blau"
            action Jump ("treppenhaus1")


label start:

    scene tagebuch

    a "{i}Mein Tagebuch mit allem, was ich heute bereits erlebt habe.{/i}"

    call screen pfeil_rechts

label weiter:

    scene treppenhaus1gruppe

    a "{i} Den Anschiss vom Boss hätte ich mir sparen können… ich hätte die Happiness-Pille heute Morgen einfach doch nehmen sollen. {/i}"
    a "{i} Ob es wohl Auswirkungen hat, wenn ich sie einen einzigen Tag nicht nehme? Anders kann ich mir Anans Reaktion echt nicht erklären. {/i}"
    a "{i} Hmm… ich glaube die Plakate sind neu. Wie Aither die Pillen wohl dieses Mal bewirbt? Sie lassen sich echt immer was Neues einfallen. {/i}"

    show screen pfeiltreppe

    menu:
        "Ich könnte mir die Plakate mal etwas näher ansehen.":
            jump plakate

        "Ich könnte mal wieder mit meinen Kollegen reden. Vielleicht haben sie interessante Neuigkeiten.":
            jump konversation

        "Ich sollte besser wieder zurück ins Labor. Anan meinte, ich soll die Tablette sofort nachträglich einnehmen.":
            jump treppenhausOhneMenu


label konversation:

    hide screen pfeiltreppe

    $ konversation = True

    scene kollegen
    with zoomin

    a "Gespräch mit Kollegen"

    "Kollege" "bla bla bla"

    jump treppenhaus1


label plakate:

    hide screen pfeiltreppe

    $ konversation = False

    scene plakate1

    a "Sie stellen sie genauso wie immer dar. Ein perfektes glückliches Leben für jeden."
    a "Wie lösen die Pillen nur diese Glücklichkeit in einem aus? Ich entwickle sie selbst mit, aber ich habe trotzdem keine Ahnung wie sie eigentlich wirken."
    a "Ich sollte mich nicht zu lange mit den Plakaten beschäftigen. Ich habe keine Lust Anan noch einmal über den Weg zu laufen und einen weiteren Anschiss zu riskieren."

    call screen pfeil_unten

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

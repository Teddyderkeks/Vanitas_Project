
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

    scene treppenhaus2leiche

    a "Kloth? Nein, das darf nicht wahr sein… was? Warum? Ich…"
    a "{i}Vergiss die Pille nicht, Atropos. Du fängst schon an dir Sachen einzubilden. Hier ist nichts zu sehen.{/i}"
    a "{i}Langsam wirst du wirklich wahnsinnig. Nimm die Pille und werde wieder glücklich, so wie all deine Kollegen es sind.{/i}"
    a "{i}Du hast dein Glück verdient. So wie alle Menschen Glück verdient haben. Da hängen Plakate für die Impfung, damit auch diese Menschen bald glücklich werden können.{/i}"

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
                "Ja natürlich. Ich muss sofort die Pille nehmen. Ich fange schon an mir Sachen einzubilden.":
                    jump monolog
                "Irgendwie möchte ich mich doch vergewissern, dass diese Leiche nur eine Einbildung ist. Ich sollte sie mir näher ansehen.":
                    jump leiche
                "Ich brauche einen Moment Bedenkzeit. Vielleicht könnte ich mir in der Zwischenzeit die Plakate etwas genauer anschauen.":
                    jump plakate2


label plakate2:

    scene plakate2

    $ plakat = True

    a "{i}Die nächste Impfung steht also bald an. Damals vor meiner war ich ziemlich aufgeregt gewesen.{/i}"
    a "{i}Danach durfte ich endlich Happiness nehmen. Ich war zum ersten Mal wirklich glücklich.{/i}"
    a "{i}Ob ich wohl tatsächlich unglücklicher werde, weil ich die Pille die letzten Tage nicht genommen habe?{/i}"
    a "{i}Zu welchem Preis bin ich eigentlich glücklich?… Kann mir die Glücklichkeit wirklich einfach so geschenkt werden, ohne dass ich einen Preis dafür bezahlen muss?{/i}"
    a "{i}Ja, kann sie. Du hast es immerhin verdient glücklich zu sein. {/i}"
    a "{i}Du machst andere Menschen glücklich, also wieso solltest du einen Preis für deine eigene Glücklichkeit zahlen müssen?{/i}"
    a "{i}Und was spielt es überhaupt für eine Rolle? Die Hauptsache ist doch, dass du glücklich bist und nicht warum du es bist.{/i}"
    a "{i}Du solltest jetzt ins Labor zurückkehren und Happiness nehmen. Werde wieder glücklich.{/i}"
    a "{i}Ja, ich sollte besser ins Labor zurückkehren.{/i}"

    jump treppenhaus2

label monolog:

    scene treppenhaus2leiche

    a "{i}Verdammt noch mal, was denke ich denn da bloß? Die Pille ist doch gerade nicht wichtiger. Was, wenn das da am Boden wirklich mein Freund ist?{/i}"
    a "{i}Kloth könnte schwer verletzt oder sogar tot sein. Ich muss nach ihm sehen. Ich hoffe wirklich, dass es nur eine Einbildung ist.{/i}"

    jump leiche

label leiche:

label credits:

    scene credits

    "Danke fürs Spielen"

    return

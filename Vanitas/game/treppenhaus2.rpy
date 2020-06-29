
default plakat = False
default leiche = False
default ende = False

screen pfeil_verlassen():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "pfeil_rechts"
            hover "pfeil_rechts_blau"
            action Jump ("credits")

screen pfeil_back():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "pfeil_rechts"
            hover "pfeil_rechts_blau"
            action Jump ("treppenhaus2")

label treppenhaus2:

    hide screen pfeiltreppe

    scene treppenhaus2leiche

    if plakat:
        if leiche:
            if ende:
                call screen pfeil_verlassen

        else:

            menu:
                "Ich sollte ins Labor zurück und meine Pille nehmen. Wenn Anan mich immer noch hier herumstehen sieht, bekomme ich ein Problem.":
                    jump dochleiche
                "Ich muss mir zuvor die Leiche ansehen. Irgendetwas stimmt nicht. Ich habe Kloth den ganzen Tag noch nicht gesehen.":
                    jump leiche

    else:
        if leiche:
            if zustimmen:

                a "Nein."
                a "Nein!"
                a "Kloth… verdammt… wie konnte das nur passieren? Und was habe ich nur getan? Was hatte ich tun wollen?"
                a "Nein… nein… das war nicht ich… das war… dieser… dieser miese…. Ich dachte wir wären Freunde?! Wie konnte Chesis ihm das nur antun?"
                a "Wie konnte er einem seiner besten Freunde so etwas antun? Wie hatte er Kloth in den Abgrund stürzen können?"
                a "Hätte ich es verhindern können? Nein- das spielt keine Rolle. Ich hätte es verhindern müssen."
                a "Das hätte alles niemals passieren dürfen. Ich werde… ich werde dafür sorgen, dass jemand dafür büßt."
                a "Ich werde dich rächen, Kloth, das verspreche ich dir! Dein Mord wird nicht ungesühnt bleiben!"
                $ ende= True
                call screen pfeil_verlassen
            else:
                a "Nein."
                a "Nein!"
                a "Kloth… verdammt… wie konnte das nur passieren? "
                a "Dieser… dieser miese…. Ich dachte wir seien Freunde. Wie konnte Chesis ihm das nur antun?"
                a "Wie konnte er einem seiner besten Freunde so etwas antun? Wie hatte er Kloth in den Abgrund stürzen können?"
                a "Und ich… warum verdammt noch mal war ich nicht da als er mich gebraucht hat? Dann wäre das alles nicht passiert."
                a "Ich werde… ich werde dafür sorgen, dass jemand dafür büßt."
                a "Ich werde dich rächen, Kloth, das verspreche ich dir! Dein Mord wird nicht ungesühnt bleiben! "
                a "Chesis wird dafür büßen. Dafür sorge ich. Wie konnte er es wagen heute Morgen so zu tun als wäre das alles nicht passiert?"
                a "Wie konnte er es wagen mich anzulächeln und glücklich zu sein? Er hat es nicht verdient glücklich zu sein. Keiner hat das."
                a "Ich werde dich rächen, Kloth und wenn es das letzte ist, was ich tue."
                $ ende= True
                call screen pfeil_verlassen

        else:

            a "Kloth? Nein, das darf nicht wahr sein… was? Warum? Ich…"
            a "{i}Vergiss die Pille nicht, Atropos. Du fängst schon an dir Sachen einzubilden. Hier ist nichts zu sehen.{/i}"
            a "{i}Langsam wirst du wirklich wahnsinnig. Nimm die Pille und werde wieder glücklich, so wie all deine Kollegen es sind.{/i}"
            a "{i}Du hast dein Glück verdient. So wie alle Menschen Glück verdient haben. Da hängen Plakate für die Impfung, damit auch diese Menschen bald glücklich werden können.{/i}"

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

    call screen pfeil_back

    jump treppenhaus2

label monolog:

    scene treppenhaus2leiche

    a "{i}Verdammt noch mal, was denke ich denn da bloß? Die Pille ist doch gerade nicht wichtiger. Was, wenn das da am Boden wirklich mein Freund ist?{/i}"
    a "{i}Kloth könnte schwer verletzt oder sogar tot sein. Ich muss nach ihm sehen. Ich hoffe wirklich, dass es nur eine Einbildung ist.{/i}"

    jump leiche


label dochleiche:

    scene treppenhaus2leiche

    a "{i}Du solltest gehen, deine Glücklichkeit wartet auf dich. Auf was wartest du also noch?{/i}"
    a "{i}Nein… ich weiß nicht… irgendetwas stimmt nicht. Kloth, wenn er das wirklich ist und ich es mir nicht einbilde…{/i}"
    a "{i}Nein, das könnte ich mir nicht verzeihen. Ich muss mir die Leiche anschauen und herausfinden, ob sie wirklich existiert.{/i}"

    jump leiche

label leiche:

    scene leiche

    a "Kloth?"
    a "Nein, verdammt. Das darf doch nicht wahr sein. Das ist keine Illusion, oder? Es ist so real… das ganze Blut… und… "
    a "So etwas kann ich mir nicht einbilden, oder? Aber wie? Warum? Kloth!"
    a "Kloth. Bitte rede mit mir. Du kannst doch nicht tot sein."
    a "Kloth… bitte… "
    a "{i}Pille, du musst deine Pille nehmen. Du halluzinierst, merkst du es denn nicht? Das hier kann nicht wahr sein.{/i}"
    a "{i}Wie könnte so etwas schreckliches wahr sein? Du bist doch eigentlich glücklich.{/i}"
    a "Nein… es ist wahr… es ist wahr… ich will nicht, dass es wahr ist, aber es ist wahr…"
    a "Kloth… Kloth… komm zu mir zurück. Bitte… ich… Wie soll ich nur ohne dich zurechtkommen? Du warst mein Leben lang an meiner Seite."
    a "Ich… ich brauche dich. "
    a "Ich… "
    a "Bitte…"
    a "Wieso haben die anderen vorhin nichts gesagt? Sie hätten dich doch sehen müssen. Kloth… warum haben sie dir nicht geholfen?"
    a "Warum sind sie einfach vorbeigegangen und haben dich ignoriert? Vielleicht wärst du dann jetzt noch am Leben."
    a "Verdammt, das darf doch alles nicht wahr sein. Warum nur? Warum? Warum? "
    a "WARUM?"
    a "Kann das alles einfach nur ein schlechter Traum sein? Ich habe nicht die Kraft es durchzustehen, falls es wirklich wahr sein sollte…"
    a "{i}Ja, genau. Es ist nicht mehr als nur ein Traum. Du solltest weitergehen und eine Pause machen. Nimm die Pille, danach wird es dir besser gehen.{/i}"
    a "Ich… ich weiß nicht mehr was ich tun soll… ich will weggehen, aber gleichzeitig habe ich das Gefühl, dass das hier real ist."
    a "Ahhh- mein Kopf tut weh. Da ist irgendeine Erinnerung, aber ich bekomme sie nicht ganz zu fassen… Was ist das?"
    a "Warte. Hatte ich mich nicht gestern mit Kloth unterhalten? Er kam zu mir und…"
    jump letzterTag


label credits:

    scene credits

    "Fortsetzung folgt..."

    return

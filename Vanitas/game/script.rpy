define a = Character("Atropos")
default glitchfertig = False
image pfeil_rechts = Transform ("pfeil",rotate = 180)
image pfeil_rechts_blau = Transform ("pfeilblau",rotate = 180)
image pfeil_unten = Transform ("pfeil",rotate = 270)
image pfeil_unten_blau = Transform ("pfeilblau",rotate = 270)

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
            idle "pfeil_unten"
            hover "pfeil_unten_blau"
            action Jump ("treppenhaus1")

screen pfeil_backtreppe1():
    frame:
        xpos 1700 ypos 500
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

    menu:
        "Ich könnte mir die Plakate mal etwas näher ansehen.":
            jump plakate

        "Ich könnte mal wieder mit meinen Kollegen reden. Vielleicht haben sie interessante Neuigkeiten.":
            jump konversation

        "Ich sollte besser wieder zurück ins Labor. Anan meinte, ich soll die Tablette sofort nachträglich einnehmen.":
            jump treppenhausOhneMenu


label konversation:

    $ konversation = True

    scene menschengruppe
    with zoomin

    a "Hey- schön euch zu sehen. Wie war eure Mittagspause?"
    "Tycho" "Oh, hey. Wir waren gerade unten beim Essen. Wir haben dich schon vermisst- hattest du keinen Hunger?"
    "Neiro" "(lacht) Er hält sich mittlerweile lieber in höheren Kreisen auf, nicht wahr? Ich hatte dich zuvor aus Anans Büro kommen sehen."
    a "Ja, ich war bei ihm, aber…"
    "Neiro" "Wusste ich es doch! Na, wie war es mit dem Chef zu Mittag zu essen? Ich stelle es mir traumhaft vor Zeit mit einem so großen Mann wie ihm zu verbringen."
    "Armene" "Ich wünschte ich hätte einmal das Glück mit ihm persönlich zu sprechen. Es gibt wirklich keine größere Ehre als für Anan zu arbeiten."
    "Era" "Unglaublich charmant und gut aussehend ist er auch noch, das muss mal gesagt sein!"
    "Tycho" "(lacht) Ich glaube nicht, dass das der Grund war, aus welchem Atropos mit ihm zu Mittag gegessen hat. Also los, erzähl schon."
    a "{i}Ich sollte besser nichts von der Pille erwähnen. Sie würden mich vermutlich dafür verurteilen.{/i}"
    a "Ach, es ging um ein paar persönliche Sachen. Nichts weiter Wichtiges."
    "Neiro" "Es ist schon unglaublich, dass sich so eine bedeutende Person wie Anan Zeit für persönliche Gespräche nimmt. Und dabei ist er auch immer so locker und entspannt drauf. "
    "Neiro" "Ich hatte neulich auch mal ein Gespräch mit ihm und…"
    "Tycho" "(lacht)Die Geschichte hast du schon tausend Mal erzählt."
    a "{i}Anan wirkte heute nicht wirklich locker. Aber vielleicht hatte er ja einen stressigen Tag. Er hat immerhin nicht wenig Verantwortung.{/i}"
    a "Heute beim Gespräch wirkte er nicht unbedingt entspannt…"
    "Neiro" "Nun, wenn man so hart und voller Freude arbeitet wie Anan, kann man sich wohl nicht entspannen. Er hat immer etwas zu tun."
    "Era" "Es muss viel Arbeit machen das Glück aller zu erhalten. Wir sind ihm wirklich viel schuldig."
    a "{i}Warum haben sie meine Aussage so sehr verdreht?{/i}"
    a "Nein, so meinte ich das nicht. Es geht mehr darum wie Anan sich verh…"
    "Neiro" "Wir können alle noch viel von Anan lernen. Sein Enthusiasmus ist unglaublich. Aber hier zu arbeiten und das Glück in die Welt zu bringen- es gibt einfach keinen besseren Job."
    "Armene" "Und wir haben das Glück, dass wir unsere Happiness dafür auch noch umsonst bekommen. Kostenloses Glück, besser geht es nicht."
    a "{i}Sie verehren Anan wirklich wie einen Gott. Aber irgendwie… warum ignorieren sie meine Aussagen als wäre ich gar nicht da?{/i}"
    a "{i} Außerdem… Anan… er wirkt seit gestern irgendwie nicht mehr so glücklich und zuvorkommend wie ich ihn in Erinnerung hatte. Irgendetwas ist… {/i}"
    "Tycho" "Oh, wir sollten langsam zurück an die Arbeit. Lass dich morgen mal herab mit uns Gewöhnlichen zu speisen, Atropos. (lacht)"
    "Neiro" "Es ist an der Zeit für Glücklichkeit. (lacht) Bringen wir den Menschen noch mehr davon. Na los, zurück an die Arbeit!"
    a "Wir sehen uns."

    jump treppenhaus1


label plakate:

    hide screen pfeiltreppe

    $ konversation = False

    scene plakate1

    a "Sie stellen sie genauso wie immer dar. Ein perfektes glückliches Leben für jeden."
    a "Wie lösen die Pillen nur diese Glücklichkeit in einem aus? Ich entwickle sie selbst mit, aber ich habe trotzdem keine Ahnung wie sie eigentlich wirken."
    a "Ich sollte mich nicht zu lange mit den Plakaten beschäftigen. Ich habe keine Lust Anan noch einmal über den Weg zu laufen und einen weiteren Anschiss zu riskieren."

    call screen pfeil_backtreppe1

label treppenhaus1:

    if konversation:
        scene treppenhaus1

        a "{i}Irgendetwas war an dem Gespräch seltsam. Aber irgendwie bekomme ich es nicht wirklich zu fassen… ich…{/i}"
        a "{i}Naja, egal. Ich sollte jetzt…{/i}"

        menu:
            "Ich könnte mir nun die Plakate mal etwas näher ansehen.":
                jump treppenhausOhneMenu
            "Ich sollte wirklich keine Zeit mehr verschwenden. Die Pille ist jetzt wichtiger.":
                jump treppenhausOhneMenu2

    else:
        scene treppenhaus1gruppe
        menu:
            "Vielleicht könnte ich noch mit meinen Kollegen reden.":
                jump treppenhausOhneMenu
            "Ich sollte wirklich keine Zeit mehr verschwenden. Die Pille ist jetzt wichtiger.":
                jump treppenhausOhneMenu2

label treppenhausOhneMenu:

    a "{i}Atropos, denk an die Pillen. Du solltest wirklich nicht mehr länger warten. Merkst du nicht, dass du nicht mehr perfekt glücklich bist?{/o}"
    a "{i}Du machst dir zu viele Gedanken und Sorgen. Sei wieder glücklich. Kehre ins Labor zurück und nimm die Happiness-Pille.{/i}"
    a "{i}Ich sollte wirklich die Pille nehmen… was mache ich hier überhaupt noch? Ich sollte gehen.{/i}"

    call screen pfeiltreppe

label treppenhausOhneMenu2:

    "Hier gibt es nichts mehr zum anschauen"

    call screen pfeiltreppe

    # This ends the game.

    #return

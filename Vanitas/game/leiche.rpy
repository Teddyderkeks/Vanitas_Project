define k = Character ("Kloth")

default zustimmen = False

#image sequenz1 = Movie (play = "atropos_will_Kloth_toeten.mov", pos = (10,10))

image glitch:
        "glitch1"
        pause .09
        "glitch2"
        pause .09
        "glitch3"
        pause .09
        "glitch4"
        pause .09
        "glitch5"
        pause .09
        "glitch6"
        pause .09
        "glitch7"
        pause .09
        "glitch8"
        pause .09
        repeat

label letzterTag:
    $ leiche = True
    scene treppenhaus2

    show kloth aengstlich1:
        xalign 0.25
        yalign 1.0

    k "Atropos!"
    a "Kloth, was ist los?"
    k "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"
    a "Beruhige dich erst einmal und atme tief durch. Was ist passiert?"
    k "Nicht hier … es könnte jemand kommen und dann…"
    a "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

    show chesis freundlich:
        xalign 0.75
        yalign 1.0

    k "Ich… ich…"
    a "Ich wollte eigentlich gerade Mittagspause machen. Willst du nicht einfach mitkommen und wir reden dann? Chesis scheint auch Pause zu haben."

    show kloth aengstlich2

    k "Du hörst mir ja gar nicht richtig zu… bitte… ich… ich weiß nicht an wen ich mich sonst wenden soll. Ich brauche dich jetzt."
    k "Es gibt da etwas, das ich schon eine ganze Weile mit mir herumtrage und ich komme alleine einfach nicht damit klar. Bitte, ich muss mit jemanden darüber sprechen."

    show kloth aengstlich1

    k "Du bist der Einzige, der mir helfen kann!"

    menu:
        "Ja, natürlich helfe dich dir. Erzähl endlich was los ist. Wie kann ich dir helfen?":
            jump zustimmen
        "Können wir das Gespräch vielleicht vertagen? Ich habe echt Hunger und ich will zudem Chesis nicht warten lassen.":
            jump verschieben
        "Tut mir leid, aber ich habe gerade nicht den Nerv für ein solches Gespräch. Ich hatte heute einen stressigen Tag und brauche jetzt erstmal wieder etwas Ruhe und Entspannung.":
            jump ablehnen

label zustimmen:

    $ zustimme =True

    k "(atmet erleichtert auf) Danke Atropos. Wirklich… vielen vielen Dank… du weißt nicht wie froh ich bin endlich jemanden zu haben, dem ich mich anvertrauen kann."
    a "Schon okay, nichts zu danken. Wir sind Freunde. Ich bin für dich da. Also, worum geht es?"
    k "Die Happiness-Pille ist nicht das, was du und jeder andere Mensch auf dieser Welt denkt."
    a "Von was redest du? Sie sorgt dafür, dass wir glücklich sind und endlich das Leben unserer Träume leben können. Nicht mehr und nicht weniger."
    k "Nein, das stimmt nicht. Also doch… zum Teil schon, aber es ist nur die halbe Wahrheit. Die Tabletten bewirken nicht wirklich etwas…"
    a "Hör auf um den heißen Brei herumzureden und sag schon, was los ist."

    show kloth aengstlich1

    k "Atropos. Es gibt etwas anderes, das die Menschen ..."

    hide kloth
    #screen glitch

    a "{i}Hör nicht hin. Das sind nichts anderes als Lügen. Alles nur Lügen. Er ist vollkommen wahnsinnig. Siehst du es denn nicht?{/i}"
    a "{i}Er ist nicht glücklich und er wird auch dich unglücklich machen. Willst du dein restliches Leben in Furcht und Angst und Unglücklichkeit verbringen?{/i}"
    a "{i}Willst du ein tristes, graues Leben führen, wenn du ein Leben voller Farben und Freude haben kannst?{/i}"
    a "Nein… nein, ich will ein glückliches Leben haben."

    #screen treppenhaus2

    show kloth aengstlich2

    k "Hast du was gesagt? Geht es dir gut? Du hast ziemlich weggetreten gewirkt."
    a "Ich… was? Ja… ja, mir geht es gut… ich…"
    k "Gut, ich hatte mir schon Sorgen gemacht. Also? Was meinst du sollen wir tun? Das müssen die Menschen erfahren. Wir können sie nicht im Unwissenden lassen…"
    a "{i}Ein glückliches Leben. Ein Leben voller Happiness.{/i}"

    #$ renpy.movie_cutscene("atropos_will_Kloth_toeten.mov")
    #sequenz

    "nein"

    jump treppenhaus2

label ablehnen:

    $ zustimmen = False

    k "Oh okay. Ja klar… wenn du nicht willst… ich kann dich nicht dazu zwingen. Ich wünschte du hättest mir zugehört, Atropos. Ich dachte wir wären Freunde."
    k "Aber da habe ich mich wohl getäuscht. Ich habe mich in dir getäuscht. In dem Moment, in dem ich dich am meisten brauche, bist du nicht für mich da."
    a "{i}Lass dir kein schlechtes Gewissen einreden. Du hast die richtige Entscheidung getroffen.{/i}"
    a "{i}Wie kann er sich dein Freund nennen und dich gleichzeitig in ein tödliches Geheimnis einweihen wollen? So jemand darf sich nicht dein Freund schimpfen.{/i}"
    k "Vielleicht ist Chesis ja ein besserer Freund. Vielleicht hört wenigstens er mir zu."

    # was?

    k "..."
    "Chesis" "..."
    k "..."
    k "… Kontrolle …"
    k "..."

    #sequenz

    jump treppenhaus2

label verschieben:

    k "Kannst du dir nicht jetzt kurz fünf Minuten nehmen? Bitte… es dauert wirklich nicht lange…"
    a "Muss es jetzt sein? Kloth, so wichtig kann es doch gar nicht sein, dass du nicht noch ein bisschen länger warten kannst, oder?"
    a "Ich bezweifle sehr, dass du irgendwelche Staatsgeheimnisse entdeckt hast. Also los, entspann dich und wir sprechen wann anders darüber, okay?"
    k "Jetzt höre mir doch bitte einen Moment zu… es braucht wirklich nicht lange, okay? Ich verspreche es dir…"
    a "Um was geht es denn überhaupt?"
    k "Ich arbeite ja bei Anan als Chefsekretär und nun ja… es ist alles nicht so wie es scheint, Atropos. Ich habe mehr erfahren und ich komme mit dieser Wahrheit nicht alleine klar…"
    a "Wieso flüsterst du? So schlimm kann die Wahrheit schon nicht sein."

    show kloth aengstlich2

    k "Und wie sie es ist. Sie ist gefährlich, vielleicht sogar tödlich… Bitte… können wir an einen ruhigen Ort gehen und ich erzähle dir dann alles?"

    show kloth unsicherlaechelnd

    a "{i}Rede nicht mit ihm. Er hat nichts Gutes im Sinn. Siehst du es denn nicht? Er versucht dich zu manipulieren und zu beeinflussen.{/i}"
    a "{i}Siehst du nicht das grausame Lächeln, welches für einen Moment über sein Gesicht huschte? Lauf weg, solange du noch die Gelegenheit hast.{/i}"
    a "{i}Hast du nicht gehört, dass es sich um ein tödliches Wissen handelt? Willst du dich und deine Glücklichkeit in Gefahr bringen?{/i}"
    a "{i}Lehne das Gespräch ab. Es wäre ein großer Fehler mit ihm zu sprechen. Er wird dein Glück zerstören und dich in einen dunklen Abgrund mitreißen.{/i}"

    menu:
        "Nein, tut mir leid, aber das ist mir alles zu riskant und unsicher. Ich will lieber weiterhin mein glückliches Leben führen.":
            jump ablehnen
        "Alles gut, von mir aus. Ich höre dir zu. Aber hier und jetzt. Ich möchte noch ein bisschen was von meiner Mittagspause haben.":
            jump zustimmen



    #menu:
        #"Ja":

        #"Nein"
    jump treppenhaus2

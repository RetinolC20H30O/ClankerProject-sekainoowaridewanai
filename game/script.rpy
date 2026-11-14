# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wtf = Character("???")
define ai = Character("Inori")
define anc = Character("Announcement")
define mc = Character("Akira Satou")
define car = Character("Driver")

default preferences.text_cps = 45

transform splash_fade:
    alpha 0.0
    linear 0.5 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0

screen splash_text(message):
    modal True
    add "#000"

    text message:
        xalign 0.5
        yalign 0.5
        at splash_fade

    # Auto-advance after the fade in, hold, and fade out (0.5 + 1.0 + 0.5)
    timer 2.0 action Return()

    # Click, Enter, or Space skips just this one
    key "dismiss" action Return()

label splashscreen:

    scene black
    with Pause(1.0)

    call screen splash_text("BAANPHONG Studios presents")
    pause 0.5

    call screen splash_text("The World isn't Ending Yet.")
    pause 0.5

    return
# The game starts here.
label start:
    stop music fadeout 1.25

    scene black
    with dissolve
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg wtf.png" or "bg wtf.jpg") to the
    scene black with fade
    "In this era, artificial intelligence is a highly profitable section in the startup world."
    "All the new companies around the world are developing their own artificial intelligence."
    "{cps=25}So I, an independent developer, tried developing the most advanced artificial intelligence in the world."
    scene proj with fade
    play music "audio/what_could_go_wrong_rework.ogg"
    "I call this project 'INORI'"
    "INORI have been under development for years now. And finally, the project is almost finished."
    scene black with fade
    stop music fadeout 0.5
    "But... the path is not smooth as I thought..."
    scene invade with fade
    "My rival company, which had been watching us during the project, had decided to interfere."
    "{cps=20}They sent troops to end this project at last."
    scene black with fade
    pause 0.5
    show text "I managed to escape and activate my AI in time." at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    pause 0.5
    scene bg wtf
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    wtf "I am thankful for my creation, Satou-sama."
    wtf "..."
    wtf "Please, take your time."
    scene black with fade
    pause 0.5
    show text "2037" at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    pause 0.5

    scene train_2
    play music "audio/Satou_maintheme.ogg"
    anc "{cps=20}This is a local train bound for Nanishima, the next stop is Baguette."
    "My name's Akira Satou. I've lived in this small, weird-named town for as long as i can remember"
    "Until a year ago that I had to flee the town."
    "I wonder how my hometown looks like now."
    with fade
    anc "{cps=20}We will soon be arriving at Baguette, the doors on the left side will open."
    with fade
    "Where is everyone?"
    stop music fadeout 1.0
    wtf "Long time no see, master!"
    play music "audio/what_could_go_wrong_rework.ogg" fadein 0.5
    "It was a very soft, comforting sound of a woman."
    "I glanced towards the sound."
    mc "Project INORI Class-S No.1!?"
    "She's the android I had created."
    "I should really give her a nickname..."
    mc "From now, you'll just be Inori."
    ai "Inori?"
    mc "Inori from the verb {i}Inoru{/i}, means 'to wish'"
    ai "Noted."
    "A taxi stopped infront of the station."
    mc "Look, a cab! Perfect!"
    "I open the door to the cab."
    mc "Baguette, please,"
    stop music fadeout 0.5
    "The driver went silent."
    car "Sorry kid, I can't go there. Place is closed."
    mc "What? Whatdoyamean?"
    car "I just... I can't take you there kid. Sorry."
    mc "Oh, thank you anyway..."
    "I closed the door"
    ai "What is going on...?"
    mc "I don't know... but the bigger problem seems to be that we have to walk there."
    ai "WE'RE GOING TO {i}WHAT!?{/i}"
    scene black with fade
    pause 0.5
    # This ends the game.

    return

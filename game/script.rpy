# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wtf = Character("???")
define ai = Character("Inori")
define anc = Character("Announcement")
define mc = Character("Akira Satou")

default preferences.text_cps = 40

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
    scene black
    with fade
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg wtf.png" or "bg wtf.jpg") to the
    # images directory to show it.

    scene bg wtf
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    wtf "I am thankful for my creation, Satou-sama."
    wtf "..."
    wtf "Please, take your time."

    with fade
    scene black
    show text "2037"
    with Pause(1.0)

    scene bg train
#line 67
    anc "{cps=20}This is a local train bound for Nanishima, the next stop is Baguette."
    "My name's Akira Satou. I've lived in this small, weird-named town for as long as i can remember"
    "A year ago, I created an android that resembles the girl of my dreams. Because, obviously, I do not have a human partner."
    "But all of a sudden, I had to travel for an overseas business camp."
    "I wonder how my hometown looks like now."
    with fade
    anc "{cps=20}We will soon be arriving at Baguette, the doors on the left side will open."
    with fade
    "Where is everyone?"
    wtf "Long time no see, master!"
    "It was a very soft, comforting sound of a woman."
    "I glanced towards the sound."
    mc "gAI-001!"
    "She's the android I had created."
    "I should really give her a nickname..."
    mc "From now, you'll be Inori."
    ai "Inori?"
    mc "Your new name. Inori from the verb {i}Inoru{/i}, means 'to wish'"
    ai "How lovely!"
    # This ends the game.

    return

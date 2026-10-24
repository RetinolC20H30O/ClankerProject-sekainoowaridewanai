# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wtf = Character("???")
define ai = Character("gAI-001")

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

    play sound "audio/intro.wav"

    call screen splash_text("BAANPHONG Studios presents")
    pause 0.5

    call screen splash_text("The World isn't Ending Yet.")
    pause 0.5

    return
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    wtf "I am thankful for my creation, Satou-sama."
    wtf "..."
    wtf "Please, take your time.

    # This ends the game.

    return

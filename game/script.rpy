# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wtf = Character("???")

label splashscreen:

    scene black
    with Pause(1.0)

    play sound "audio/intro.wav"
    show text "BAANPHONG Studios presents" at truecenter with dissolve
    renpy.pause(1.0, hard=True)
    hide text with dissolve
    with Pause(0.5)

    show text "The World isn't Ending Yet." at truecenter with dissolve
    with Pause(1.0)
    hide text with dissolve
    with Pause(0.5)

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

    wtf "skibidi sigma placeholder 6767"
    wtf "this is a placeholder"

    # This ends the game.

    return

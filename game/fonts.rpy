default persistent.font_choice = "serif"

init python:
    # language key = the name of your tl/ folder (None = default language)
    FONTS = {
        "serif": {
            None:       "fonts/NotoSerif-Regular.ttf",
            "japanese": "fonts/NotoSerifJP-Regular.ttf",
            "thai":     "fonts/NotoSerifThai-Regular.ttf",
        },
        "sans": {
            None:       "fonts/NotoSans-Regular.ttf",
            "japanese": "fonts/NotoSansJP-Regular.ttf",
            "thai":     "fonts/NotoSansThai-Regular.ttf",
        },
    }

    def set_fonts():
        choice = persistent.font_choice or "serif"
        options = FONTS.get(choice, FONTS["serif"])
        path = options.get(_preferences.language, options[None])
        gui.text_font = path
        gui.name_text_font = path
        gui.interface_text_font = path
        gui.button_text_font = path
        gui.choice_button_text_font = path

    def change_font(choice):
        persistent.font_choice = choice
        set_fonts()
        gui.rebuild()

    set_fonts()

# Re-apply whenever the language changes
translate japanese python:
    set_fonts()

translate thai python:
    set_fonts()

translate None python:
    set_fonts()

init python:
    config.after_load_callbacks.append(set_fonts)
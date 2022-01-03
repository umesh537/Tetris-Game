from pygame import mixer

def main_theme(volume_value):
    theme_sound = r".\music&imgsrc\Original Tetris theme.mp3"
    mixer.music.load(theme_sound)
    mixer.music.play(-1)
    mixer.music.set_volume(volume_value)


def drop_theme():
    drop_sound = r".\music&imgsrc\rotation.mp3"
    mixer.music.load(drop_sound)
    mixer.music.play()

def success_theme():
    success_sound = r".\music&imgsrc\clear.mp3"
    mixer.music.load(success_sound)
    mixer.music.play()


def fail_theme():
    fail_sound = r".\music&imgsrc\fail.mp3"
    mixer.music.load(fail_sound)
    mixer.music.play()

def fall_theme():
    drop_sound = r".\music&imgsrc\fall.mp3"
    mixer.music.load(drop_sound)
    mixer.music.play()

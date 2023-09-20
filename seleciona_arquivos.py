import os

def select_mp3_files():
    mp3_files = []
    for file in os.listdir():
        if file.endswith(".mp3"):
            mp3_files.append(file)
    return mp3_files

mp3_files = select_mp3_files()
print(mp3_files)
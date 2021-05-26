import os

path = 'songs'
song_list = os.listdir(path)
print(song_list)
def scall():
    for i in range(len(song_list)):
        print(i+1, '.', song_list[i][:-4])
def select_song():
    scall()
    select = int(input("Select a song which you want to see lyrics of that:"))
    if select in [i+1 for i in range(len(song_list))]:
        print(f'You chose {song_list[select-1][:-4]}. Here you go:')
        print()
        print(f'{"-"*10}{song_list[select-1][:-4]}{"-"*10}')
        with open(f"songs/{song_list[select-1]}", 'r') as lyric:
            print(lyric.read())
    else:
        print("invalid option, press * and select from list")

select_song()
while True:
    repeat = input("Press * to choose again or press any key to quit.")
    if repeat == "*":
        select_song()
    else:
        break




def make_album(artist: str, title: str, number_of_songs: int = False) -> dict: 
    if number_of_songs:
        album = {
            'artist name': artist, 
            'album title': title, 
            'number of songs': number_of_songs
            }
    else:
        album = {
            'artist name': artist, 
            'album title': title,
            }
    return album

album1 = make_album('Big Pun', 'Capital Punishment')
album2 = make_album('Weeknd', 'Starboy', 18)
album3 = make_album('Eminem', 'The Marshall Mathers LP', 27)

print(album1)
print(album2)
print(album3)

while True:
    print('\nPlease tell me the album details')
    print('(enter "q" at any time to quit)')
    
    artist = input('Artist name: ')
    if artist == 'q':
        break
    
    title = input('Title of album: ')
    if title == 'q':
        break
    album = make_album(artist, title)
    print(f'The details of the album are: {album}')
    repeat = input('do you want to continue? (y/n): ')
    if repeat.lower() != 'y':
        break

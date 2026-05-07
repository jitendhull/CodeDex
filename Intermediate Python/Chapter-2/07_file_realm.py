liked_songs = {
  'Bad Habits': 'Ed Sheeran',
  'Mastermind': 'Taylor Swift'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in liked_songs.items():
            file.write(f' {song} by {artist}\n')
    

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
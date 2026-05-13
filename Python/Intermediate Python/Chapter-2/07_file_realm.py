liked_songs = {
  'Bad Habits': 'Ed Sheeran',
  'Mastermind': 'Taylor Swift'
}

def write_liked_songs_to_file(liked_songs, file_name):
    # Open the file in write mode and write the header
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        # Loop through the liked songs and write each song and artist to the file
        for song, artist in liked_songs.items():
            file.write(f' {song} by {artist}\n')
    
# Call the function to write the liked songs to a file
write_liked_songs_to_file(liked_songs, 'liked_songs.txt')


#    First of all we define the Dictionary Containing Song names and It Artists. 
#    Then we create a function that takes the liked_songs dictionary and a file name as paramaters.
#    Inside the function, we open the file in write mode and write a header "Liked Songs".
#    Then we loop through the liked_songs dictionary and write each song and its artist to the file in the format "song by artist".
#    Finally, we call the function to write the liked songs to a file named 'liked_songs.txt'.
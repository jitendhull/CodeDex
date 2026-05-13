# For many, music is so personal. We have created a playlist of songs that have won the “Song of the Year” 🏆 Grammy award in the past 5 years.

# Let's play around with the data!

# # List of songs with their durations (in minutes)
# playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

# First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

# Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

# Lastly, add up the total playtime of the playlist with reduce().

# Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

# A longer_than_five_minutes() function for filter().
# A minutes_to_seconds() function for map().
# An add_durations() function for reduce().

from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5.00

longer_than_five_minute_songs = list(filter(longer_than_five_minutes, playlist))

def convert_to_seconds(song):
    return (song[0], song[1] * 60)


songs_in_seconds = list(map(convert_to_seconds, playlist))

def add_durations(total, song):
    return total + song[1]

total_playtime = reduce(add_durations, songs_in_seconds, 0)

print(longer_than_five_minute_songs)
print(songs_in_seconds)
print(total_playtime)
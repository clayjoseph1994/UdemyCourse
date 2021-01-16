playlist = {
    "Title": "My Playlist", 
    "Creator": "Joseph",
    "Songs": [
        {"Song Title": "Enter Sandman", "Artist": ["Metallica"], "Duration(mins)": 2.5},
        {"Song Title": "Fade to Black", "Artist": ["Metallica", "The Chainsmokers"], "Duration(mins)": 2.7},
        {"Song Title": "Another Brick in the Wall", "Artist": ["Pink Floyd"], "Duration(mins)": 3.2},
        {"Song Title": "Big Booty Gurl", "Artist": ["Ke$ha"], "Duration(mins)": 6.7}
    ]
}

total_len = 0
for song in playlist["Songs"]:
    #print(song["Duration(mins)"])
    total_len += song["Duration(mins)"]

print(total_len)


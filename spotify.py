import spotipy
from spotipy.oauth2 import SpotifyOAuth

# This is hardcoded into David (the maker of this)'s spotify right now.
# Functionality to change this coming soon
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    # to get your ids, go to spotify developer
    client_id="ENTER ID HERE",         # Replace with your Client ID
    client_secret="ENTER ID HERE", # Replace with your Client Secret
    redirect_uri="http://localhost:8888/callback",  # Use the same redirect URI in your Spotify app
    scope=["user-library-read", "user-read-playback-state", "user-modify-playback-state"]
))

def get_current_song():
    playback = sp.current_playback()

    if playback is not None and playback['is_playing']:
        track = playback['item']
        song_name = track['name']
        artist_name = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        
        return f"Currently Playing: {song_name} by {artist_name} from the album {album_name}"
    else:
        return "No song is currently playing."

def toggle_playback():
    # Get the current playback state
    playback = sp.current_playback()

    if playback is not None and playback['is_playing']:
        print("Pausing the current song...")
        sp.pause_playback()
    elif playback is not None:
        print("Resuming the current song...")
        sp.start_playback()
    else:
        print("No playback is currently active.")
    
def update_song_label(label):
    current_song = get_current_song()
    label.config(text=f"{current_song}")
    label.after(1000, update_song_label, label)

    

def skip_song():
    sp.next_track()
    print("Song skipped to the next track.")

def instantiateWindow(mainWindow, tk):
    spotify_window = tk.Toplevel(mainWindow)
    spotify_window.title("Spotify")
    spotify_window.attributes("-topmost", True)

    song_label = tk.Label(spotify_window, text=get_current_song(), font=("Arial", 8))
    song_label.pack(pady=20)

    update_song_label(song_label)
    
    playPauseButton = tk.Button(spotify_window, text="Pause/unpause", command=toggle_playback)
    playPauseButton.pack(side=tk.LEFT, padx=5)

    skipSongButton = tk.Button(spotify_window, text="Skip song", command=skip_song)
    skipSongButton.pack(side=tk.LEFT, padx=5)



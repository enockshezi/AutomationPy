import os
from pytube import YouTube
musicDist = "/mnt/c/Users/shezi/Music"

def download_audio(url,songname):
    # Create a YouTube object
    yt = YouTube(url)

    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Set the output file path
    output_file = f"{os.path.splitext(os.path.basename(url))[0]}.mp3"

    # Download the audio stream
    audio_stream.download(output_path=musicDist, filename=songname)

    print("Audio downloaded successfully!")

if __name__ == "__main__":
    while True:
        youtube_url = input("Enter the YouTube video URL or done to stop: ")
        if youtube_url == "done":
            break 
        
        else:
            song_name = input("Enter the name of the song: ")
            song_name = song_name+".mp3"
            download_audio(youtube_url,song_name)
            

from pytube import YouTube
from tqdm import tqdm
import time

def download_video(url, resolution='1080p'):
    try:
        yt = YouTube(url)

        if resolution == '1080p':
            stream = yt.streams.filter(progressive=False, file_extension='mp4', resolution='1080p').first()
            audio_stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not stream:
            print("No stream found with the specified resolution.")
            return

        # Print video details
        print(f"Title: {yt.title}")
        print(f"Duration: {yt.length} seconds")
        print(f"Resolution: {stream.resolution}")
        print(f"Downloading...")

        # Start the timer
        start_time = time.time()
        if resolution == '1080p':
            video_file = stream.download(filename='video.mp4')
            audio_file = audio_stream.download(filename='audio.mp4')
            print("Merging video and audio...")
            # Use ffmpeg to merge video and audio
            import subprocess
            subprocess.run(['ffmpeg', '-i', 'video.mp4', '-i', 'audio.mp4', '-c:v', 'copy', '-c:a', 'aac', 'output.mp4'])
            print("Download and merge complete!")
        else:
            stream.download()

        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url, resolution='1080p')

import yt_dlp
import json
import os
from datetime import datetime

def download_channel(channel_url, quality='1080', output_dir='downloads'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    format_map = {
        '4k': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '1080': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',
        '720': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best',
        '480': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best',
        'lowest': 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst'
    }
    
    ydl_opts = {
        'format': format_map.get(quality, 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best'),
        'outtmpl': f'{output_dir}/%(title)s/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'writeinfojson': True,
        'writethumbnail': True,
        'writedescription': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'json3',
        'allsubtitles': False,
        'subtitleslangs': ['en'],
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'srt',
        }],
        'verbose': True,
        'progress': True,
        'progress_hooks': [lambda d: print(f"Status: {d['status']} - {d.get('filename', '')}")],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Starting download...")
            ydl.download([channel_url])
            print("Download complete!")
            
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    channel_url = "https://www.youtube.com/@dallaswillard"  # Replace with the actual channel URL
    download_channel(channel_url)

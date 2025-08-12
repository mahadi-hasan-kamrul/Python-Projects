# First install yt-dlp: pip install yt-dlp
import yt_dlp # type: ignore
import os
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        os.makedirs(save_path, exist_ok=True)
        
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best',
            'ffmpeg_location': r'project path\ffmpeg\bin\ffmpeg.exe',  # UPDATE THIS PATH
            'quiet': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"✅ Downloaded: {info['title']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")



def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
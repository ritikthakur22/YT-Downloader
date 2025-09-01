import os
import shutil
import platform
from yt_dlp import YoutubeDL, DownloadError

def check_dependencies():
    """Checks for required external dependencies."""
    missing_deps = []
    if not shutil.which("aria2c"):
        missing_deps.append("aria2c")
    if not shutil.which("ffmpeg"):
        missing_deps.append("ffmpeg")

    if missing_deps:
        print("🚨 Error: Missing required dependencies.")
        print("Please install the following and make sure they are in your PATH:")
        for dep in missing_deps:
            print(f"- {dep}")
        
        system = platform.system()
        if system == "Linux":
            print("\nTo install on Debian/Ubuntu, you can use: sudo apt update && sudo apt install -y aria2 ffmpeg")
        elif system == "Darwin":
            print("\nTo install on macOS with Homebrew, you can use: brew install aria2 ffmpeg")
        elif system == "Windows":
            print("\nTo install on Windows with Chocolatey, you can use: choco install aria2 ffmpeg")
        
        exit(1)

def prompt_link_type():
    print("\n📦 What are you downloading?")
    print("1. Single YouTube Video")
    print("2. YouTube Playlist")
    while True:
        choice = input("Choose [1/2]: ").strip()
        if choice in ["1", "2"]:
            return choice
        print("Invalid choice. Please enter 1 or 2.")

def prompt_format_type():
    print("\n🎧 Which format do you want?")
    print("1. Audio (MP3)")
    print("2. Video (MP4)")
    while True:
        choice = input("Choose [1/2]: ").strip()
        if choice in ["1", "2"]:
            return choice
        print("Invalid choice. Please enter 1 or 2.")

def prompt_quality(is_audio):
    if is_audio:
        return input("🎚️ Audio Quality [0=Best, 9=Worst] (default=0): ").strip() or "0"
    else:
        return input("🎚️ Max video resolution? [e.g., 720, 1080] (leave empty for best): ").strip()

def prompt_aria2c_threads():
    """Prompt for the number of connections for aria2c."""
    print("\n🚀 Download Speed")
    return input("Number of connections for each download (aria2c -x)? [1-16] (default=5): ").strip() or "5"

def build_ydl_opts(format_type, quality, threads, is_playlist):
    download_dir = "Downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        
    if is_playlist:
        outtmpl = os.path.join(download_dir, '%(playlist_index)s - %(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(download_dir, '%(title)s.%(ext)s')

    opts = {
        'outtmpl': outtmpl,
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x', threads, '-k', '1M'],
        'ignoreerrors': True,
        'retries': 5,
        'download_archive': '.downloaded_files.txt' # Keep track of downloaded files
    }

    if format_type == "audio":
        opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }]
        })
    else: # video
        format_spec = 'bestvideo+bestaudio/best'
        if quality:
            format_spec = f'bestvideo[height<={quality}]+bestaudio/best'
        opts['format'] = format_spec
        opts['merge_output_format'] = 'mp4' # To ensure mp4 container

    return opts

def run_downloader(url, opts):
    print("\n⬇️ Starting download...")
    try:
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("\n✅ Download finished!")
    except DownloadError as e:
        print(f"\n❌ An error occurred during download: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    check_dependencies()
    link_type = prompt_link_type()
    url = input("🔗 Paste YouTube URL: ").strip()
    format_choice = prompt_format_type()
    format_type = "audio" if format_choice == "1" else "video"
    quality = prompt_quality(format_type == "audio")
    threads = prompt_aria2c_threads()

    ydl_opts = build_ydl_opts(format_type, quality, threads, is_playlist=(link_type == "2"))
    run_downloader(url, ydl_opts)

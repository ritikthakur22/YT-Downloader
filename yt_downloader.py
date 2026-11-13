import os
import sys
import shutil
import platform
from yt_dlp import YoutubeDL, DownloadError

def check_dependencies():
    """Checks for required external dependencies and returns aria2c availability."""
    if not shutil.which("ffmpeg"):
        print("Error: Missing required dependency: ffmpeg")
        system = platform.system()
        if system == "Linux":
            print("Install with: sudo apt install ffmpeg (Debian/Ubuntu) or sudo pacman -S ffmpeg (Arch)")
        elif system == "Darwin":
            print("Install with: brew install ffmpeg")
        elif system == "Windows":
            print("Install with: choco install ffmpeg")
        sys.exit(1)

    has_aria2c = bool(shutil.which("aria2c"))
    if not has_aria2c:
        print("[Notice] aria2c not found. Using yt-dlp default downloader (install aria2 for faster speeds).")

    return has_aria2c

def prompt_url():
    while True:
        url = input("Enter YouTube URL: ").strip()
        if url.startswith("http://") or url.startswith("https://"):
            return url
        print("Please enter a valid URL (starting with http:// or https://).")

def prompt_link_type():
    print("\nDownload Type:")
    print("1. Single Video")
    print("2. Playlist")
    while True:
        choice = input("Select [1/2] (default=1): ").strip() or "1"
        if choice in ["1", "2"]:
            return choice == "2"
        print("Invalid choice. Please enter 1 or 2.")

def prompt_format_type():
    print("\nFormat:")
    print("1. Audio (MP3)")
    print("2. Video (MP4)")
    while True:
        choice = input("Select [1/2] (default=2): ").strip() or "2"
        if choice in ["1", "2"]:
            return "audio" if choice == "1" else "video"
        print("Invalid choice. Please enter 1 or 2.")

def prompt_quality(is_audio):
    if is_audio:
        choice = input("Audio Quality [0=Best, 9=Worst] (default=0): ").strip() or "0"
        return choice if choice.isdigit() and 0 <= int(choice) <= 9 else "0"
    else:
        res = input("Max video resolution [e.g. 720, 1080] (leave empty for best): ").strip()
        return res if res.isdigit() else ""

def prompt_threads():
    choice = input("Number of download connections [1-16] (default=5): ").strip() or "5"
    if choice.isdigit() and 1 <= int(choice) <= 16:
        return choice
    return "5"

def build_ydl_opts(format_type, quality, threads, is_playlist, has_aria2c):
    download_dir = "Downloads"
    os.makedirs(download_dir, exist_ok=True)

    if is_playlist:
        outtmpl = os.path.join(download_dir, '%(playlist_title)s', '%(playlist_index)02d - %(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(download_dir, '%(title)s.%(ext)s')

    opts = {
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'retries': 5,
        'download_archive': '.downloaded_files.txt',
    }

    if has_aria2c:
        opts['external_downloader'] = 'aria2c'
        opts['external_downloader_args'] = ['-x', threads, '-k', '1M']

    if format_type == "audio":
        postprocessors = [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            },
            {'key': 'FFmpegMetadata'},
        ]

        # Use mutagen if installed to embed album cover art into the mp3
        try:
            import mutagen  # noqa: F401
            opts['writethumbnail'] = True
            postprocessors.append({'key': 'EmbedThumbnail'})
        except ImportError:
            pass

        opts.update({
            'format': 'bestaudio/best',
            'postprocessors': postprocessors,
        })
    else:
        format_spec = f'bestvideo[height<={quality}]+bestaudio/best' if quality else 'bestvideo+bestaudio/best'
        opts['format'] = format_spec
        opts['merge_output_format'] = 'mp4'

    return opts

def run_downloader(url, opts):
    print("\nStarting download...")
    try:
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
        print("\nDownload finished!")
    except DownloadError as e:
        print(f"\nDownload error: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

def main():
    try:
        has_aria2c = check_dependencies()
        url = prompt_url()
        is_playlist = prompt_link_type()
        format_type = prompt_format_type()
        quality = prompt_quality(format_type == "audio")
        threads = prompt_threads() if has_aria2c else "1"

        opts = build_ydl_opts(format_type, quality, threads, is_playlist, has_aria2c)
        run_downloader(url, opts)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()

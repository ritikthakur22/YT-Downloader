# YT-Downloader

A simple Python CLI to download YouTube videos and playlists as MP4 or MP3, using `yt-dlp` and `aria2c` for multi-connection speed.

## Prerequisites

You need Python 3.8+ and two system packages installed and available in your `PATH`:
- `ffmpeg` (for audio extraction and video remuxing)
- `aria2` (for multi-threaded downloads)

### Install dependencies:

- **Ubuntu / Debian:**
  ```bash
  sudo apt update && sudo apt install -y aria2 ffmpeg
  ```
- **Arch Linux:**
  ```bash
  sudo pacman -S aria2 ffmpeg
  ```
- **macOS:**
  ```bash
  brew install aria2 ffmpeg
  ```
- **Windows:**
  ```powershell
  choco install aria2 ffmpeg
  ```

## Setup

```bash
git clone https://github.com/ritikthakur22/YT-Downloader.git
cd YT-Downloader
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python yt_downloader.py
```

The script will prompt you for:
1. Single video or playlist
2. YouTube URL
3. Format (MP3 audio or MP4 video)
4. Quality (audio VBR 0–9 or max video height like `1080`)
5. Aria2c connections (default: 5)

Downloaded files are saved in the `Downloads/` directory. Completed downloads are logged in `.downloaded_files.txt` so re-running a playlist skips already downloaded videos.

## Notes

If downloads fail due to YouTube changes, update `yt-dlp`:
```bash
pip install -U yt-dlp
```

## License

[MIT](LICENSE)

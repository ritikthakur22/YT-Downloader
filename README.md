# YT-Downloader 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/Powered%20By-yt--dlp-red?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp)
[![aria2c](https://img.shields.io/badge/Accelerated%20By-aria2c-blue?style=for-the-badge)](https://aria2.github.io/)
[![ffmpeg](https://img.shields.io/badge/Audio%2FVideo%20Processing-FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A fast, interactive command-line YouTube video and playlist downloader written in Python. It leverages **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** for robust media extraction, **[aria2c](https://aria2.github.io/)** for multi-connection download acceleration, and **[FFmpeg](https://ffmpeg.org/)** for audio extraction and video post-processing.

---

## ✨ Features

- 📹 **Single Videos & Playlists**: Download standalone videos or entire playlists with formatted index prefixes.
- ⚡ **Multi-Connection Acceleration**: Accelerated downloads using external downloader `aria2c` with configurable threads (1–16).
- 🎵 **High-Quality Audio Extraction**: Convert YouTube audio directly into MP3 with customizable quality levels (`0` = Best to `9` = Smallest).
- 🎬 **Customizable Video Resolutions**: Select specific maximum resolutions (e.g., `720p`, `1080p`, `1440p`, `2160p`) or automatically fetch the best available stream merged into MP4 container.
- 🔄 **Smart Archive Tracking**: Automatically records downloaded videos in `.downloaded_files.txt` to avoid re-downloading duplicate files across runs.
- 🛡️ **Dependency Verification**: Checks for external system dependencies (`aria2c` and `ffmpeg`) before starting and provides platform-specific installation instructions.
- 🔁 **Resilient Downloading**: Automatic error handling with 5 retries on network dropouts.

---

## 📋 Prerequisites

Before running the downloader, make sure you have the following installed on your system:

1. **Python 3.8+**
2. **FFmpeg** (required for remuxing video and extracting audio)
3. **aria2c** (required for multi-threaded download acceleration)

### Installing System Dependencies

#### Linux (Debian / Ubuntu / Pop!_OS)
```bash
sudo apt update && sudo apt install -y aria2 ffmpeg
```

#### Linux (Arch / Manjaro)
```bash
sudo pacman -S aria2 ffmpeg
```

#### Linux (Fedora)
```bash
sudo dnf install aria2 ffmpeg-free
```

#### macOS (via [Homebrew](https://brew.sh/))
```bash
brew install aria2 ffmpeg
```

#### Windows (via [Chocolatey](https://chocolatey.org/) or [Scoop](https://scoop.sh/))
```powershell
# Using Chocolatey
choco install aria2 ffmpeg

# Using Scoop
scoop install aria2 ffmpeg
```
> **Note for Windows:** Ensure both `aria2c.exe` and `ffmpeg.exe` are added to your system's `PATH`.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ritikthakur22/YT-Downloader.git
   cd YT-Downloader
   ```

2. **(Recommended) Create and activate a virtual environment:**
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Usage

Run the script from your terminal:

```bash
python yt_downloader.py
```

Follow the interactive prompts:

```text
📦 What are you downloading?
1. Single YouTube Video
2. YouTube Playlist
Choose [1/2]: 1

🔗 Paste YouTube URL: https://www.youtube.com/watch?v=...

🎧 Which format do you want?
1. Audio (MP3)
2. Video (MP4)
Choose [1/2]: 2

🎚️ Max video resolution? [e.g., 720, 1080] (leave empty for best): 1080

🚀 Download Speed
Number of connections for each download (aria2c -x)? [1-16] (default=5): 8

⬇️ Starting download...
✅ Download finished!
```

All downloaded media files will be saved in the `Downloads/` directory inside the project root:
- **Single Video:** `Downloads/<video_title>.<ext>`
- **Playlist Video:** `Downloads/<playlist_index> - <video_title>.<ext>`

---

## ⚙️ Options & Interactive Prompts

| Prompt | Option / Input | Description |
|---|---|---|
| **Content Type** | `1` / `2` | Choose between downloading a **Single Video** or **Full Playlist**. |
| **URL** | YouTube URL | Accepts standard video URLs, shortened `youtu.be` links, or playlist URLs. |
| **Format** | `1` (Audio) / `2` (Video) | Extracts **MP3** audio or merges streams into an **MP4** video container. |
| **Quality** | `0`–`9` (Audio) or height (Video) | For MP3: `0` is highest VBR quality. For MP4: enter target max height (e.g. `1080`), or press Enter for best. |
| **Connections** | `1`–`16` | Number of concurrent connections for `aria2c -x` (default: `5`). |

---

## 📁 Project Structure

```text
YT-Downloader/
├── Downloads/               # Auto-created folder where downloaded files are saved
├── .downloaded_files.txt    # Download archive history to prevent duplicate downloads
├── .gitignore               # Ignored files and directories for Git
├── requirements.txt         # Python dependencies (yt-dlp)
├── yt_downloader.py         # Main interactive CLI script
└── README.md                # Project documentation
```

---

## 🛠️ Updating yt-dlp

YouTube frequently changes its internal player mechanisms. If you ever run into download errors, update `yt-dlp` to the latest release:

```bash
pip install --upgrade yt-dlp
```

---

## ⚖️ Disclaimer

This tool is created for educational and personal archival purposes only. Please respect YouTube's [Terms of Service](https://www.youtube.com/t/terms) and the intellectual property rights of content creators. Ensure you have the right or permission before downloading copyrighted material.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

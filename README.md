# YT-Downloader 🚀

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/Powered%20By-yt--dlp-red?style=for-the-badge" alt="yt-dlp" />
  <img src="https://img.shields.io/badge/Speed%20Boost-aria2c-0052CC?style=for-the-badge" alt="aria2c" />
  <img src="https://img.shields.io/badge/Remuxing-FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFmpeg" />
  <img src="https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <b>A fast, lightweight, and interactive YouTube downloader for videos and playlists.</b><br>
  Extract crystal-clear <b>MP3</b> audio or high-definition <b>MP4</b> video with multi-threaded acceleration!
</p>

---

## ✨ Features

- 📹 **Single Videos & Full Playlists**: Download standalone videos or entire playlists automatically categorized into dedicated folders.
- ⚡ **Multi-Connection Acceleration**: Integrated with `aria2c` multi-threaded engine (1–16 connections) for blazing fast download speeds (with automatic fallback to native downloader).
- 🎧 **High-Quality Audio Extraction**: Converts audio to MP3 with customizable VBR quality levels (`0` = Best to `9` = Smallest) and auto-tags artist/title metadata.
- 🎬 **Customizable Video Resolutions**: Select your desired maximum resolution (`720p`, `1080p`, `1440p`, `4K`) or grab the highest available quality merged into an MP4 container.
- 🔄 **Smart Archive Tracking**: Automatically logs downloaded videos in `.downloaded_files.txt` to prevent duplicate re-downloads when restarting playlists.
- 🛡️ **Intelligent Dependency Detection**: Automatically checks for `ffmpeg` and `aria2c` with quick-install hints for your operating system.
- 🛑 **Graceful Interrupts**: Clean cancellation handling on `Ctrl + C` without ugly error traces.

---

## 📋 Prerequisites

To get the best experience, ensure you have:
1. **Python 3.8+**
2. **FFmpeg** *(Required for audio conversion and video merging)*
3. **aria2c** *(Optional, recommended for accelerated multi-connection speeds)*

### 📦 Quick Install External Dependencies

| Platform | Command |
|---|---|
| **Debian / Ubuntu / Pop!_OS** | `sudo apt update && sudo apt install -y aria2 ffmpeg` |
| **Arch Linux / Manjaro** | `sudo pacman -S aria2 ffmpeg` |
| **Fedora** | `sudo dnf install aria2 ffmpeg-free` |
| **macOS (Homebrew)** | `brew install aria2 ffmpeg` |
| **Windows (Chocolatey)** | `choco install aria2 ffmpeg` |
| **Windows (Scoop)** | `scoop install aria2 ffmpeg` |

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ritikthakur22/YT-Downloader.git
   cd YT-Downloader
   ```

2. **Create and activate a virtual environment:**
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

## 🎮 Interactive Usage

Launch the script directly from your terminal:

```bash
python yt_downloader.py
```

### 💻 Walkthrough Example

```text
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Download Type:
1. Single Video
2. Playlist
Select [1/2] (default=1): 1

Format:
1. Audio (MP3)
2. Video (MP4)
Select [1/2] (default=2): 2

Max video resolution [e.g. 720, 1080] (leave empty for best): 1080
Number of download connections [1-16] (default=5): 8

Starting download...
[download] 100% of 34.20MiB in 00:03
Download finished!
```

---

## ⚙️ Options Reference

| Setting | Input / Choices | Description |
|---|---|---|
| **URL** | YouTube URL | Accepts standard, shortened (`youtu.be`), or playlist links. |
| **Download Type** | `1` (Single) / `2` (Playlist) | Single video goes to `Downloads/`; Playlists get their own organized subfolder. |
| **Format** | `1` (MP3) / `2` (MP4) | Extracts audio to MP3 or combines best audio+video into MP4. |
| **Quality** | `0`–`9` (Audio) or height (Video) | For MP3: `0` is best VBR. For Video: target max resolution (`720`, `1080`, etc.). |
| **Threads** | `1`–`16` | Multi-connection count for `aria2c` acceleration (default: `5`). |

---

## 📁 Project Structure

```text
YT-Downloader/
├── Downloads/               # Auto-created folder where downloads are stored
│   └── <Playlist Name>/     # Subfolders automatically created for playlists
├── .downloaded_files.txt    # Download log archive preventing duplicate files
├── .gitignore               # Ignores venv, logs, and downloads
├── requirements.txt         # Core dependencies (yt-dlp)
├── yt_downloader.py         # Main interactive CLI downloader
├── LICENSE                  # MIT License
└── README.md                # Documentation
```

---

## 🛠️ Keeping Up-to-Date

YouTube frequently updates its internal player algorithms. If downloads ever slow down or fail, simply update `yt-dlp`:

```bash
pip install --upgrade yt-dlp
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

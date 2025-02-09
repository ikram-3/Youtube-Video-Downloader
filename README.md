# YouTube Video Downloader

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo Stars](https://img.shields.io/github/stars/ikram-3/Youtube-Video-Downloader?style=social)

A Python script to download YouTube videos in Full HD (1080p) with sound. This tool displays download progress, calculates the time taken, and automatically merges video and audio streams for high-quality downloads.

---

## Features
- **Full HD Download**: Downloads YouTube videos in 1080p resolution.
- **Audio Support**: Ensures the downloaded video includes both video and audio.
- **Progress Tracking**: Displays a progress bar during the download.
- **Time Calculation**: Shows the total time taken to download the video.
- **Automatic Merging**: Uses `ffmpeg` to merge video and audio streams for 1080p videos.

---

## Prerequisites

Before using this script, ensure you have the following installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **pytube**: Install using `pip install pytube`.
3. **tqdm**: Install using `pip install tqdm`.
4. **ffmpeg**: Required for merging video and audio streams. Download and install from [ffmpeg.org](https://ffmpeg.org/).

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ikram-3/Youtube-Video-Downloader.git
   cd Youtube-Video-Downloader
   ```

2. Run the script:
   ```bash
   python download_video.py
   ```

3. Enter the YouTube video URL when prompted.

---

## Example

```bash
Enter the video URL: https://www.youtube.com/watch?v=example
Title: Example Video
Duration: 300 seconds
Resolution: 1080p
Downloading...
[========================================] 100%
Time taken: 45.23 seconds
```

---

## Code Structure

- `download_video.py`: The main script to download YouTube videos.
- `README.md`: This file, containing instructions and details about the project.

---

## Dependencies

- `pytube`: For interacting with YouTube and downloading videos.
- `tqdm`: For displaying a progress bar.
- `ffmpeg`: For merging video and audio streams.

---

## Contributing

Contributions are welcome! If you find any issues or want to improve the script, feel free to:
1. Open an issue.
2. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

If you find this project useful, please give it a ⭐ on [GitHub](https://github.com/ikram-3/Youtube-Video-Downloader)!

# m4a-to-mp4

Convert `.m4a` audio files into `.mp4` videos using a static cover image (PNG/JPG) via `ffmpeg`.

This tool is ideal for podcasts, audiobooks, or spoken-word content that must be uploaded to platforms requiring video input.

## Features
- Converts M4A audio to MP4 video with a static image
- Audio passthrough (`-c:a copy`) for zero quality loss
- Input validation before conversion
- Windows-safe paths
- No Python dependencies

## Requirements
- Python 3.8+
- `ffmpeg` installed and available on PATH

Verify installation:
```bash
ffmpeg -version
```

## Usage

```
ROOT_DIR = r"C:\Users\user\Downloads"

m4a_file = "my_audio_file"
image = "cover_img.png"
```

## License
MIT License. See LICENSE.md for details.

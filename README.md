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

```python
import subprocess
import os

FFMPEG_PATH = "ffmpeg"

def validate_inputs(m4a_path: str, image_path: str):
    if not os.path.isfile(m4a_path):
        raise FileNotFoundError(f"M4A file not found: {m4a_path}")
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    if not m4a_path.lower().endswith(".m4a"):
        raise ValueError("Audio file must be .m4a")
    if not image_path.lower().endswith((".png", ".jpg", ".jpeg")):
        raise ValueError("Image must be PNG or JPG")

def m4a_to_mp4_with_image(input_m4a, image_path, output_mp4):
    validate_inputs(input_m4a, image_path)
    subprocess.run([
        FFMPEG_PATH,
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", input_m4a,
        "-c:a", "copy",
        "-c:v", "libx264",
        "-shortest",
        "-pix_fmt", "yuv420p",
        output_mp4
    ], check=True)
```

## License
MIT License. See LICENSE.md for details.

import subprocess
import os

FFMPEG_PATH = "ffmpeg"  # or full path to ffmpeg.exe

def check_ffmpeg():
    try:
        subprocess.run(
            [FFMPEG_PATH, "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    except Exception:
        raise RuntimeError("ffmpeg not found. Ensure it is installed and on PATH.")

check_ffmpeg()

def validate_inputs(m4a_path: str, image_path: str):
    """
    Validate required input files before running ffmpeg.
    Raises FileNotFoundError or ValueError with clear messages.
    """
    if not os.path.isfile(m4a_path):
        raise FileNotFoundError(f"M4A file not found: {m4a_path}")

    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    if not m4a_path.lower().endswith(".m4a"):
        raise ValueError(f"Invalid audio file type (expected .m4a): {m4a_path}")

    if not image_path.lower().endswith((".png", ".jpg", ".jpeg")):
        raise ValueError(
            f"Invalid image type (expected PNG/JPG): {image_path}"
        )
    
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

# -------------------
# Usage
# -------------------
ROOT_DIR = r"C:\Users\user\Downloads"

m4a_file = "my_audio_file"
image = "cover_img.png"

m4a_to_mp4_with_image(
    os.path.join(ROOT_DIR, m4a_file + ".m4a"),
    os.path.join(ROOT_DIR, image),
    os.path.join(ROOT_DIR, m4a_file + ".mp4"),
)
print("Conversion completed.")
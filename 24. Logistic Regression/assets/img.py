from pathlib import Path
from PIL import Image

TARGET_SIZE = (1376, 768)          # width × height
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}

def process_images(folder: str | Path = "."):
    folder = Path(folder)
    not_matching = []

    for img_path in sorted(folder.iterdir()):
        if img_path.suffix.lower() not in IMAGE_EXTS:
            continue

        with Image.open(img_path) as im:
            if im.size == TARGET_SIZE:
                print(f"✓  {img_path.name}  already {TARGET_SIZE}")
                continue

            not_matching.append((img_path.name, im.size))
            print(f"✗  {img_path.name}  is {im.size}  →  resizing to {TARGET_SIZE}")

            # High-quality resize (Lanczos)
            resized = im.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

            # Keep original format & quality
            save_kwargs = {}
            if img_path.suffix.lower() in {".jpg", ".jpeg"}:
                save_kwargs = {"quality": 95, "subsampling": 0, "optimize": True}

            resized.save(img_path, **save_kwargs)   # overwrites original

    print("\n" + "=" * 50)
    if not_matching:
        print("Images that were resized:")
        for name, size in not_matching:
            print(f"  • {name}  ({size[0]}×{size[1]})")
    else:
        print("All images already have the correct size.")

if __name__ == "__main__":
    # Run on the current folder (or change the path)
    process_images(".")
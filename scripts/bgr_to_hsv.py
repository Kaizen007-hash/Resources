"""Convert an image loaded by OpenCV from BGR to HSV and save it losslessly."""

from pathlib import Path

import cv2


ROOT = Path(__file__).resolve().parents[1]
INPUT_IMAGE = ROOT / "assets" / "pp.jpg"
OUTPUT_IMAGE = ROOT / "output" / "pp_hsv.png"


def main() -> None:
    image = cv2.imread(str(INPUT_IMAGE), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Could not read input image: {INPUT_IMAGE}")

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(OUTPUT_IMAGE), hsv_image):
        raise OSError(f"Could not write output image: {OUTPUT_IMAGE}")

    print(f"Shape: {hsv_image.shape}; dtype: {hsv_image.dtype}")
    print(f"Saved HSV pixels to {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()

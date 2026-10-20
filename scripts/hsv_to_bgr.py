"""Convert a losslessly stored OpenCV HSV image back to BGR for display."""

from pathlib import Path

import cv2


ROOT = Path(__file__).resolve().parents[1]
INPUT_IMAGE = ROOT / "output" / "pp_hsv.png"
OUTPUT_IMAGE = ROOT / "output" / "pp_roundtrip.png"


def main() -> None:
    hsv_image = cv2.imread(str(INPUT_IMAGE), cv2.IMREAD_COLOR)
    if hsv_image is None:
        raise FileNotFoundError(
            f"Could not read {INPUT_IMAGE}. Run bgr_to_hsv.py first."
        )

    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    OUTPUT_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(OUTPUT_IMAGE), bgr_image):
        raise OSError(f"Could not write output image: {OUTPUT_IMAGE}")

    print(f"Saved BGR image to {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()

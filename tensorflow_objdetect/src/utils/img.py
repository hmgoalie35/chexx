from pathlib import Path

import cv2 as cv


def resize(img_dir: Path):
    for img_path in img_dir.iterdir():
        if img_path.suffix != '.jpg':
            continue

        print('Processing...')
        img = cv.imread(str(img_path))
        h, w, _ = img.shape
        # Take a 4K img and resize to 1080p
        if h == 2160 and w == 3840:
            new_h = int(h * .5)
            new_w = int(w * .5)
            resized_img = cv.resize(img, (new_w, new_h))
            cv.imwrite(str(img_path), resized_img)

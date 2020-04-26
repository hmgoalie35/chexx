import argparse
from pathlib import Path

from common_objdetect.utils.video import Video2Img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_src')
    parser.add_argument('label')
    parser.add_argument('output_dir', type=Path)
    parser.add_argument('max_images', type=int)
    parser.add_argument('frequency', type=int)
    parser.add_argument('offset', type=int)

    args = parser.parse_args()

    input_src = args.input_src
    try:
        input_src = int(input_src)
    except ValueError:
        pass

    Video2Img(
        input_file=input_src,
        label=args.label,
        output_dir=args.output_dir,
        max_images=args.max_images,
        frequency=args.frequency,
        offset=args.offset
    ).run()


if __name__ == '__main__':
    main()

import argparse
from pathlib import Path

from common_objdetect.utils.video import Video2Img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_src')
    parser.add_argument('label')
    parser.add_argument('output_dir')
    parser.add_argument('max_images')
    parser.add_argument('frequency')
    parser.add_argument('offset')
    args = parser.parse_args()

    input_src = args.input_src
    try:
        input_src = int(input_src)
    except ValueError:
        pass

    Video2Img(
        input_file=input_src,
        label=args.label,
        output_dir=Path(args.output_dir),
        max_images=int(args.max_images),
        frequency=int(args.frequency),
        offset=int(args.offset)
    ).run()


if __name__ == '__main__':
    main()

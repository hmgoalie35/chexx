import argparse

from common_objdetect.utils.video import Video2Img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_src')
    parser.add_argument('output_dir')
    parser.add_argument('label')
    args = parser.parse_args()

    Video2Img(
        input_file=args.input_src,
        label=args.label,
        output_dir=args.output_dir,
        max_images=500,
        frequency=60,
        offset=0
    ).run()


if __name__ == '__main__':
    main()

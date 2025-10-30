import argparse
from pprint import pprint

from settings import SETTINGS
from modules import Pohon

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--images_only", action='store_true', help='Only imports images')
    args = parser.parse_args()

    pprint(SETTINGS)
    pohon = Pohon(SETTINGS)

    if args.images_only:
        pohon.only_images()
    else:
        pohon.images_with_coordinates()
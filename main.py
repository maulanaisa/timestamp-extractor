import argparse
from pprint import pprint

from settings import SETTINGS
from modules import Pohon

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    pprint(SETTINGS)
    pohon = Pohon(SETTINGS)

    pohon.images_with_coordinates()
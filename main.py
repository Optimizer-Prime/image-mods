#! /usr/bin/env python
# Program to apply the specified modification to an input image.
# The names of each option are fairly self-explanatory in what they do.
# Check the 'previews' folder to see what each may look like.
# Images will save to the directory program is run from.
# Processed images will be saved with format 'originalfilename_filter.png'
# Large images may take some time.

import argparse
import mods


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--negative', dest='negative', action='store_const', const=True, help='Test')
    parser.add_argument('-nr', '--nored', dest='nored', action='store_const', const=True, help='Test2')
    parser.add_argument('-ore', '--onlyred', dest='onlyred', action='store_const', const=True)
    parser.add_argument('-ng', '--nogreen', dest='nogreen', action='store_const', const=True)
    parser.add_argument('-og', '--onlygreen', dest='onlygreen', action='store_const', const=True)
    parser.add_argument('-nb', '--noblue', dest='noblue', action='store_const', const=True)
    parser.add_argument('-ob', '--onlyblue', dest='onlyblue', action='store_const', const=True)
    parser.add_argument('-g', '--grayscale', dest='grayscale', action='store_const', const=True)
    parser.add_argument('-bw', '--blackwhite', dest='blackwhite', action='store_const', const=True)
    parser.add_argument('-s', '--sepia', dest='sepia', action='store_const', const=True)
    parser.add_argument('-db', '--deblock', dest='deblock', action='store_const', const=True)
    parser.add_argument('-dn', '--denoise', dest='denoise', action='store_const', const=True)
    parser.add_argument('-rgb', '--rgbtint', dest='rgbtint', action='store_const', const=True)
    parser.add_argument('-bow', '--rainbow', dest='rainbow', action='store_const', const=True)
    parser.add_argument('-b', '--brighten', dest='brighten', action='store_const', const=True)
    parser.add_argument('-df', '--deepfry', dest='deepfry', action='store_const', const=True)

    args = parser.parse_args()
    if args.negative:
        mods.negative_image()
    elif args.nored:
        mods.no_red()
    elif args.onlyred:
        mods.only_red()
    elif args.nogreen:
        mods.no_green()
    elif args.onlygreen:
        mods.only_green()
    elif args.noblue:
        mods.no_blue()
    elif args.onlyblue:
        mods.only_blue()
    elif args.grayscale:
        mods.grayscale()
    elif args.blackwhite:
        mods.black_white()
    elif args.sepia:
        mods.sepia()
    elif args.deblock:
        mods.deblock()
    elif args.denoise:
        mods.denoise()
    elif args.rgbtint:
        mods.rgb_tint()
    elif args.rainbow:
        mods.rainbow()
    elif args.brighten:
        mods.brighten()
    elif args.deepfry:
        mods.deepfry()


if __name__ == '__main__':
    main()


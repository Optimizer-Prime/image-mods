import cImage as image
from statistics import median
from random import randrange
import os


def get_image():
    """Returns image to be modified."""
    return input("Enter path to image without quotes e.g. '/home/username/Pictures/image.jpg': ")


def root_fname(path):
    """Returns the filename without the extension."""
    fname = os.path.splitext(os.path.basename(path))
    return fname[0]


def negative_image():
    """Returns negative version of input image."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 255 - p.getGreen()
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_negative".format(root_fname(path)), 'png')
    win.exitonclick()


def no_red():
    """Returns input image with no red."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 0
            newgreen = 255 - p.getGreen()
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_no_red".format(root_fname(path)), 'png')
    win.exitonclick()


def only_red():
    """Returns input image with only red."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen, newblue = 0, 0

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_only_red".format(root_fname(path)), 'png')
    win.exitonclick()


def no_green():
    """Returns input image with no green."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 0
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_no_green".format(root_fname(path)), 'png')
    win.exitonclick()


def only_green():
    """Returns input image with only green."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred, newblue = 0, 0
            newgreen = 255 - p.getGreen()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_only_green".format(root_fname(path)), 'png')
    win.exitonclick()


def no_blue():
    """Returns input image with no blue."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 255 - p.getGreen()
            newblue = 0

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_no_blue".format(root_fname(path)), 'png')
    win.exitonclick()


def only_blue():
    """Returns input image with only blue."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred, newgreen = 0, 0
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_only_blue".format(root_fname(path)), 'png')
    win.exitonclick()


def grayscale():
    """Returns input image as grayscale."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            avg = int((p.getRed() + p.getGreen() + p.getBlue()) / 3)

            newred, newgreen, newblue = avg, avg, avg

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_grayscale".format(root_fname(path)), 'png')
    win.exitonclick()


def black_white():
    """Returns input image as black and white (literally just black and white)."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)
            avg = int((p.getRed() + p.getGreen() + p.getBlue()) / 3)

            if avg >= 127:
                newred, newgreen, newblue = 255, 255, 255
                newpixel = image.Pixel(newred, newgreen, newblue)
                img.setPixel(col, row, newpixel)
            elif avg < 127:
                newred, newgreen, newblue = 0, 0, 0
                newpixel = image.Pixel(newred, newgreen, newblue)
                img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_black_white".format(root_fname(path)), 'png')
    win.exitonclick()


def sepia():
    """Returns input image with sepia tone."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = int((p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189))
            newgreen = int((p.getRed() * 0.349 + p.getGreen() * 0.689 + p.getBlue() * 0.168))
            newblue = int((p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131))

            if newred > 255:
                newred = 255
            else:
                newred = newred

            if newgreen > 255:
                newgreen = 255
            else:
                newgreen = newgreen

            if newblue > 255:
                newblue = 255
            else:
                newblue = newblue

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_sepia".format(root_fname(path)), 'png')
    win.exitonclick()


def deblock():
    """Returns input image with blocking reduced."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(1, img.getHeight() - 1):
        for col in range(1, img.getWidth() - 1):
            p1 = img.getPixel(col - 1, row)
            p2 = img.getPixel(col + 1, row)
            p3 = img.getPixel(col, row + 1)
            p4 = img.getPixel(col, row - 1)
            p5 = img.getPixel(col + 1, row - 1)
            p6 = img.getPixel(col - 1, row - 1)
            p7 = img.getPixel(col + 1, row + 1)
            p8 = img.getPixel(col - 1, row + 1)

            newred = int((p1.getRed() + p2.getRed() + p3.getRed() + p4.getRed() +
                          p5.getRed() + p6.getRed() + p7.getRed() + p8.getRed()) / 8)
            newgreen = int((p1.getGreen() + p2.getGreen() + p3.getGreen() + p4.getGreen() +
                            p5.getGreen() + p6.getGreen() + p7.getGreen() + p8.getGreen()) / 8)
            newblue = int((p1.getBlue() + p2.getBlue() + p3.getBlue() + p4.getBlue() +
                           p5.getBlue() + p6.getBlue() + p7.getBlue() + p8.getBlue()) / 8)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_deblock".format(root_fname(path)), 'png')
    win.exitonclick()


def denoise():
    """Returns input image with noise reduced."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(1, img.getHeight() - 1):
        for col in range(1, img.getWidth() - 1):
            p1 = img.getPixel(col - 1, row)
            p2 = img.getPixel(col + 1, row)
            p3 = img.getPixel(col, row + 1)
            p4 = img.getPixel(col, row - 1)
            p5 = img.getPixel(col + 1, row - 1)
            p6 = img.getPixel(col - 1, row - 1)
            p7 = img.getPixel(col + 1, row + 1)
            p8 = img.getPixel(col - 1, row + 1)

            newred = int(median([int(p1.getRed()), int(p2.getRed()), int(p3.getRed()), int(p4.getRed()),
                                 int(p5.getRed()), int(p6.getRed()), int(p7.getRed()), int(p8.getRed())]))
            newgreen = int(median([int(p1.getGreen()), int(p2.getGreen()), int(p3.getGreen()), int(p4.getGreen()),
                                   int(p5.getGreen()), int(p6.getGreen()), int(p7.getGreen()), int(p8.getGreen())]))
            newblue = int(median([int(p1.getBlue()), int(p2.getBlue()), int(p3.getBlue()), int(p4.getBlue()),
                                  int(p5.getBlue()), int(p6.getBlue()), int(p7.getBlue()), int(p8.getBlue())]))

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_denoise".format(root_fname(path)), 'png')
    win.exitonclick()


def rgb_tint():
    """Returns input image with RGB tint, one for each third of image."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    onethird = int(img.getHeight() * 0.33)
    twothird = int(img.getHeight() * 0.66)

    for col in range(img.getWidth()):
        for row in range(1, onethird):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen, newblue = 0, 0

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(onethird, twothird):
            p = img.getPixel(col, row)

            newred, newblue = 0, 0
            newgreen = 255 - p.getGreen()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(twothird, img.getHeight()):
            p = img.getPixel(col, row)

            newred, newgreen = 0, 0
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_rgb_tint".format(root_fname(path)), 'png')
    win.exitonclick()


def rainbow():
    """Returns input image with rainbow filter."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    onesixth = int(img.getHeight() * 0.143)
    twosixth = int(img.getHeight() * 0.286)
    threesixth = int(img.getHeight() * 0.429)
    foursixth = int(img.getHeight() * 0.572)
    fivesixth = int(img.getHeight() * 0.715)
    sixsixth = int(img.getHeight() * 0.858)

    for col in range(img.getWidth()):
        for row in range(1, onesixth):
            # Red
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 1.0)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 0.4)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 0.4)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(onesixth, twosixth):
            # Orange
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 1.0)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 0.75)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 0.35)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(twosixth, threesixth):
            # Yellow
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 1.0)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 1.0)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 0.4)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(threesixth, foursixth):
            # Green
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 0.35)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 1.0)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 0.35)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(foursixth, fivesixth):
            # Blue
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 0.4)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 0.69)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 1.0)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(fivesixth, sixsixth):
            # Indigo
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 0.4)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 0.4)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 1.0)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)
        for row in range(sixsixth, img.getHeight()):
            # Violet
            p = img.getPixel(col, row)

            newred = int(p.getRed() + (255 - p.getRed()) * 0.69)
            newgreen = int(p.getGreen() + (255 - p.getGreen()) * 0.4)
            newblue = int(p.getBlue() + (255 - p.getBlue()) * 1.0)

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_rainbow".format(root_fname(path)), 'png')
    win.exitonclick()


def brighten():
    """Returns input image with brightness increased by specified factor."""
    path = get_image()
    img = image.Image(path)
    increase = abs(int(input("Please enter an integer value to increase brightness by.\n"
                             "Suggested 50 - 150: ")))
    win = image.ImageWin(img.getWidth(), img.getHeight())

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = p.getRed() + abs(increase)
            newgreen = p.getGreen() + abs(increase)
            newblue = p.getBlue() + abs(increase)

            if newred > 255:
                newred = 255
            else:
                newred = newred

            if newgreen > 255:
                newgreen = 255
            else:
                newgreen = newgreen

            if newblue > 255:
                newblue = 255
            else:
                newblue = newblue

            newpixel = image.Pixel(newred, newgreen, newblue)
            img.setPixel(col, row, newpixel)

    img.draw(win)
    img.save("{0}_brighten".format(root_fname(path)), 'png')
    win.exitonclick()


def deepfry():
    """Returns a 'deep-fried' version of the input image."""
    path = get_image()
    img = image.Image(path)
    win = image.ImageWin(img.getWidth(), img.getHeight())

    # saturate
    for row in range(1, img.getHeight() - 1):
        for col in range(1, img.getWidth() - 1):
            p = img.getPixel(col, row)

            oldred, oldgreen, oldblue = p.getRed(), p.getGreen(), p.getBlue()

            # red
            if p.getRed() > p.getGreen() and p.getBlue():
                if p.getRed() > 150:
                    newgreen = p.getGreen() - 75
                    newblue = p.getBlue() - 75

                    if newgreen > 255:
                        newgreen = 255
                    else:
                        newgreen = newgreen

                    if newgreen < 0:
                        newgreen = 0
                    else:
                        newgreen = newgreen

                    if newblue > 255:
                        newblue = 255
                    else:
                        newblue = newblue

                    if newblue < 0:
                        newblue = 0
                    else:
                        newblue = newblue

                    newpixel = image.Pixel(oldred, newgreen, newblue)
                    img.setPixel(col, row, newpixel)
            # orange
            elif p.getRed() and p.getGreen() > p.getBlue():
                if p.getRed() > 200:
                    if p.getGreen() < 100:
                        newgreen = p.getGreen() - 30
                        newblue = p.getBlue() - 50

                        if newgreen > 255:
                            newgreen = 255
                        else:
                            newgreen = newgreen

                        if newgreen < 0:
                            newgreen = 0
                        else:
                            newgreen = newgreen

                        if newblue > 255:
                            newblue = 255
                        else:
                            newblue = newblue

                        if newblue < 0:
                            newblue = 0
                        else:
                            newblue = newblue

                        newpixel = image.Pixel(oldred, newgreen, newblue)
                        img.setPixel(col, row, newpixel)
            # yellow
            elif p.getRed() == p.getGreen():
                newblue = p.getBlue() - 75

                if newblue > 255:
                    newblue = 255
                else:
                    newblue = newblue

                if newblue < 0:
                    newblue = 0
                else:
                    newblue = newblue

                newpixel = image.Pixel(oldred, oldgreen, newblue)
                img.setPixel(col, row, newpixel)
            # green
            elif p.getGreen() > p.getRed() and p.getBlue():
                if p.getGreen() > 210:
                    newred = p.getRed() - 60
                    newblue = p.getBlue() - 60

                    if newred > 255:
                        newred = 255
                    else:
                        newred = newred

                    if newred < 0:
                        newred = 0
                    else:
                        newred = newred

                    if newblue > 255:
                        newblue = 255
                    else:
                        newblue = newblue

                    if newblue < 0:
                        newblue = 0
                    else:
                        newblue = newblue

                    newpixel = image.Pixel(newred, oldgreen, newblue)
                    img.setPixel(col, row, newpixel)
            # blue
            elif p.getBlue() > p.getRed() and p.getGreen():
                if p.getBlue() > 225:
                    if p.getGreen() > 120:
                        newred = p.getRed() - 50
                        newgreen = p.getGreen() - 23

                        if newred > 255:
                            newred = 255
                        else:
                            newred = newred

                        if newred < 0:
                            newred = 0
                        else:
                            newred = newred

                        if newgreen > 255:
                            newgreen = 255
                        else:
                            newgreen = newgreen

                        if newgreen < 0:
                            newgreen = 0
                        else:
                            newgreen = newgreen

                        newpixel = image.Pixel(newred, newgreen, oldblue)
                        img.setPixel(col, row, newpixel)
            # indigo
            elif p.getBlue() > p.getRed() and p.getGreen():
                if p.getRed() > 100:
                    newred = p.getRed() - 70
                    newgreen = p.getGreen() - 70

                    if newred > 255:
                        newred = 255
                    else:
                        newred = newred

                    if newred < 0:
                        newred = 0
                    else:
                        newred = newred

                    if newgreen > 255:
                        newgreen = 255
                    else:
                        newgreen = newgreen

                    if newgreen < 0:
                        newgreen = 0
                    else:
                        newgreen = newgreen

                    newpixel = image.Pixel(newred, newgreen, oldblue)
                    img.setPixel(col, row, newpixel)
            # violet
            elif p.getBlue() > p.getRed() and p.getGreen():
                if p.getRed() > p.getGreen():
                    newred = p.getRed() - 23
                    newgreen = p.getGreen() - 50

                    if newred > 255:
                        newred = 255
                    else:
                        newred = newred

                    if newred < 0:
                        newred = 0
                    else:
                        newred = newred

                    if newgreen > 255:
                        newgreen = 255
                    else:
                        newgreen = newgreen

                    if newgreen < 0:
                        newgreen = 0
                    else:
                        newgreen = newgreen

                    newpixel = image.Pixel(newred, newgreen, oldblue)
                    img.setPixel(col, row, newpixel)

    # blur
    count = 0
    while count < 100:
        count += 1
        pcol = randrange(2, img.getWidth() - 2)
        prow = randrange(2, img.getHeight() - 2)
        p = img.getPixel(pcol, prow)

        red, green, blue = p.getRed(), p.getGreen(), p.getBlue()

        bordered, bordergreen, borderblue = 200, 100, 100

        newpixel = image.Pixel(red, green, blue)
        borderpix = image.Pixel(bordered, bordergreen, borderblue)

        new_pair = [(pcol, prow), (pcol-1, prow), (pcol, prow+1), (pcol-1, prow+1)]
        for i, j in new_pair:
            img.setPixel(i, j, newpixel)

        border_pair = [(pcol, prow+2), (pcol-1, prow+2), (pcol-2, prow+2), (pcol-2, prow+1), (pcol-2, prow),
                       (pcol-2, prow-1), (pcol-1, prow-1), (pcol, prow-1), (pcol+1, prow-1), (pcol+1, prow),
                       (pcol+1, prow+1), (pcol+1, prow+2)]
        for i, j in border_pair:
            img.setPixel(i, j, borderpix)

    pixelate = ((img.getWidth() * img.getHeight()) * 0.35)
    # pixelate white
    count1 = 0
    while count1 < pixelate:
        count1 += 1
        pcol = randrange(1, img.getWidth() - 1)
        prow = randrange(1, img.getHeight() - 1)

        wred, wgreen, wblue = 200, 200, 200

        whitepix = image.Pixel(wred, wgreen, wblue)
        img.setPixel(pcol, prow, whitepix)

    # pixelate gray
    count2 = 0
    while count2 < pixelate:
        count2 += 1
        pcol = randrange(1, img.getWidth() - 1)
        prow = randrange(1, img.getHeight() - 1)

        gred, ggreen, gblue = 150, 150, 150

        graypix = image.Pixel(gred, ggreen, gblue)
        img.setPixel(pcol, prow, graypix)

    img.draw(win)
    img.save("{0}_deepfry".format(root_fname(path)), 'png')
    win.exitonclick()

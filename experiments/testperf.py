import imagehash
import timeit
from PIL import Image
from ssim import SSIM


def testmess():
    try:
        for i in range(1, 26):
            SSIM(Image.open("./dHash/bulktest/%3d.jpg" % i)).ssim_value(Image.open("./dHash/bulktest/%3d.jpg" % 26 - i))
    except:
        pass


def testmeah():
    try:
        for i in range(1, 26):
            imagehash.average_hash(Image.open("./dHash/bulktest/%3d.jpg" % i))
    except:
        pass


def testmeph():
    try:
        for i in range(1, 26):
            imagehash.phash(Image.open("./dHash/bulktest/%3d.jpg" % i))
    except:
        pass


def testmedh():
    try:
        for i in range(1, 26):
            imagehash.dhash(Image.open("./dHash/bulktest/%3d.jpg" % i))
    except:
        pass


def testmewh():
    try:
        for i in range(1, 26):
            imagehash.whash(Image.open("./dHash/bulktest/%3d.jpg" % i))
    except:
        pass


def testmewhdb4():
    try:
        for i in range(1, 26):
            imagehash.whash(Image.open("./dHash/bulktest/%3d.jpg" % i), mode='db4')
    except:
        pass


if __name__ == '__main__':
    print("\nSSIM (two images)\n=====")
    print(timeit.timeit("testmess()", setup="from __main__ import testmess", number=100000))
    print("\nahash\n=====")
    print(timeit.timeit("testmeah()", setup="from __main__ import testmeah", number=100000))
    print("\nphash\n=====")
    print(timeit.timeit("testmeph()", setup="from __main__ import testmeph", number=100000))
    print("\ndhash\n=====")
    print(timeit.timeit("testmedh()", setup="from __main__ import testmedh", number=100000))
    print("\nwhash-haar\n=====")
    print(timeit.timeit("testmewh()", setup="from __main__ import testmewh", number=100000))
    print("\nwhash-db4\n=====")
    print(timeit.timeit("testmewhdb4()", setup="from __main__ import testmewhdb4", number=100000))

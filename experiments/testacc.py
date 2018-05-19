import glob
import ssim
import imagehash
from PIL import Image
from tabulate import tabulate


def diff(hs, img1, img2):
    h1 = hs(img1)
    h2 = hs(img2)
    return (h1 - h2) / len(h1.hash)**2


table = []
imgs = glob.glob("*.jpg")
imgs.remove("bull_orig.jpg")
img1 = Image.open("bull_orig.jpg")
for i in range(len(imgs)):
    img2 = Image.open("%s" % imgs[i])
    ssim_r = ssim.compute_ssim(img1, img2) * 100
    ah_r = 100 - diff(imagehash.average_hash, img1, img2) * 100
    ph_r = 100 - diff(imagehash.phash, img1, img2) * 100
    dh_r = 100 - diff(imagehash.dhash, img1, img2) * 100
    wh_r = 100 - diff(imagehash.whash, img1, img2) * 100
    whdb4_r = 100 - diff(lambda img: imagehash.whash(img, mode='db4'), img1, img2) * 100
    table.append(["'%s'" % imgs[i],
                  "%lf%%" % ssim_r,
                  "%lf%%" % ah_r,
                  "%lf%%" % ph_r,
                  "%lf%%" % dh_r,
                  "%lf%%" % wh_r,
                  "%lf%%" % whdb4_r])
print(tabulate(table,
               headers=["'bull_orig.jpg' vs",
                        "PySSIM", "ahash", "phash", "dhash", "whash-haar", "whash-db4"],
               floatfmt=".1f",
               numalign="left",
               tablefmt="orgtbl"))

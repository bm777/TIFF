import matplotlib.pyplot as plt
import numpy as np
import skimage.io as skio

print("[INFOS] :> Reading tiff file")
img = skio.imread("file.tif", plugin="tifffile")
skio.imshow(img)
print("[INFOS] :> Saving on disk tiff file as 'file.png'")
#plt.show() if you to show it, uncomment this line and comment next next line
plt.savefig("file.png")

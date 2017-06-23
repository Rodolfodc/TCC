import numpy, os, array
from scipy import misc  # same as import scipy.misc

def read_image(filename, img_x_size=3000, img_y_size=1500):
    f = open(filename,'rb')
    ln = os.path.getsize(filename) # length of file in bytes
    width = 256
    rem = ln%width
    a = array.array("B") # uint8 array
    a.fromfile(f,ln-rem)
    f.close()
    g = numpy.reshape(a,(len(a)//width,width))
    g = numpy.uint8(g)
    g = numpy.resize(g, (img_x_size, img_y_size))
    return list(g)

## >>>>>>>>>>>>>>> usar em g.resize y=800 e x=200 parece interessante

def read_image_and_save(filename, path_to_store):
    img_bytes_list = read_image(filename)
    misc.imsave(path_to_store, img_bytes_list)
    return True


def ngram_features(path, c):
    with open(path,'rb') as f:
        features = f.readline().replace('"', '').strip().split(',')
        return features[(c-1)*750+1:c*750+1]
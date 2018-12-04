from PIL import ImageFile
from PIL import Image
from zipfile import ZipFile
import numpy as np
#import tensorflow as tf
import random
import json
import os
import codecs
from flask import jsonify
import mxnet as mx
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

class NDArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, mx.nd.NDArray):
            return obj.asnumpy().tolist()
        return json.JSONEncoder.default(self, obj)
    
def main():
    ziplist = []
    for file in os.listdir():
        if file.endswith(".zip") and file.startswith("train"):
            ziplist.append(file)
    print(ziplist)
    # import data
    labels = []  #list of file names without suffix
    img = []
    count = 0
    #for file in ziplist:
    #    count += 1
    with ZipFile('train_2.zip','r') as archive:
        for item in archive.namelist():
            #labels = []  #list of file names without suffix
            #img = []
            #  labels.append(os.path.splitext(entry.filename)[0])
            if (".jpg" in item or ".JPG" in item):
                with archive.open(item) as file:
                    ima = Image.open(file)
                    ima = ima.resize((928,928))
                    randnum = random.randint(227,701)
                    box = (randnum-113,randnum-113,randnum+114,randnum+114)
                    region = ima.crop(box)
                    img.append(np.asarray(region))
                    
        # save using json
        #f=open('file.json','w')
        print(img)
        img = img.tolist() # nested lists with same data, indices
        labels = labels.tolist() # nested lists with same data, indices
        file_path = "file.json" ## your path variable
        json.dump(img, codecs.open(file_path, 'w', encoding='utf-8'), cls=NDArrayEncoder, sort_keys=True, indent=4)
        #jsonify({labels: img})### this saves the array in .json format
        #f.write(json.dumps({"labels":labels,"img":img}))
        #f.close()


if __name__ == '__main__':
    main()

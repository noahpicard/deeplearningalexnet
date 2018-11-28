from PIL import Image
from zipfile import ZipFile
import numpy as np
import random

def main():

    # import data
    labels = []  #list of file names without suffix
    img = []
    
    with ZipFile('train_8.zip','r') as archive:
        for item in archive.namelist():
          #  labels.append(os.path.splitext(entry.filename)[0])
            if (".jpg" in item or ".JPG" in item):
                with archive.open(item) as file:
                    ima = Image.open(file)
                    ima = ima.resize((227,227))
                    img.append(np.asarray(img))

if __name__ == '__main__':
    main()

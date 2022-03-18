import os
from random import shuffle
from glob import glob
from _01_json_to_image import SelectProject

def main():
    
    imgs,path = SelectProject('input','PNGScribble','png')
    shuffle(imgs)
    
    file_cnt = len(imgs)
    train_cnt = round(file_cnt * 0.8)
    
    train_imgs = imgs[:train_cnt]
    val_imgs = imgs[train_cnt:]
    
    train_txt = os.path.join(path,'../train.txt')
    val_txt = os.path.join(path,'../val.txt')
    
    with open(train_txt, "w") as file1:
        for f in train_imgs:
            name, ext = os.path.splitext(f)
            file1.write(name.split('/')[-1]+"\n")
    with open(val_txt, "w") as file2:
        for f in val_imgs:
            name, ext = os.path.splitext(f)
            file2.write(name.split('/')[-1]+"\n")
    print('Complete')

if __name__ == '__main__':
    main()
    
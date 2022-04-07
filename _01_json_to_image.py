import json
from PIL import Image, ImageDraw, ImageOps
import os
from glob import glob
import random

def FindProjects(upper_path):
    P_list = glob(upper_path+'/*')
    if not P_list:
        print("There's no Folder in %s Folder" % upper_path)
        return 0
    else:
        P_list = [i.split('/')[-1] for i in P_list]
        print('\nProject list : %s\n' % P_list)
        return 1
        
def SelectProject(upper_path,lower_path,lookup):
    if FindProjects(upper_path):
        print('Please Select Project or type Full Path\n',end='>> ')
        while True:
            select = input()
            path = '%s/%s/%s' % (upper_path,select,lower_path)
            files = glob(os.path.join(path,'*.%s' % lookup))
            if files:
                break
            path = '%s/%s' % (select,lower_path)
            files = glob(os.path.join(path,'*.%s' % lookup))
            if files:
                break
            print('No %s Files found.. Please type again\n' % lookup,end='>> ')
    else:
        print('Please Input Project Path\n',end='>> ')
        while True:
            path = '%s/%s' % (input(),lower_path)
            files = glob(os.path.join(path,'*.%s' % lookup))
            if files:
                break
            print('No %s Files found.. Please type again\n' % lookup,end='>> ')
    return files,path
    
def MakeColorSet(classes):
    color_set = [[i for i in range(0,255,255//len(classes)-10)] for i in range(3)]
    label_dict = dict()
    for i in classes:
        color = []
        for idx,rgb in enumerate(color_set):
            val = random.choice(rgb)
            color.append(val)
            color_set[idx].pop(color_set[idx].index(val))
            
        label_dict[i] = color
        
    return label_dict
def main():

    jsons,path = SelectProject('input','JSONScribble','json')
    p_path = '/'.join(path.split('/')[:-1])
    ### make classes.txt - include the length and name of classes
    if os.path.isfile(os.path.join(p_path, 'classes.txt')):
        with open(os.path.join(p_path, 'classes.txt'),'r') as f:
            values = f.readlines()
        classes = [i.split()[0] for i in values[1:]]
        
    else:
        print('Please input all classes\n>>',end='')
        classes = input().split()
    print('Classes Loaded. %s\n' % classes)
    
    ### make dict for each classes
    
    label_dict = dict()
    cnt_dict = dict()
    for idx,i in enumerate(classes):
        label_dict[i] = [idx for j in range(3)]
        cnt_dict[i] = 0
    ### The folder where the picture will be saved.
    os.makedirs(os.path.join(p_path,'PNGScribble'),exist_ok=True)

    for j in jsons:
        data = json.load(open(j)) ### json load
        
        width, height = data["imageWidth"], data["imageHeight"]
        img = Image.new("RGB", (width, height), color=(255,255,255))
        draw = ImageDraw.Draw(img)
        
        ### draw scribble line on blank window
        for line in data["shapes"]:
            label = line["label"]
            points = line["points"]
            cnt_dict[label] += 1
            
            for idx, point in enumerate(points):
                if not idx:
                    first_pt = point
                else:
                    second_pt = point
                    
                    draw.line((first_pt[0], first_pt[1], second_pt[0], second_pt[1]), fill=tuple(label_dict[label]), width=5)
                    first_pt = second_pt
        ### make it Black and white.           
        gray_image = ImageOps.grayscale(img)
        gray_image.save(os.path.join(p_path,'PNGScribble/%s' % data["imagePath"].split('\\')[-1]))
    ### Print out how many times each class was drawn.   
    for key,value in cnt_dict.items():
        print('%s : %s' % (key,value),end=' ')
        
    ### Set Color     
    label_dict = MakeColorSet(classes)
    with open(os.path.join(p_path, 'classes.txt'),'w') as f:    
        f.write(str(len(classes))+'\n')
        for c,color in label_dict.items():
            f.write('%s %s\n' % (c,tuple(color)))
            
    print('\nComplete')
        
    
if __name__ == '__main__':
    main()
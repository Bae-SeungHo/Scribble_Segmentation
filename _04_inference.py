import os
import argparse
import shutil
from glob import glob

def main():
    #create parse
    parser = argparse.ArgumentParser(description="inference model")

    parser.add_argument("-model", help="model dir", required=False,default=None)
    parser.add_argument("-dataset", help="datasets dir", required=True )
    parser.add_argument("-output", help="output dir", required=False , default='output/')
    parser.add_argument("-clear", help="whether clear the output directory",action='store_true', default=False)
    parser.add_argument("-n_class", help="number of classes",required=False, default=None)
    args = parser.parse_args()
    
    if args.clear:
        if os.path.exists(args.output):
            shutil.rmtree(args.output)

    if not args.model:
        model = max(glob('model/*'))
    else:
        model = args.model

    if not args.n_class:
        try:        
            with open('temp.txt','r') as f:
                path = f.read()
            with open(os.path.join(path,'classes.txt'),'r') as f:
                n_class = f.readline()
            n_class = int(n_class.strip())
            print('n_class : %d'%n_class)
        except:
            print('Please input the number of classes\n',end='>> ')
            n_class = int(input())


            
    os.makedirs('output/',exist_ok=True)
    
    #start inference
    os.system('rloss/v-env/bin/python3.7 rloss/pytorch/pytorch-deeplab_v3_plus/inference.py --backbone resnet --checkpoint %s --image_path %s --output_directory %s --n_class %d' % (model , args.dataset , args.output,n_class))
    if os.path.isfile('temp.txt'):
        os.remove('temp.txt')
    
if __name__ == '__main__':
    main()
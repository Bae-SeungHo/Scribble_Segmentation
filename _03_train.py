import os
import argparse
from glob import glob
from datetime import datetime
import shutil

def main():
    #create parse
    parser = argparse.ArgumentParser(description="train model")

    parser.add_argument("-checkpoint", help="checkpoint file dir (also you can use 'auto')",required=False,default=None)
    parser.add_argument("-dataset", help="dataset type",choices=['custom','pascal','coco','cityscapes'] , default='custom')
    parser.add_argument("-output", help="output dir", required=False , default='model/')
    parser.add_argument("-lr", help="learning rate", required=False , default='0.007')
    parser.add_argument("-batch", help="batch size", required=False , default='4')
    parser.add_argument("-name", help="directory name", required=False , default='testing')
    parser.add_argument("-epochs", help="learning times", required=False , default='50')
    parser.add_argument("-clear", help="whether clear the output directory",action='store_true', default=False)
    args = parser.parse_args()

    #activate virtual enviroment (run bash shell)
    #subprocess.call('/bin/bash -c "$GREPDB"', shell=True, env={'GREPDB': 'dataset rloss/v-env/bin/activate'})
    if os.path.isfile('temp.txt'):
        os.remove('temp.txt')
    
    if os.path.isdir(args.dataset):
        args.dataset = 'custom'
    if args.clear:
        if os.path.exists(args.output):
            shutil.rmtree(args.output)
        if os.path.exists('run/'):    
            shutil.rmtree('run/')
    os.makedirs(args.output,exist_ok=True)
    
    #you can customize parameters
    command = 'rloss/v-env/bin/python3.7 rloss/pytorch/pytorch-deeplab_v3_plus/train_withdensecrfloss.py --backbone mobilenet --lr %s --worker 4 --epochs %s --batch-size 4 --checkname %s --dataset %s --eval-interval 5 --save-interval 5 ' % (args.lr , args.epochs , args.name, args.dataset)
    #like 'rloss/v-env/bin/python3.7 rloss/pytorch/pytorch-deeplab_v3_plus/train_withdensecrfloss.py --backbone mobilenet --lr %s --worker 4 --epochs %s --batch-size 4 --checkname %s --dataset %s --densecrfloss 2e-9 --rloss-scale 0.5 --sigma-rgb 15 --sigma-xy 100 --eval-interval 5 --save-interval 5' % (args.lr , args.epochs , args.name,args.dataset)
    
    if args.checkpoint == 'auto':
        latest_model = max(glob('model/*'))
        os.system(command+'--resume %s '% latest_model)
        
    elif args.checkpoint:
        os.system(command+'--resume %s '% args.checkpoint)
        
    else:
        os.system(command)
            
    d_name = args.dataset
    #$model_dir = max(glob('run/pascal/%s/*/' % args.name))
    #os.replace(os.path.join(model_dir,'checkpoint.pth.tar'),'model/model.pth')
    if (os.path.isfile(os.path.join('run/%s/%s' % (d_name,args.name),'model_best.pth.tar'))):
        os.replace(os.path.join('run/%s/%s' % (d_name,args.name),'model_best.pth.tar'),'model/model_%s.pth' % datetime.today().strftime("%Y%m%d%H%M"))
        print('model saved at ./model/model_%s.pth' % datetime.today().strftime("%Y%m%d%H%M"))
    else:
        latest_exp = glob('run/%s/%s/*' % (d_name,args.name))
        latest_exp = [int(i.split('_')[-1]) for i in latest_exp]
        latest_version = sorted(latest_exp,reverse=True)[0]
        latest_exp = glob('run/%s/%s/*_%d/checkpoint*.tar' % (d_name,args.name,latest_version))
        latest_version = max(latest_exp)
        try:
            os.replace(latest_version,'model/model_%s.pth' % datetime.today().strftime("%Y%m%d%H%M"))
        except:
            print("There's Error while training. check the total epochs is larger than starting epoch and try again")
            

    
if __name__ == '__main__':
    main()
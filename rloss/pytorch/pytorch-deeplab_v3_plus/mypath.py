import os,sys
sys.path.append('/home/qisens/bsh/')
from _01_json_to_image import SelectProject
class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            # folder that contains pascal/. It should have three subdirectories 
            # called "JPEGImages", "SegmentationClassAug", and "pascal_2012_scribble" 
            # containing RGB images, groundtruth, and scribbles respectively.
            return '/home/qisens/bsh/input/pascal/'  
        elif dataset == 'sbd':
            return '/path/to/datasets/benchmark_RELEASE/'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/path/to/datasets/cityscapes/'     # foler that contains leftImg8bit/
        elif dataset == 'coco':
            return '/path/to/datasets/coco/'
        elif dataset == 'custom':
            
            if os.path.isfile('./temp.txt'):
                with open('./temp.txt','r') as f:    
                    path=f.read()
            else:
                _,path = SelectProject('input','','txt')
                with open('./temp.txt','w') as f:    
                    f.write(path)
            return path
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError

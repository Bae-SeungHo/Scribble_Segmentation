from glob import glob
from tkinter import *
from _01_json_to_image import SelectProject
import os
from PIL import Image,ImageTk
#----------------------------------------------------------------------

class MainWindow():

    #----------------
    
    def __init__(self, main  ):
        
        # canvas for image
        imsize = 400
        self.canvas = Canvas(main, width=3*imsize + 100, height=imsize)
        self.canvas.grid(row=0, column=0)
        
        # images
        
        self.origin_imgs , self.inf_imgs = self.GetImages()
        self.origin_imgs , self.inf_imgs = self.Resize((imsize,imsize))
        self.alpha_imgs = self.MakeAlphaImages()
        self.my_images = [ImageTk.PhotoImage(i) for i in self.origin_imgs]
        self.my_images2 = [ImageTk.PhotoImage(i) for i in self.inf_imgs]
        self.my_images3 = [ImageTk.PhotoImage(i) for i in self.alpha_imgs]
        
        #self.my_images2 = [PhotoImage(file=i) for i in self.inf_imgs]
        self.my_image_number = 0
        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.my_images[self.my_image_number])
        self.image_on_canvas2 = self.canvas.create_image(imsize+50, 0, anchor='nw', image=self.my_images2[self.my_image_number])
        self.image_on_canvas3 = self.canvas.create_image((imsize*2)+100, 0, anchor='nw', image=self.my_images3[self.my_image_number])
        # button to change image
        self.button = Button(main, text="Next", command=self.onButton)
        self.button.grid(row=1, column=0)
        
    #----------------
    
    def GetImages(self):
        f,path = SelectProject('output','','txt')
        
        with open(f[0],'r') as f:
            origin_path = f.readline()

        inf_imgs = glob('%s/*.png' % path)
        origin_imgs = glob('%s*.jpg' % origin_path)
        if not origin_imgs:
            origin_imgs = glob('%s*.png' % origin_path)
            
        inf_imgs.sort()
        origin_imgs.sort()
        
        assert len(inf_imgs) == len(origin_imgs)
        
        return origin_imgs,inf_imgs
        
    def Resize(self,size):
        resize_origin = [Image.open(i).resize(size) for i in self.origin_imgs]
        resize_inf = [Image.open(i).resize(size) for i in self.inf_imgs]
        
        return resize_origin,resize_inf
        
    def MakeAlphaImages(self):
        alpha_imgs = []
        for idx in range(len(self.origin_imgs)):
            
            background = self.origin_imgs[idx].convert('RGBA')
            foreground = self.inf_imgs[idx].convert('RGBA')
            foreground.putalpha(125)
            alpha_imgs.append(Image.alpha_composite(background, foreground))
        return alpha_imgs
        
        
    def onButton(self):
        
        # next image
        self.my_image_number += 1

        # return to first image
        if self.my_image_number == len(self.my_images):
            self.my_image_number = 0

        # change image
        self.canvas.itemconfig(self.image_on_canvas, image=self.my_images[self.my_image_number])
        self.canvas.itemconfig(self.image_on_canvas2, image=self.my_images2[self.my_image_number])
        self.canvas.itemconfig(self.image_on_canvas3, image=self.my_images3[self.my_image_number])

#----------------------------------------------------------------------

def main():


    
    

    root = Tk()
    MainWindow(root)
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()

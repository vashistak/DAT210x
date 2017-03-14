from scipy import misc
img=misc.imread('image.jpg')
print(type(img))        #numpy.ndarray
print(img.shape,img.dtype) #(4032, 3024, 3) uint8
img=img[::2,::2]
print(img.shape,img.dtype)
#shrink the image down, for faster computing

img=(img/255.0).reshape(-1,3)    #red,green,blue
                                #reshape(-1)says to panda to
                                #convert 2D image flatten into 1Darray                       
#grayscale: luminance formula different than a
#straight average. since we preceive different color
#wavelengths as having different brightness
print(img.shape,img.dtype)
red=img[:,0]
green=img[:,1]
blue=img[:,2]

gray=(0.299*red+0.587*green+0.114*blue)

print(img.shape)
print (gray.shape)

#from scipy import misc

# Load the image up
#dset = []
#for fname in files:
# img = misc.imread(fname)
#dset.append(  (img[::2, ::2] / 255.0).reshape(-1)  )
#dset = pd.DataFrame( dset )

#do machine learning with grey
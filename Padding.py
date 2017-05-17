import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('kat.png')
print(image.shape) #three layers image
image = np.asarray(image,dtype=float)/255.0 #converting image to float type
#image = image[:,:,:3] #make sure it has three layers
plt.imshow(image)
plt.show()

# this image is BGR converting it to RGB
#print(image.dtype) # the image datatype is float64
#cvtcolor takes 8 bit or 16 bit unsigned
#image=np.asarray(image,dtype=np.uint16)
#image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#plt.imshow(image)
#plt.show()

#cv2.BORDER_REPLICATE - Last element is replicated throughout,
#  like this: aaaaaa|abcdefgh|hhhhhhh
replicate=cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image, 50,50,50,50, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(image,50,50,50,50, cv2.BORDER_CONSTANT,value=(0,0,0))

plt.subplot(231),plt.imshow(image, ),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()


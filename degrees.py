import turtle 
from PIL import Image
import numpy as np

wn=turtle.Screen()

resize_ration=0.5
step_size=1.3

im=Image.open('C:/Users/advan/OneDrive/Pictures/kashmiri_old.jpg')
w,h=im.size
im=im.resize((int(w*resize_ration),int(h*resize_ration)))
im=np.array(im)
processed_img=im.sum(axis=2)
processed_img[processed_img<processed_img.mean()-processed_img.mean()*0.1]=0
processed_img[processed_img>0]=1

image=list(processed_img)

'''
def translate(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(len(str(count)))+str(count)
            if(count==1):
                res+='1'
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(len(str(count)))+str(count)
    if(count==1):
        res+='1'+'1'
    op=res
    i=0
    count=0
    lines={}
    while(True):
        try : 
            value=op[i]
            length_rep=op[i+1]
            length=op[i+2:i+2+int(length_rep)]
            
            i=i+int(length_rep)+2
            lines['l'+str(count)]=(value,length_rep,length)
            count+=1
        except:
            break
    return lines

'''

def translate(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]
    lines={}
    j=0
    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        v=string[i]
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
                lines[j]=(v,count)
                j+=1
            if(count==1):
                res+='1'
                lines[j]=(v,1)
                j+=1
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
        lines[j]=(v,count)
        j+=1
    if(count==1):
        res+='1'
        lines[j]=(v,count)
        j+=1
    return lines


pointer=turtle.Turtle()
pointer.up()
pointer.speed('fastest')
pointer.goto(-700,370)
pointer.down()
pointer.pensize(1)


for i in range(0,len(image)):
    processed=translate(''.join( str(ele) for ele in image[i]))
    s=0

    for k,v in processed.items():
        print(v)
        value=int(v[0])
        length=int(v[1])
        s=s+step_size*length
        if(value==0):
            pointer.forward(step_size*length)
        else:
            pointer.up()
            pointer.forward(step_size*length)
            pointer.down()
  
    pointer.up()
    pointer.right(90)
    pointer.forward(1.5)
    pointer.left(90)
    pointer.backward(s)
    pointer.down()
    
'''
for line in image:
    s=0
    for ele in line:
        s=s+1
        if(ele==1):
            pointer.down()
            pointer.forward(1)
            
        else:
            pointer.up()
            pointer.forward(1)
       
    pointer.up()
    pointer.right(90)
    pointer.forward(1.5)
    pointer.left(90)
    pointer.backward(s)
    pointer.down()
            
'''

wn.mainloop()

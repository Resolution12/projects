import PIL
import matplotlib.pyplot as plt

#create new image
emoji = PIL.Image.new('RGBA', (200, 200), (0,0,0,255))

#make drawable canvas
canvas= PIL.ImageDraw.Draw(emoji)

###DRAWINGSTUFF###

#stars
check = []
for i in range(200):
    for j in range(200):
        if j%9== 0 and i%9== 0:
            i1 = i+1
            j1 = j+1
            if [i,j] not in check:
                canvas.point(((i,j), (i1, j1)), fill= "yellow")
                canvas.point(((i1,j), (i, j1)), fill= "yellow")
                check.append([i, j])
                check.append([i1, j1])



#planet
canvas.ellipse((25, 25, 175, 175), fill=(193,68,14), outline=(1, 1, 1))

#craters
crtf = (178,63,14)
crto = (163, 58, 13)
canvas.ellipse((108, 63, 160, 106), fill=crtf, outline=crto)
canvas.ellipse((50, 50, 62, 62), fill=crtf, outline=crto)
canvas.ellipse((48, 130, 107, 148), fill=crtf, outline=crto)
canvas.ellipse((130, 69, 146, 80), fill=crtf, outline=crto)


##ice caps
ico  = crto
#northpole
canvas.ellipse((73, 27, 128, 40), fill=(255,255,255), outline=ico)
#borderfix
for n1 in range(79,121+1):
    canvas.point(((n1,29), (n1, 29)), fill= "grey")
    
for n2 in range(82,119+1):
    canvas.point(((n2,28), (n2, 28)), fill= "grey")
    
for n3 in range(84,114+1):
    canvas.point(((n3,27), (n3, 27)), fill= "grey")
        
for n4 in range(92,108+1):
    canvas.point(((n4,26), (n4, 26)), fill= "grey")

for n5 in range(79,121+1):
    canvas.point(((n5,30), (n5, 30)), fill= "grey")
    
for n6 in range(82,119+1):
    canvas.point(((n6,31), (n6, 31)), fill= "grey")
    
for n7 in range(84,114+1):
    canvas.point(((n7,32), (n7, 32)), fill= "grey")
        
for n8 in range(92,108+1):
    canvas.point(((n7,33), (n7, 33)), fill= "grey")
#southpole  
canvas.ellipse((68, 159, 132, 174), fill=(255,255,255), outline=ico)
#borderfix
for s1 in range(92,108+1):
    canvas.point(((s1,174), (s1, 174)), fill= "grey")
    
for s2 in range(85,115+1):
    canvas.point(((s2,173), (s2, 173)), fill= "grey")
    
for s3 in range(82,118+1):
    canvas.point(((s3,172), (s3, 172)), fill= "grey")
    
for s4 in range(82-4,123):
    canvas.point(((s4,171), (s4, 171)), fill= "grey")

for s5 in range(92,108+1):
    canvas.point(((s5,166), (s5, 167)), fill= "grey")
    
for s6 in range(85,115+1):
    canvas.point(((s6,167), (s6, 168)), fill= "grey")
    
for s7 in range(82,118+1):
    canvas.point(((s7,168), (s7, 169)), fill= "grey")
    
for s8 in range(82-4,123):
    canvas.point(((s8,169), (s8, 170)), fill= "grey")    

for s9 in range(74,76):
    canvas.point(((s9,170), (s9, 171)), fill= "black")
            
canvas.point(((126,171), (126, 171)), fill= "black")                
canvas.ellipse((25, 25, 175, 175), outline=(1, 1, 1))


#display emoji
fig, ax = plt.subplots(1, 1)
ax.imshow(emoji)
fig.show()



import os, shutil,time
from PIL import Image


def main():
    tic = time.perf_counter()
    start_directory = os.getcwd() + "/"
    new_directory = start_directory + "modified/"
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    iconList, first_directory = initialize(start_directory, new_directory)
    addLogo(iconList, first_directory, start_directory, new_directory)
    toc = time.perf_counter()
    t =  int(round((toc - tic), 0))
    print("Total: {t} seconds\n".format(t=t))

def initialize(start_directory, finalFolder):


    iconList = []


    try:
        shutil.rmtree(finalFolder)
    except OSError as e:
        print("Error: %s : %s" % (finalFolder, e.strerror))

    try:
        os.mkdir(finalFolder)
    except OSError:
        print ("Creation of the directory failed")
    else:
        pass

    directory = os.listdir(start_directory)
    first_directory = []
    for d in range(len(directory)):
        e = directory[d]
        if "jpg" in e or "jpeg" in e or "png" in e or "gif" in e:
            if "logo" not in e:
                first_directory.append(e)
            


    for z in range(len(first_directory)):
        q = start_directory + first_directory[z]
        if "jpg" in q.lower() or "jpeg" in q or "png" in q or "gif" in q:
            iconList.append(q)
    return iconList, first_directory

def addLogo(iconList, first_directory, start_directory, finalFolder):
    for o in range(len(iconList)):
        ftic = time.perf_counter()
        #progress
        print(first_directory[o])
        print(iconList[o])
        #open image
        img = Image.open(iconList[o])
        img = img.convert('RGB')
        width, height = img.size
        
        #open logo
        logo = Image.open(os.path.join(start_directory, 'logo.png')).resize((int(.1*height), int(.1*height)))
        #make transparent
        logowidth, logoheight = logo.size
        logomap  = logo.load()
        watermark = Image.new( 'RGBA', (logowidth, logoheight), (0, 0, 0, 0))
        wmmap = watermark.load()
        for i in range(logowidth):
            for j in range(logoheight):
                pixel = logomap[i,j]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if len(pixel) == 4:
                    a = pixel[3]
                    if a == 0:
                        wmmap[i,j] = (r, g, b, a)
                    else:
                        wmmap[i,j] = (r, g, b, 96)
        
        #add logo      
        img.paste(watermark, (5, 5), mask=watermark)
        img.save(finalFolder + first_directory[o], 'PNG')
        ftoc = time.perf_counter()
        ft =  int(round(1000*(ftoc - ftic), 0))
        print("{ft} ms\n".format(ft=ft))
        
main()
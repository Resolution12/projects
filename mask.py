import os, PIL, shutil
from PIL import Image


def main():
    start_directory = os.getcwd() + "/"
    new_directory = start_directory + "modified/"
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    iconList, first_directory = initialize(start_directory, new_directory)
    sepia(iconList, first_directory, start_directory, new_directory)

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
            first_directory.append(e)
            


    for z in range(len(first_directory)):
        q = start_directory + first_directory[z]
        if "jpg" in q.lower() or "jpeg" in q or "png" in q or "gif" in q:
            iconList.append(q)
    return iconList, first_directory

def sepia(iconList, first_directory, start_directory, finalFolder):
    for o in range(len(iconList)):
        print(first_directory[o])
        print(iconList[o] + "\n")

        img = Image.open(iconList[o])
        img = img.convert('RGB')
        pixelMap = img.load() #create the pixel map
        width, height = img.size
        newIcon = Image.new( 'RGBA', (width, height), (255, 255, 255, 0))
        newPixels = newIcon.load()
        for i in range(width):
            for j in range(height):
                pixel = pixelMap[i,j]
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]
                if len(pixel) == 4:
                    alpha = pixel[3]
                tr = int((0.393 * red) + (0.769 * green) + (0.189 * blue))
                tg = int((0.349 * red) + (0.686 * green) + (0.168 * blue))
                tb = int((0.272 * red) + (0.534 * green) + (0.131 * blue))
                if(tr > 255):
                    tr = 255
                if(tg > 255):
                    tg = 255
                if(tb > 255):
                    tb = 255
                if(tr < 0):
                    tr = 0
                if(tg < 0):
                    tg = 0
                if(tb < 0):
                    tb = 0
                    
                if len(pixel) == 4:
                    newPixels[i, j] = (int(tr), int(tg), int(tb), alpha)
                else:
                    newPixels[i, j] = (int(tr), int(tg), int(tb))

        newIcon.save(finalFolder + first_directory[o], 'PNG')
main()

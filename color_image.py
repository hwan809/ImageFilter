from PIL import Image, ImageDraw
import numpy as np
from tqdm import tqdm

def getBestColor(bestcolor, colors, isadd):
    bettercolor = None
    colornum = None
    
    for color in colors:
        nownum = 0

        if isadd:
            nownum = np.abs(bestcolor[0] - color[0]) + np.abs(bestcolor[1] - color[1]) + np.abs(bestcolor[2] - color[2])
        else:    
            nownum = np.abs(bestcolor[0] - color[0]) ** 2 + np.abs(bestcolor[1] - color[1]) ** 2 + np.abs(bestcolor[2] - color[2]) ** 2

        if (colornum is None) or (colornum > nownum):
            bettercolor = color
            colornum = nownum

    
    return bettercolor

if __name__ == "__main__":

    impath = input('이미지 경로 입력 (ex: test.jpg) : ')
    canvaspath = input('RGB값 txt 파[일명] 입력 (ex: watercolor_12) : ')
    isadd = bool(int(input('평가함수 type 입력 (0 - 가우시안, 1 - 대비) : ')))

    filename = impath.split('.')[0]
    canvascolors = list() #튜플 (0, 0, 0)
    with open(canvaspath + '.txt', 'r') as f:
        for line in f.readlines():
            if line == '': continue

            sr, sg, sb = map(int, line.split())
            canvascolors.append((sr, sg, sb))

    im = Image.open(impath)
    imraw = im.load()

    for x in tqdm(range(im.size[0])):
        for y in range(im.size[1]):
            nowcolor = (imraw[x, y][0], imraw[x, y][1], imraw[x, y][2]) 
            newcolor = getBestColor(nowcolor, canvascolors, isadd)

            imraw[x, y] = newcolor

    im.save(filename + '_' + canvaspath + '.' + impath.split('.')[1])
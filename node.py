from constants import WIN
import pygame


class Node:

    def __init__(self, coords, color=(0, 255, 0), visited=False):
        self.x1 ,self.y1, self.x2 , self.y2 =  coords
        self.color = color
        self.visited = visited
        self.deleteList = []

    def setColor(self, color):
        self.color = color

    def getPos(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def draw(self, delete=0, fill=False, test=False, testCell=None):
        x1, y1, x2, y2 = self.getPos()
        topColor = (0, 0, 0)
        bottomColor = (0, 0, 0)
        leftColor = (0, 0, 0)
        rightColor = (0, 0, 0)

        if delete !=0:
            self.deleteList.append(delete)

        # Check if we want to remove the wall between corresponding cell and current cell
        for delet in self.deleteList:
            if delet == 1:
                topColor = (255, 255, 255)
            if delet == 2:
                bottomColor = (255, 255, 255)
            if delet == 3:
                leftColor = (255, 255, 255)
            if delet == 4:
                rightColor = (255, 255, 255)

        # Draw lines
        self.top = pygame.draw.line(WIN, topColor, (x1, y1), (x1+x2, y1))
        self.left = pygame.draw.line(WIN, leftColor, (x1, y1), (x1, y1+y2))
        self.bottom = pygame.draw.line(WIN, bottomColor, (x1, y1+y2), (x1+x2, y1+y2))
        self.right = pygame.draw.line(WIN, rightColor, (x1+x2, y1), (x1+x2, y1+y2))



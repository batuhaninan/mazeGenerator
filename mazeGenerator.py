#!/usr/bin/env python3
import pygame, random
from node import Node
from constants import WIDTH, HEIGHT, WH, WIN, BG

pygame.display.set_caption("Maze")


BG.fill((255,255,255))


def createNodes(nodeCount):
    # Create nodes
    nodeList = []
    for i in range(1, nodeCount + 1):
        temp = []
        for j in range(1, nodeCount + 1):
            x1 = (50 * j) - 40
            y1 = (50 * i) - 40
            x2 = 50
            y2 = 50
            coords = (x1, y1, x2, y2)

            color = (255, 255, 255)

            temp.append(Node(coords, color=color))
        nodeList.append(temp)

    return nodeList


def drawNodes(nodeList):
    # Draw all nodes
    for i in range(len(nodeList)):
        for j in range(len(nodeList[i])):
            currNode = nodeList[i][j]
            currNode.draw()

    # Right line
    pygame.draw.line(WIN, (0, 0, 0), (760, 10), (760, 760))

    # Bottom line
    pygame.draw.line(WIN, (0, 0, 0), (10, 760), (760, 760))

def getNeighbours(nodeList, currCell):
    neighbours = {}

    # Get index of the current cell
    index = getIndex(nodeList, currCell)
    y, x = index

    # Get neighbours of current cell if neighbour cell is not visited

    if y + 1 < len(nodeList):
        cell = nodeList[y+1][x]
        if not cell.visited:
            neighbours["bottom"] = cell

    if y - 1 >= 0:
        cell = nodeList[y-1][x]
        if not cell.visited:
            neighbours["top"] = cell

    if x + 1 < len(nodeList[y]):
        cell = nodeList[y][x+1]
        if not cell.visited:
            neighbours["right"] = cell

    if x - 1 >= 0:
        cell = nodeList[y][x-1]
        if not cell.visited:
            neighbours["left"] = cell


    return neighbours


def getIndex(nodeList, currCell):
    # Get the coordinates as (y, x) of current cell
    temp = (0,0)
    for i in range(len(nodeList)):
        for j in range(len(nodeList[i])):
            if nodeList[i][j] == currCell:
                temp = (i, j)
                break

    return temp


def generateMaze(nodeList, currCell, prog):

    stack = []
    # Mark the current cell as visited and push it to the stack
    currCell.visited = True
    stack.append(currCell)

    # While stack is not empty
    while stack:

        # Get a cell
        currCell = stack.pop()
        # Get neighbours of that cell
        neighbours = getNeighbours(nodeList, currCell)

        # If current cell has unvisited neighbours
        if neighbours:
            # Push the current cell back to the stack
            stack.append(currCell)

            # Get random neighbour of current cell
            k = random.choice(list(neighbours.keys()))
            v = neighbours[k]

            # Remove appropriate wall between current cell and neighbour cell

            if k == "right":
                currCell.draw(delete=4)
                v.draw(delete=3)

            if k == "left":
                currCell.draw(delete=3)
                v.draw(delete=4)

            if k == "bottom":
                currCell.draw(delete=2)
                v.draw(delete=1)

            if k == "top":
                currCell.draw(delete=1)
                v.draw(delete=2)

            # Mark neighbour cell as visited and push it back to the stack
            v.visited = True
            stack.append(v)

            # Put delay if we want to watch progress
            if prog:
                time.sleep(0.01)
                pygame.display.update()


def main():
    run = True
    WIN.blit(BG, (0,0))

    nodeCount = 15
    nodeList = createNodes(nodeCount)
    drawNodes(nodeList)
    pygame.display.update()
    generateMaze(nodeList, nodeList[0][0], prog=False)
    print("finished")

    while run:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                break

    pygame.quit()


if __name__ == '__main__':
    main()

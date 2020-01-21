# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/11 12:35
@Description : pass
"""
import random
import numpy
from matplotlib import pyplot
from matplotlib import patches


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)


class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        """ point 是否在当前象限内 """
        return self.x - self.w < point.x < self.x + self.w and self.y - self.h < point.y < self.y + self.h

    def __str__(self):
        return 'x: %s, y: %s, w: %s, h: %s' % (self.x, self.y, self.w, self.h)


class QuadTree(object):
    def __init__(self, root, capacity):
        self.root = root
        self.capacity = capacity
        self.points = []
        self.divided = False

        self.north_west = None
        self.north_east = None
        self.south_west = None
        self.south_east = None

    def insert(self, point):
        if self.root.contains(point) is False:
            return

        if len(self.points) < self.capacity:
            self.points.append(point)
        else:
            if self.divided is False:
                self.subdivide()

            self.north_west.insert(point)
            self.north_east.insert(point)
            self.south_west.insert(point)
            self.south_east.insert(point)

    def subdivide(self):
        """当前象限拆成四等份"""
        x = self.root.x
        y = self.root.y
        w = self.root.w
        h = self.root.h

        north_west_rect = Rectangle(x - w / 2, y + h / 2, h / 2, w / 2)
        north_east_rect = Rectangle(x + w / 2, y + h / 2, h / 2, w / 2)
        south_west_rect = Rectangle(x - w / 2, y - h / 2, h / 2, w / 2)
        south_east_rect = Rectangle(x + w / 2, y - h / 2, h / 2, w / 2)

        self.north_west = QuadTree(north_west_rect, self.capacity)
        self.north_east = QuadTree(north_east_rect, self.capacity)
        self.south_west = QuadTree(south_west_rect, self.capacity)
        self.south_east = QuadTree(south_east_rect, self.capacity)

        self.divided = True

    def collect_rects(self, ax):
        xy = numpy.array([self.root.x - self.root.w, self.root.y - self.root.h])
        rect = patches.Rectangle(xy, self.root.w * 2, self.root.w * 2, edgecolor='w')
        ax.add_patch(rect)

        for point in self.points:
            pyplot.plot(point.x, point.y, 'r+', label="point", markersize=4)

        if self.divided:
            self.north_west.collect_rects(ax)
            self.north_east.collect_rects(ax)
            self.south_west.collect_rects(ax)
            self.south_east.collect_rects(ax)

    def show(self):
        fig, ax = pyplot.subplots()
        self.collect_rects(ax)

        pyplot.rcParams['savefig.dpi'] = 300
        pyplot.rcParams['figure.dpi'] = 300
        pyplot.axis('equal')
        pyplot.grid(False)
        pyplot.show()

    def __str__(self):
        rtn = ''
        points_count = len(self.points)
        for index in xrange(points_count):
            if index != points_count - 1:
                rtn += 'point_%s: %s\n' % (index, self.points[index])
            else:
                rtn += 'point_%s: %s' % (index, self.points[index])
        return rtn


if __name__ == '__main__':
    width = 400
    height = 400
    root = Rectangle(200, 200, 200, 200)
    quad_tree = QuadTree(root, 4)

    for x in xrange(300):
        point = Point(random.uniform(0, width), random.uniform(0, height))
        quad_tree.insert(point)

    quad_tree.show()

import math
from enum import Enum
import os


class Parameters:

    # window sizes:
    WIDTH = 1000
    HEIGHT = 800

    DIRECTORY = os.path.join("..", "data")

    # image parameters:
    MIN_COLOR = 0
    MAX_COLOR = 235
    FINAL_SIZE = 100

    # brush size (canvas):
    RADIUS = 15

    # brush size in percentages (imageDraw):
    RADIUS_PERCENTAGE = 5

    # min distance between points to perform interpolation
    MIN_LIMIT = math.sqrt(2)


class State(Enum):

    SETTING_CLASS_NAME = 0
    PAINING = 1

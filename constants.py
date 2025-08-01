from enum import Enum


class PackageStack(Enum):
    STANDARD = 1
    SPECIAL = 2
    REJECTED = 3
    INVALID = 4


MAX_WIDTH = 150
MAX_LENGTH = 150
MAX_HEIGHT = 150
MAX_VOLUME = 1000000
MAX_MASS = 20

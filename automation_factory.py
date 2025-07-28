from constants import (
    MAX_HEIGHT,
    MAX_LENGTH,
    MAX_MASS,
    MAX_VOLUME,
    MAX_WIDTH,
    PackageStack,
)


def package_sort(width: int, height: int, length: int, mass: int) -> str:
    volume = width * height * length
    heavy = mass >= MAX_MASS
    bulky = (
        volume >= MAX_VOLUME
        or width >= MAX_WIDTH
        or height >= MAX_HEIGHT
        or length >= MAX_LENGTH
    )

    if bulky and heavy:
        return PackageStack.REJECTED.name
    elif bulky or heavy:
        return PackageStack.SPECIAL.name
    else:
        return PackageStack.STANDARD.name

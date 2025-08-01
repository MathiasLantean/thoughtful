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


def safe_package_sort(width: int, height: int, length: int, mass: int) -> str:
    try:
        package_width = int(width)
        package_height = int(height)
        package_length = int(length)
        package_mass = int(mass)

        if (
            package_mass > 0
            and package_length > 0
            and package_height > 0
            and package_width > 0
        ):
            return package_sort(
                package_width, package_height, package_length, package_mass
            )
        return PackageStack.INVALID.name

    except ValueError:
        return PackageStack.INVALID.name

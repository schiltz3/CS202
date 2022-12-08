def print_coords_of_cube(cube_side_len: int, resolution: float = 1):
    """Generate all coordinates contained in a cube with side the size of cube_side_len

    Args:
        cube_side_len (int): size of the cube [1 : cube_side_len +1]
        resolution (float, optional): resolution to print coords at. Defaults to 1.
    """
    cube_side_len += 1
    l = 0
    print(f"(x\ty\tz)")
    while l <= cube_side_len:
        w = 0
        while w <= cube_side_len:
            h = 0
            while h <= cube_side_len:
                print(f"({l}\t{w}\t{h})")
                h += resolution
            w += resolution
        l += resolution


if __name__ == "__main__":
    print_coords_of_cube(4, 0.75)

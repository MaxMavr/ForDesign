from collections import deque
from utils import svg
from utils.color import Color
from utils.img import input_img
from utils.system import file


def get_neighbors(x, y, width, height):
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= nx < width and 0 <= ny < height:
            yield nx, ny


def find_connected_components(img):
    width, height = img.size
    pixels = img.load()
    visited = [[False] * width for _ in range(height)]
    components = []

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:
                color = pixels[x, y]
                queue = deque([(x, y)])
                visited[y][x] = True
                comp_pixels = []
                while queue:
                    cx, cy = queue.popleft()
                    comp_pixels.append((cx, cy))
                    for nx, ny in get_neighbors(cx, cy, width, height):
                        if not visited[ny][nx] and pixels[nx, ny] == color:
                            visited[ny][nx] = True
                            queue.append((nx, ny))
                components.append({'color': Color.from_rgb(color), 'pixels': comp_pixels})
    return components


def trace_outline(pixels_set):
    outline_edges = set()

    for (x, y) in pixels_set:
        if (x - 1, y) not in pixels_set:
            outline_edges.add(((x, y), (x, y + 1)))
        if (x + 1, y) not in pixels_set:
            outline_edges.add(((x + 1, y), (x + 1, y + 1)))
        if (x, y - 1) not in pixels_set:
            outline_edges.add(((x, y), (x + 1, y)))
        if (x, y + 1) not in pixels_set:
            outline_edges.add(((x, y + 1), (x + 1, y + 1)))

    paths = []
    while outline_edges:
        start = edge = outline_edges.pop()
        path = [edge[0], edge[1]]

        while path[-1] != start[0]:
            next_edge = None
            found_edge = None

            for e in list(outline_edges):
                if e[0] == path[-1]:
                    next_edge = e
                    found_edge = e
                    break
                elif e[1] == path[-1]:
                    next_edge = (e[1], e[0])
                    found_edge = e
                    break

            if not next_edge:
                break

            outline_edges.remove(found_edge)
            path.append(next_edge[1])

        if len(path) > 1:
            d = f"M {path[0][0]} {path[0][1]} " + " ".join(f"L {x} {y}" for x, y in path[1:]) + " Z"
            paths.append(d)

    if paths:
        return paths[0]
    else:
        return ""


def colorful(filename: str):
    img = input_img(filename)
    name = file.split_filename(filename, 'n')

    components = find_connected_components(img)

    styles = []
    content = []
    styles_dict = {}

    for idx, comp in enumerate(components, 1):
        color = comp['color'].hex
        pixels_set = set(comp['pixels'])
        if color not in styles_dict:
            styles_dict[color] = idx
            styles.append(f'.st{idx}{{fill:{color};shape-rendering:crispEdges;}}')
        cls = f'st{styles_dict[color]}'
        d = trace_outline(pixels_set)
        content.append(f'<path class="{cls}" d="{d}"/>')

    svg.make(
        width=img.width,
        height=img.height,
        styles=styles,
        content=content,
        attributes={"shape-rendering": "crispEdges"},
        filename=name
    )


if __name__ == '__main__':
    colorful('brick.png')

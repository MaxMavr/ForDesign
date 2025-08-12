import random
from typing import Union
import numpy as np

BAYER_8x8 = np.array([
    [0, 48, 12, 60, 3, 51, 15, 63],
    [32, 16, 44, 28, 35, 19, 47, 31],
    [8, 56, 4, 52, 11, 59, 7, 55],
    [40, 24, 36, 20, 43, 27, 39, 23],
    [2, 50, 14, 62, 1, 49, 13, 61],
    [34, 18, 46, 30, 33, 17, 45, 29],
    [10, 58, 6, 54, 9, 57, 5, 53],
    [42, 26, 38, 22, 41, 25, 37, 21],
]) / 64.0

BAYER_4x4 = np.array([
    [0, 8, 2, 10],
    [12, 4, 14, 6],
    [3, 11, 1, 9],
    [15, 7, 13, 5],
]) / 16.0

CLUSTER_DOT_4x4 = np.array([
    [8, 9, 4, 5],
    [10, 11, 6, 7],
    [3, 0, 1, 2],
    [15, 12, 13, 14],
]) / 16.0

BLUE_NOISE_8x8 = np.array([
    [0.73, 0.41, 0.83, 0.22, 0.65, 0.37, 0.90, 0.11],
    [0.55, 0.97, 0.18, 0.79, 0.44, 0.08, 0.68, 0.29],
    [0.86, 0.25, 0.60, 0.32, 0.75, 0.14, 0.50, 0.05],
    [0.35, 0.70, 0.02, 0.93, 0.27, 0.58, 0.16, 0.80],
    [0.61, 0.39, 0.88, 0.19, 0.46, 0.99, 0.07, 0.72],
    [0.12, 0.66, 0.30, 0.53, 0.09, 0.84, 0.21, 0.95],
    [0.49, 0.26, 0.77, 0.34, 0.62, 0.04, 0.91, 0.17],
    [0.82, 0.13, 0.43, 0.56, 0.24, 0.69, 0.31, 0.06],
])


def pattern_dither_8x8(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = BAYER_8x8[y % 8][x % 8]
    return brightness > threshold


def pattern_dither_4x4(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = BAYER_4x4[y % 4][x % 4]
    return brightness > threshold


def noise_dither(brightness: Union[int, float]) -> bool:
    threshold = random.random()
    return brightness > threshold


def white_noise_dither(brightness: Union[int, float]) -> bool:
    jitter = (random.random() - 0.5) * 0.3  # ±15%
    threshold = min(max(brightness + jitter, 0), 1)
    return brightness > threshold


def threshold_dither(brightness: Union[int, float], threshold: Union[int, float]) -> bool:
    return brightness > threshold


def clustered_dot_dither(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = CLUSTER_DOT_4x4[y % 4][x % 4]
    return brightness > threshold


def blue_noise_dither(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = BLUE_NOISE_8x8[y % 8][x % 8]
    return brightness > threshold

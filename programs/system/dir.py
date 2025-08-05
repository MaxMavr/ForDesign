from PIL import Image
from os import listdir, makedirs
from os.path import isdir, getsize, exists
from typing import Union
from programs.prints.color_output import g, y, bold
from programs.system.file import split_name_format


def make_dir(dir_path):
    if not exists(dir_path):
        makedirs(dir_path)
        return True
    return False


def size_file(file):
    return getsize(file)


def size_photo(photo):
    with Image.open(photo) as img:
        return img.size


def merge_path(path1: str, path2: str):
    return fr'{path1}\{path2}'


def searching_files_in_dir(check_path: Union[str, list, tuple],
                           search_file: Union[str, list, tuple],
                           highlight=True,
                           show_check=False,
                           notsoft=False,
                           deep=False,
                           ignore_dir: Union[str, list, tuple] = None):

    check_paths = [check_path] if isinstance(check_path, str) else check_path
    search_files = [search_file] if isinstance(search_file, str) else search_file

    if ignore_dir is not None:
        ignore_dir = [ignore_dir] if isinstance(ignore_dir, str) else ignore_dir
    else:
        ignore_dir = []

    print(y(f"""
    Ищем в {', '.join(check_paths)}
    Файлы {', '.join(search_files)}
    """))

    def check_dir(path):
        items = listdir(path)

        for item in items:
            path2item = merge_path(path, item)

            if isdir(path2item) \
                    and (item[0] != '.' or notsoft) \
                    and item not in ignore_dir \
                    and deep:

                check_dir(path2item)

            elif item in search_files:
                if highlight:
                    print(merge_path(path, g(item)))
                else:
                    print(path2item)

            elif show_check:
                print(path2item)

    for pth in check_paths:
        check_dir(pth)


def searching_in_files(check_path: Union[str, list, tuple],
                       format_file: Union[str, list, tuple],
                       search_word: Union[str, list, tuple],
                       highlight=True,
                       show_check=False,
                       show_line=True,
                       notsoft=False,
                       deep=False,
                       ignore_dir: Union[str, list, tuple] = None):

    check_paths = [check_path] if isinstance(check_path, str) else check_path
    format_files = [format_file] if isinstance(format_file, str) else format_file
    search_words = [search_word] if isinstance(search_word, str) else search_word

    if ignore_dir is not None:
        ignore_dir = [ignore_dir] if isinstance(ignore_dir, str) else ignore_dir
    else:
        ignore_dir = []

    print(y(f"""
    Ищем в {', '.join(check_paths)}
    Файлы {', '.join(format_files)}
    Слова {', '.join(search_words)}
    """))

    def check_dir(path):
        items = listdir(path)

        for item in items:
            path2item = merge_path(path, item)

            if isdir(path2item) \
                    and (item[0] != '.' or notsoft) \
                    and item not in ignore_dir \
                    and deep:

                check_dir(path2item)

            elif split_name_format(item, 'f') in format_files:
                with open(path2item, 'r', encoding='utf-8') as file:
                    file_text = file.read()

                    for sw in search_words:
                        if show_check:
                            print(path2item)

                        if sw in file_text:
                            if not show_check:
                                print(path2item)

                            if show_line:
                                lines = file_text.split('\n')
                                for i in range(len(lines)):
                                    if sw in lines[i]:
                                        if highlight:
                                            print(f'    {i + 1}: {lines[i].strip().replace(sw, bold(g(sw)))}')
                                        else:
                                            print(f'    {i + 1}: {lines[i].strip()}')

    for pth in check_paths:
        check_dir(pth)


if __name__ == "__main__":
    pass

    # path = r'L:\maxim\1 Pаботы\KF\Сайт\download-res\desktops'
    #
    # for item in listdir(path):
    #     if split_name_format(item, 'f') == 'png':
    #         if split_name_format(item, 'p') == '4K' and size_photo(merge_path(path, item)) == (3840, 2160):
    #             print(g(item), size_photo(merge_path(path, item)))
    #         elif split_name_format(item, 'p') == 'FHD' and size_photo(merge_path(path, item)) == (1920, 1080):
    #             print(g(item), size_photo(merge_path(path, item)))
    #         else:
    #             print(item, size_photo(merge_path(path, item)))

    # path = r'L:\maxim\1 Pаботы\KF\Сайт\download-res\desktops'
    #
    # for item in listdir(path):
    #
    #     nf = split_name_format(item, 'l')
    #
    #     if nf[1] == 'ai':
    #         create_zip(merge_path(path, f'{nf[0]}.zip'),
    #                    merge_path(path, f'{nf[0]}@4K.png'),
    #                    f'PNG/{nf[0]}@4K.png')
    #         create_zip(merge_path(path, f'{nf[0]}.zip'),
    #                    merge_path(path, f'{nf[0]}@FHD.png'),
    #                    f'PNG/{nf[0]}@FHD.png')

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('css', 'html',),
    #                    ('#231f20', '#fff', '#000', '#f2f3f5',),
    #                    show_check=False,
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'default'))

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('css',),
    #                    ('user-select',),
    #                    # ('--black', '#231f20', '--white', '#fff', '--gray', '#f2f3f5', '#'),
    #                    show_check=False,
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'default', 'colors.css'))

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('css',),
    #                    ('grid-template-columns',),
    #                    show_check=False,
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'default', 'colors.css'))

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('css', 'html',),
    #                    ('--poster-bg',),
    #                    show_check=False,
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'colors.css')
    #                    )

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('html',),
    #                    ("&mdash;", "—",),
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'default'))

    # searching_in_files(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                    ('svg',),
    #                    ("заглавная",),
    #                    show_line=True,
    #                    deep=True,
    #                    ignore_dir=('TEST', 'default'))

    # print(size_file(r"C:\Users\maxma\Desktop\Стикеры Пластырь.svg"))
    # print(size_file(r"C:\Users\maxma\Desktop\Стикеры-Пластырь.png"))

    # print(size_file(r"L:\maxim\1 Pаботы\KF\Сайт\other-pages\personal\img\tg\v"))

    # searching_files_in_dir(r'L:\maxim\1 Pаботы\KF\Сайт',
    #                        ('cover.webp', 'cover.svg', 'index.html'),
    #                        deep=True,
    #                        ignore_dir=('TEST', 'default'))
    #
    # print(size_file(r'L:\maxim\1 Pаботы\KF\Сайт\cases\nuqun\img\cover.svg'))

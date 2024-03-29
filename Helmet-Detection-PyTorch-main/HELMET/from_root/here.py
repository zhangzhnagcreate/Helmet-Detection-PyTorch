import traceback
from pathlib import Path

from from_root.base import from_base

__all__ = ['from_here']


def from_here(
        *args: str,
        mkdirs: bool = False,
) -> Path:
    """
    :param args:
    >>> from_here('dir1', 'dir2')
    <DIRECTORY_WHERE_THIS_FUNCTION_WAS_CALLED>/dir1/dir2
    :param mkdirs:
        if True, all non-existing names after <DIRECTORY_WHERE_THIS_FUNCTION_WAS_CALLED> will be created as directories
    :return: `pathlib.Path`
    """

    here_dir = Path(traceback.extract_stack()[-2].filename).parent

    return from_base(
        args,
        mkdirs=mkdirs,
        base_path=here_dir,
    )


def main():
    print(from_here())


if __name__ == '__main__':
    main()

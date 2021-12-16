import os
import pytest

FILE_1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/1.txt')
FILE_2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/2.txt')
FILE_3 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/3.txt')
FILE_4 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/4.txt')
FILE_5 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files/5.txt')


def read_file(path_file):
    """:param path_file: str path file
    :return: content of file"""

    file = open(path_file)
    return file.read()


class TestFile:

    @pytest.mark.parametrize('file_path', [FILE_1, FILE_2, FILE_3, FILE_4, FILE_5])
    def test_verify_content_file(self, file_path):
        """this test verify content of different files"""

        content_file = read_file(file_path)

        if file_path == FILE_1:
            assert content_file == 'a'
        if file_path == FILE_2:
            assert content_file == 'b'
        if file_path == FILE_3:
            assert content_file == 'c'
        if file_path == FILE_4:
            assert content_file == 'd'
        if file_path == FILE_5:
            assert content_file == 'e'

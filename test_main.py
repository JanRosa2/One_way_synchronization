import main
import os
import pathlib
import pytest
from datetime import datetime

def test_make_content_iterator(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = pathlib.Path.joinpath(temp_dir_path, "hello.txt")
    with open(file_path, 'a') as file:
        file.write("hello")
    iterator = main.make_content_iterator(temp_dir_path)
    content = next(iterator)
    assert isinstance(content, os.DirEntry)

def test_make_content_iterator_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.make_content_iterator("path")
        assert exc.value == "Path has to be string."

def test_make_content_iterator_path_not_exists():
    with pytest.raises(ValueError) as exc:
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))
        assert exc.value == f"Path cannot be found."

def test_make_content_list(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = temp_dir_path / "hello.txt"
    with open(file_path, 'a') as file:
        file.write("hello")
    content_list = main.make_content_list(temp_dir_path)
    assert content_list == ["hello.txt"]

def test_make_content_list_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.make_content_list("path")
        assert exc.value == "Path has to be Path object."

def test_make_content_list_path_not_exists():
    with pytest.raises(ValueError) as exc:
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))
        assert exc.value == f"Path cannot be found."

def test_replace_file_wrong_path():
    with pytest.raises(OSError):
        main.replace_file(pathlib.Path("/adadadad/file1"), pathlib.Path("/adadadad/file1"))

def test_replace_file_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.replace_file(10, 10)
        assert exc.value == "Arguments have to be Path objects."

def test_replace_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path1 = my_path1 / "hello.txt"
    with open(file_path1, 'a') as file:
        file.write("hello")
    my_path2 = tmp_path / "mytest2"
    my_path2.mkdir()
    file_path2 = my_path2 / "hello.txt"
    with open(file_path2, 'a') as file:
        file.write("hello")
    assert main.replace_file(file_path1, file_path2) == f"{datetime.now()}: Replaced file '{file_path2.name}'."

def test_delete_file_wrong_path():
    with pytest.raises(OSError):
        main.delete_file(pathlib.Path("/sasasasa/adadadad/file1.txt"))


def test_delete_file_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.delete_file(10)
        assert exc.value == "Argument has to be Path object."

def test_delete_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path1 = my_path1 / "hello.txt"
    with open(file_path1, 'a') as file:
        file.write("hello")
    assert main.delete_file(file_path1) == f"{datetime.now()}: Removed file '{file_path1.name}' from '{file_path1}'."

def test_delete_folder_wrong_path():
    with pytest.raises(OSError):
        main.delete_folder(pathlib.Path("/sasasasa/adadadad/file1"))


def test_delete_folder_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.delete_folder(10)
        assert exc.value == "Argument has to be Path object."

def test_delete_folder(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    main.delete_folder(my_path1)
    assert f"{datetime.now()}: Removed folder '{my_path1.name}' from '{my_path1}'."


def test_copy_file_wrong_path():
    with pytest.raises(IOError):
        main.copy_file(pathlib.Path("random1/rnd/txt.txt"), pathlib.Path("random2/rnd"))

def test_copy_file_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.copy_file(10, 10)
        assert exc.value is "Arguments have to be Path objects."

def test_copy_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path = my_path1 / "hello.txt"
    with open(file_path, 'a') as file:
        file.write("hello")
    my_path2 = tmp_path / "mytest2"
    my_path2.mkdir()
    copy_file_path = my_path2 / "hello.txt"
    assert main.copy_file(file_path, copy_file_path) == f"{datetime.now()}:" \
                                                        f" Copied file '{file_path}' -> '{copy_file_path}'."

def test_copy_folder_wrong_path():
    with pytest.raises(IOError):
        main.copy_folder(pathlib.Path("random1/rnd"), pathlib.Path("random2/rnd"))

def test_copy_folder_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.copy_folder(10, 10)
        assert exc.value is "Arguments have to be Path objects."

def test_copy_folder(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    my_path2 = tmp_path / "mytest2"
    my_path2.mkdir()
    my_path3 = my_path2 / "my_test_folder"
    assert main.copy_folder(my_path1, my_path3) == f"{datetime.now()}: Copied folder '{my_path1}' -> '{my_path3}'."

def is_file_wrong_input():
    with pytest.raises(TypeError) as exc:
        main.is_file(10)
        assert exc.value == "Argument has to be DirEntry object."

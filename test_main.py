from datetime import  datetime
import tempfile

import main
import os
import pathlib
import pytest

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
        assert exc.value is "Path has to be string."

def test_make_content_iterator_path_not_exists():
    with pytest.raises(ValueError) as exc:
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))
        assert exc.value is f"Path cannot be found."

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
        assert exc.value is "Path has to be Path object."

def test_make_content_list_path_not_exists():
    with pytest.raises(ValueError) as exc:
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))
        assert exc.value is f"Path cannot be found."

def test_replace_file_wrong_input():
    main.replace_file(pathlib.Path("/adadadad/file1"), pathlib.Path("/adadadad/file1"))
    pytest.raises(OSError)

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
    main.replace_file(file_path1, file_path2)
    assert f"{datetime.now()}: Replaced file '{file_path2.name}'."

def test_delete_file_wrong_input():
    main.delete_file(pathlib.Path("/adadadad/file1"))
    pytest.raises(OSError)

def test_delete_file_wrong_input_2():
    main.delete_file(10)
    pytest.raises(TypeError)

def test_delete_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path1 = my_path1 / "hello.txt"
    with open(file_path1, 'a') as file:
        file.write("hello")
    main.delete_file(file_path1)
    assert f"{datetime.now()}: Removed file '{file_path1.name}' from '{file_path1}'."


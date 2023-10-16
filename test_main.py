import main
import os
import pathlib
import pytest

def test_make_content_iterator(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = pathlib.Path(temp_dir_path / "hello.txt")
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
    temp_dir_path = pathlib.Path(tmp_path / "test")
    temp_dir_path.mkdir()
    file_path = pathlib.Path(temp_dir_path / "hello.txt")
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
    main.replace_file(pathlib.Path("/adadadad/file1"),pathlib.Path("/adadadad/file1"))
    pytest.raises(OSError)

def test_replace_file(tmp_path):
    temp_dir_path1 = tmp_path / "test1"
    temp_dir_path2 = tmp_path / "test2"
    temp_dir_path1.mkdir()
    temp_dir_path2.mkdir()
    file_path1 = pathlib.Path(temp_dir_path1 / "hello.txt")
    with open(file_path1, 'a') as file:
        file.write("hello")
    file_path2 = pathlib.Path(temp_dir_path2 / "hello.txt")
    with open(file_path2, 'a') as file:
        file.write("hello")
    log_file = file_path2 = pathlib.Path(temp_dir_path2 / "txt.txt")
    main.replace_file(file_path1, file_path2)

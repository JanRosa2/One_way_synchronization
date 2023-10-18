import shutil
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
    assert isinstance(next(main.make_content_iterator(temp_dir_path)), os.DirEntry)

def test_make_content_iterator_wrong_input_0():
    with pytest.raises(TypeError, match="Path has to be Path object."):
        main.make_content_iterator("path")

def test_make_content_iterator_wrong_input_1():
    with pytest.raises(TypeError, match="Path has to be Path object."):
        main.make_content_iterator(None)

def test_make_content_iterator_path_not_exists():
    with pytest.raises(ValueError, match="Path cannot be found."):
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))

def test_make_content_list(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = temp_dir_path / "hello.txt"
    with open(file_path, 'a') as file:
        file.write("hello")
    assert main.make_content_list(temp_dir_path) == ["hello.txt"]

def test_make_content_list_wrong_input_0():
    with pytest.raises(TypeError, match="Path has to be Path object."):
        main.make_content_list("path")

def test_make_content_list_wrong_input_1():
    with pytest.raises(TypeError, match="Path has to be Path object."):
        main.make_content_list(10)

def test_make_content_list_wrong_input_2():
    with pytest.raises(TypeError, match="Path has to be Path object."):
        main.make_content_list(None)

def test_make_content_list_path_not_exists():
    with pytest.raises(ValueError, match="Path cannot be found."):
        main.make_content_list(pathlib.Path("/nonsense/nonsense/nonsense/aokfakfnakfsanmflksanmflksaf"))

def test_delete_file_wrong_path_0():
    with pytest.raises(OSError):
        main.delete_file(pathlib.Path("/sasasasa/adadadad/file1.txt"))

def test_delete_file_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_file(10)

def test_delete_file_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_file("aloha")

def test_delete_file_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_file(None)

def test_delete_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path1 = my_path1 / "hello.txt"
    with open(file_path1, 'a') as file:
        file.write("hello")
    assert f" Removed file '{file_path1.name}' from '{file_path1}'." in main.delete_file(file_path1)

def test_delete_folder_wrong_path():
    with pytest.raises(OSError):
        main.delete_folder(pathlib.Path("/sasasasa/adadadad/file1"))

def test_delete_folder_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_folder(10)

def test_delete_folder_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_folder("aloha")

def test_delete_folder_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.delete_folder(None)

def test_delete_folder(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    assert f" Removed folder '{my_path1.name}' from '{my_path1}'." in main.delete_folder(my_path1)

def test_copy_file_wrong_path():
    with pytest.raises(IOError):
        main.copy_file(pathlib.Path("random1/rnd/txt.txt"), pathlib.Path("random2/rnd"))

def test_copy_file_wrong_input_0():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_file(None, None)

def test_copy_file_wrong_input_1():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_file(None, 10)

def test_copy_file_wrong_input_2():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_file(10, None)

def test_copy_file_wrong_input_3():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_file(None, pathlib.Path("/"))

def test_copy_file_wrong_input_4():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_file(pathlib.Path("/"), None)

def test_copy_file(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    file_path = my_path1 / "hello.txt"
    with open(file_path, 'a') as file:
        file.write("hello")
    my_path2 = tmp_path / "mytest2"
    my_path2.mkdir()
    copy_file_path = my_path2 / "hello.txt"
    assert f" Copied file '{file_path}' -> '{copy_file_path}'." in main.copy_file(file_path, copy_file_path)

def test_copy_folder_wrong_path():
    with pytest.raises(IOError):
        main.copy_folder(pathlib.Path("random1/rnd"), pathlib.Path("random2/rnd"))

def test_copy_folder_wrong_input_0():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_folder(None, None)

def test_copy_folder_wrong_input_1():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_folder(None, 10)

def test_copy_folder_wrong_input_2():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_folder(10, None)

def test_copy_folder_wrong_input_3():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_folder(None, pathlib.Path("/"))

def test_copy_folder_wrong_input_4():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.copy_folder(pathlib.Path("/"), None)

def test_copy_folder(tmp_path):
    my_path1 = tmp_path / "mytest1"
    my_path1.mkdir()
    my_path2 = tmp_path / "mytest2"
    my_path2.mkdir()
    my_path3 = my_path2 / "my_test_folder"
    assert f"Copied folder '{my_path1}' -> '{my_path3}'." in main.copy_folder(my_path1, my_path3)


def test_is_file_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_file(10)

def test_is_file_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_file("aloha")

def test_is_file_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_file(None)

def test_is_file_wrong_input_3():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_file(pathlib.Path("/"))

def test_is_file(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = pathlib.Path.joinpath(temp_dir_path, "hello.txt")
    with open(file_path, 'a') as file:
        file.write("hello")
    iterator = os.scandir(temp_dir_path)
    assert main.is_file(next(iterator))

def test_is_folder_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_folder(10)

def test_is_folder_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_folder("aloha")

def test_is_folder_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_folder(None)

def test_is_folder_wrong_input_3():
    with pytest.raises(TypeError, match="Argument has to be DirEntry object."):
        main.is_folder(pathlib.Path("/"))

def test_is_folder(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    testing_path = temp_dir_path / "test_folder"
    testing_path.mkdir()
    iterator = os.scandir(temp_dir_path)
    assert main.is_folder(next(iterator))

def test_is_file_path_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_file_path(None)

def test_is_file_path_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_file_path(10)

def test_is_file_path_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_file_path("aloha")

def test_is_file_path(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    file_path = pathlib.Path.joinpath(temp_dir_path, "hello.txt")
    with open(file_path, 'a') as file:
        file.write("hello")
    assert main.is_file_path(file_path)

def test_is_folder_path_wrong_input_0():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_folder_path(None)

def test_is_folder_path_wrong_input_1():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_folder_path("aloha")

def test_is_folder_path_wrong_input_2():
    with pytest.raises(TypeError, match="Argument has to be Path object."):
        main.is_folder_path(10)

def test_is_folder_path(tmp_path):
    temp_dir_path = tmp_path / "test"
    temp_dir_path.mkdir()
    assert main.is_folder_path(temp_dir_path)

def test_is_same_wrong_input_0():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(10, 10)

def test_is_same_wrong_input_1():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(pathlib.Path("/something"), 10)

def test_is_same_wrong_input_2():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(10, pathlib.Path("/something"))

def test_is_same_wrong_input_3():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(None, None)

def test_is_same_wrong_input_4():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(None, pathlib.Path("/something"))

def test_is_same_wrong_input_5():
    with pytest.raises(TypeError, match="Arguments have to be Path objects."):
        main.is_same(pathlib.Path("/something"), None)

def test_is_same_wrong_input_6():
    with pytest.raises(ValueError, match="Path does not exist."):
        main.is_same(pathlib.Path("/something/dsfdsafsafa"), pathlib.Path("/something/afafafaa"))

def test_is_same_true(tmp_path):
    tmp_path1 = tmp_path / "folder1"
    tmp_path1.mkdir()
    tmp_path2 = tmp_path / "folder2"
    tmp_path2.mkdir()
    tmp_file_path1 = tmp_path1 / "txt.txt"
    with open(tmp_file_path1, 'a') as file:
        file.write("aloha")
    tmp_file_path2 = tmp_path2 / "txt.txt"
    shutil.copy2(tmp_file_path1, tmp_path2)
    assert main.is_same(tmp_file_path1, tmp_file_path2)

def test_is_same_false(tmp_path):
    tmp_path1 = tmp_path / "folder1"
    tmp_path1.mkdir()
    tmp_path2 = tmp_path / "folder2"
    tmp_path2.mkdir()
    tmp_file_path1 = tmp_path1 / "txt.txt"
    with open(tmp_file_path1, 'a') as file:
        file.write("aloha")
    tmp_file_path2 = tmp_path2 / "txt.txt"
    with open(tmp_file_path2, 'a') as file:
        file.write("alohaj")
    assert main.is_same(tmp_file_path1, tmp_file_path2) is False

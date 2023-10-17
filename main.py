import os
import sys
import shutil
import pathlib
import time
from datetime import datetime

"""
This function returns an iterator of DirEntry objects (for iterating through a content of a folder).
"""
def make_content_iterator(path_folder):
    if isinstance(path_folder, pathlib.Path):
        try:
            iterator = os.scandir(path_folder)
            return iterator
        except IOError as exc:
            print(exc)
    else:
        raise TypeError("Path has to be Path object.")


"""
This function returns a content of a folder as a list of content names.
"""
def make_content_list(path_folder):
    if isinstance(path_folder, pathlib.Path):
        if not os.path.exists(path_folder):
            raise ValueError(f"Path cannot be found.")
        else:
            array = os.listdir(path_folder)
            return array
    else:
        raise TypeError("Path has to be Path object.")


"""
This function replaces a target-folder file with a source-folder file.
"""
def replace_file(source_path, target_path):
    try:
        os.replace(source_path, target_path)
        message = f"{datetime.now()}: Replaced file '{target_path.name}'."
        print(message)
        return message
    except OSError as exc:
        print(exc)


"""
This funtion deletes a file from the given path.
"""
def delete_file(target_path):
    try:
        os.remove(target_path)
        message = f"{datetime.now()}: Removed file '{target_path.name}' from '{target_path}'."
        print(message)
        return message
    except OSError as exc:
        print(exc)


"""
This function deletes a folder from the given path.
"""
def delete_folder(target_path):
    try:
        shutil.rmtree(target_path)
        message = f"{datetime.now()}: Removed folder '{os.path.basename(target_path)}' from '{target_path}'."
        print(message)
        return message
    except IOError as e:
        print(e)


"""
This function copies a file from a source-folder to a target-folder.
"""
def copy_file(source_path, target_path):
    try:
        shutil.copy2(source_path, target_path)
        message = f"{datetime.now()}: Copied file '{source_path}' -> '{target_path}'."
        print(message)
        return message
    except IOError as e:
        print(e)


"""
This function copies a folder from a source-folder to a target-folder.
"""
def copy_folder(source_path, target_path):
    try:
        shutil.copytree(source_path, target_path)
        message = f"{datetime.now()}: Copied folder '{source_path}' -> '{target_path}'."
        print(message)
        return message
    except IOError as e:
        print(e)


"""
This function checks if a DirEntry object is a file.
"""
def is_file(content):
    if isinstance(content, os.DirEntry):
        return os.DirEntry.is_file(content)
    else:
        raise TypeError(f"Argument has to be DirEntry object.")


"""
This function checks if a DirEntry object is a folder.
"""
def is_folder(content):
    if isinstance(content, os.DirEntry):
        return os.DirEntry.is_dir(content)
    else:
        raise TypeError(f"Argument has to be DirEntry object.")


"""
This function checks if a string object is a file.
"""
def is_file_path(content_path):
    if isinstance(content_path, pathlib.Path):
        return os.path.isfile(content_path)
    else:
        raise TypeError(f"Argument has to be Path object.")


"""
This function checks if a string object is a folder.
"""
def is_folder_path(content_path):
    if isinstance(content_path, pathlib.Path):
        return os.path.isdir(content_path)
    else:
        raise TypeError(f"Argument has to be Path object.")


"""
This function checks if files at the path1 and the path2 have same time of creation.
It returns True if yes, False if not.
"""
def is_same(path1, path2):
    if isinstance(path1, (str, pathlib.Path)) and isinstance(path2, (str, pathlib.Path)):
        if pathlib.Path(path1).exists() and pathlib.Path(path2).exists():
            source_time_creation = pathlib.Path(path1).stat().st_mtime_ns
            target_time_creation = pathlib.Path(path2).stat().st_mtime_ns
            if source_time_creation == target_time_creation:
                return True
            return False
        else:
            raise ValueError("Path does not exist.")
    else:
        raise TypeError("Path has to be Path object.")


"""
This function deletes files from the target-folder which are not in the source folder.
"""
def delete_files_not_in_source(target_content_list, source_content_list, target_folder_path):
    for target_content in target_content_list:
        if target_content not in source_content_list:
            content = pathlib.Path(f"{target_folder_path}\\{target_content}")
            if is_file_path(content):
                log_file.write(delete_file(content))
            if is_folder_path(content):
                log_file.write(delete_folder(content))


"""
This is the main function implementing the one way synchronization of two folders.
"""
def synchronize(source_folder_path, target_folder_path):
    # Create an iterator of source-folder content (DirEntry objects)
    source_content_iterator = make_content_iterator(source_folder_path)
    # Create lists of content for both source-folder and target-folder
    source_content_list = make_content_list(source_folder_path)
    target_content_list = make_content_list(target_folder_path)
    # 1. Delete files from the target folder that are not in the source folder
    delete_files_not_in_source(target_content_list, source_content_list, target_folder_path)
    # 2. Replace or copy files from the source folder to the target folder
    for content in source_content_iterator:
        # if next content in a source folder is a file
        if is_file(content):
            target_path = pathlib.Path(f"{target_folder_path}\\{content.name}")
            # if there are same names of the files, check if they are the same
            if content.name in target_content_list:
                content_path = pathlib.Path(content.path)
                # if they are not the same, replace the file in target folder by file from the source folder
                if not is_same(content_path, target_path):
                    log_file.write(replace_file(content_path, target_path))
            # if there are no same names of the files in both folders, copy the file into the target-folder
            else:
                log_file.write(copy_file(content.path, target_path))
        # if next content in a source folder is a folder
        if is_folder(content):
            content_path = pathlib.Path(content.path)
            # if there are the same folder names in both folders
            if content.name in target_content_list:
                # check if that folder in source-folder has any content, if yes
                if len(make_content_list(content_path)) > 0\
                        or len(make_content_list(pathlib.Path(f"{target_folder_path}\\{content.name}"))) > 0:
                    #do recursion
                    synchronize(content_path, pathlib.Path(f"{target_folder_path}\\{content.name}"))
            # if no just copy the folder
            else:
                log_file.write(copy_folder(content_path,
                                           pathlib.Path(f"{target_folder_path}\\{content.name}")))
    return

def main():
    if len(sys.argv) == 5:
        source_folder_path = pathlib.Path(sys.argv[1])
        target_folder_path = pathlib.Path(sys.argv[2])
        try:
            sync_interval = float(sys.argv[3])
        except ValueError:
            sys.exit("Cannot convert to float.")
        while True:
            synchronize(source_folder_path, target_folder_path)
            time.sleep(sync_interval)
            print("...")
    else:
        print("Please provide all the inputs.")
        print("e.g. python main.py 'C:/source' 'C:/target' 50")


if __name__ == '__main__':
    try:
        with open(file=sys.argv[4], mode='a') as log_file:
            main()
    except OSError:
        print("Log file has not been found.")

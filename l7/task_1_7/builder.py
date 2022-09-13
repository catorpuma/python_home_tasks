import os


def make_dir(arg_path):

    path = f'{arg_path}'
    try:
        # to create target 
        os.makedirs(path)
        
    except FileExistsError:
        print("Dir: ", path,  " exists")


def make_file(arg_path_filename):

    file_path = f'{arg_path_filename}'
    open(file_path, 'w').close()

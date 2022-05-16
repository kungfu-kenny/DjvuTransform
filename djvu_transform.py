import os
import time
from subprocess import call
from config import Folder, Commands


def develop_preparations() -> None:
    for f in [
        Commands.install_additional, 
        Commands.install_main
    ]:
        os.system(f)

def check_folder(path:str) -> None:
    return os.path.exists(path) or os.mkdir(path)

def develop_file_merged(file_name:str) -> str:
    return f"merged_{file_name}.pdf"

def develop_folders() -> None:
    for f in [
        Folder.storage,
        Folder.input,
        Folder.output,
    ]:
        check_folder(f)

def develop_file_transform():
    for files in os.listdir(Folder.input):
        path = os.path.join(Folder.input, files)
        if os.path.splitext(files)[1].lower()=='.djvu':
            time_start = time.time()
            path_output = os.path.join(Folder.output, os.path.splitext(files)[0])
            call(f'ddjvu -format=pdf "{path}" "{path_output}"', shell=True)
            print('--------------------------------------------------------------------------------')
            print('Finished:', files, '\nIt took time:', round(time.time()-time_start, 2), 'seconds')
            print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
        os.remove(path)


if __name__ == "__main__":
    develop_preparations()
    develop_folders()
    develop_file_transform()
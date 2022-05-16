import os


class Folder:
    env = os.getcwd()
    storage = os.path.join(env, 'storage')
    input = os.path.join(storage, 'input')
    output = os.path.join(storage, 'output')

class Commands:
    install_additional = "sudo apt install -y libdjvulibre21=3.5.27.1-8ubuntu0.4"
    install_main = 'sudo apt install -y djvulibre-bin libdjvulibre-dev libdjvulibre-text'


import os
from pathlib import Path
import zipfile
import uuid 

CATEGORIES = {'Images' : ['.jpeg', '.png', '.jpg', '.svg'], 
              'Video' : ['.avi', '.mp4', '.mov', '.mkv', '.wmv'],
              'Documents' : ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
              'Music': ['.mp3', '.ogg', '.wav', '.amr'],
              'Archives' : ['.zip', '.gz', '.tar'],
              'Unkknown' : []} 

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {} 

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(text: str) ->str:
    text = text.translate(TRANS)
    for chr in text:
        if ord(chr) in range(48,58):
            continue
        elif ord(chr) in range(65,91):
            continue
        elif ord(chr) in range(97,123):
            continue
        else:
            text = text.replace(chr, "_")
    return text


def delete_empty_folders(path: Path) ->None:

    for root, dirs, files in os.walk(path, topdown=False):
        
        for folder in dirs:
            folder_path = os.path.join(root, folder)
        
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def move_file(file: Path, root_dir: Path, category: str) -> None:

    target_dir = root_dir.joinpath(category)

    if not target_dir.exists():
        target_dir.mkdir()

    new_file_name = target_dir.joinpath(f'{normalize(file.stem)}{file.suffix}')

    if new_file_name.exists():
        new_file_name = new_file_name.with_name(f"{new_file_name.stem}-{uuid.uuid4()}{file.suffix}")
        
    file.rename(new_file_name)    


def get_categories(file: Path) -> str:

    ext = file.suffix.lower()

    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    cat = 'Unknown'
    return cat


def sort_folder(path: Path) -> None:

    for item in path.glob('**/*'):
        
        if item.is_file(): 
            category = get_categories(item)
            move_file(item, path, category)
    delete_empty_folders(path)
    print_lists(path)
    print_all_exrentions(path)
    unzip_archives(path)


def unzip_archives(path: Path) -> None:

    path_archives = os.path.join(path,'Archives')

    if os.path.exists(path_archives):

        for i in os.listdir(path_archives):
            file_extension = list (os.path.splitext(i))
            folder_name = file_extension[0]
        
            extraction_path = os.path.join(path_archives, folder_name)

            if not os.path.exists(extraction_path):
                os.makedirs(extraction_path)

            with zipfile.ZipFile(os.path.join(path_archives, i), 'r') as zip_ref:
                zip_ref.extractall(extraction_path)

def print_lists(path: Path) -> list:
    for item in path.glob('**/*'):
        if item.is_dir():
            file_list = []
            category_name = item.name

            for file in item.glob('*'):
                file_list.append(file.name)
            print (f'\nList of {category_name} : {file_list}\n')

def print_all_exrentions(path: Path)-> list:
        all_ext_set = set()
        
        for item in path.glob('**/*'):
            if item.is_file():
                ext = item.suffix
                all_ext_set.add(ext)
        all_ext_list = list(all_ext_set)
        print (f'\nList of all found extentions  :  {all_ext_list}\n')

def sort():
    try:
        user_input = input("\nSORTER: Enter valid path to folder or enter \"exit\" to leave programm \n>>>" )

        if user_input == "exit":
            return ("End of programm!\n")
        if user_input == "":
            print ("\nPath cannot be empty!")
            return sort()
        
        path = Path(user_input)
    except IndexError:
        return print ('There is no path to folder! Enter path!')
   
    if not path.exists():
        return print (f'The path <<< {path} >>> doesn\'t exist! Enter valid path!')
    sort_folder(path)
    return "SORTER: Folder sorting completed successfully"
    

if __name__ == '__main__':
    print(sort())

import os,sys,shutil,string,argparse
# import urllib.request

def n():
    print(end="\n\n")

def dash():
    print("=="*30)

if (plat:=sys.platform.lower()) == "windows":
	loc = str(input("Enter the path to arange >> "))
elif plat == 'linux':
	loc = "/home/haxsys/downloadscopy2/Downloads"
else:
    print("Does not support your stupid platform")
    exit(1)

# # ===================================== Handling Arguments and other involved function============================================
parser = argparse.ArgumentParser()

# Adding all the required arguments

parser.add_argument(
    '-m', '--file-match', type = str,help='accepts a pathlike string print outs a dictionary of which the key is the matching word and the values is the list of matched files')

parser.add_argument(
    '-p', '--path', type = str,help='accepts a pathlike string (will be used for all as input for other argument')

parser.add_argument(
    '-c', '--create_ext_dir', 
    help='create folders in relation to the existing file extension in the path and moves the related files to the newly created folder \ne.g example.mp4 will cause an "mp4files" folder to be created ',
    action='store_true')

parser.add_argument(
    '-obr', '--organize_by_relation', 
    help='create a folder according to matching files and organize them i.e the ouput from the "-match/-m" ',
    action = 'store_true')

parser.add_argument('-obe', '--organize_by_extension',
                    help='uses the ced function to make extension dirs and uses the obr fuction to arange the files by name',
                    action = 'store_true')


parser.add_argument('-d', '--delete_ext_dir', 
                    help='Empty the extension dirs created and deletes it',
                    action = 'store_true')

parser.add_argument('-de', '--delete_ext_dirtype',type=str,
                    help='Used to delete specific ext_dir e.g mp4->mp4files')

parser.add_argument('-ce', '--create_ext_dirtype',type=str,
                    help='Used to create specific ext_dir e.g html->htmlfiles')

# parser.add_argument('-a', '--about', 
#                     help='Outputs information on the anime in html format')

# parser.add_argument('-ad', '--autodriver', type=str,
#                     help='Automatically download chromedriver if not installed(works on all platforms)')



args = parser.parse_args()

print(args.__dict__)

marg = args.file_match
parg = args.path
darg = args.delete_ext_dir
dearg = args.delete_ext_dirtype
carg = args.create_ext_dir
cearg = args.create_ext_dirtype
obrarg = args.organize_by_relation
obearg = args.organize_by_extension
# ======================================================== End of argument handling ===========================================

# def download_words():
#     url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
#     filename = "allwords.txt"
    
#     if not os.path.exists(filename):
#         urllib.request.urlretrieve(url, filename)


# def is_valid(word: str):
#     download_words() if "allwords.txt" not in os.listdir(os.getcwd()) else None
#     with open("allwords.txt", "r") as f:
#         english_words = set(f.read().splitlines())
#         return word.lower() in english_words

# Function for creating the extension-based folder

def create_ext_dir(path: str, ext_type: str = "", show_existing_dirs: bool = False):
    """
    Create folders for file extensions in the given directory and move files into them.

    Args:
        - path (str): The path of the directory in which the extension folders will be created.
        
        - ext_type (str, optional): If provided, only create a folder for this file extension type.
            Defaults to an empty string.
            
        - show_existing_dirs (bool, optional): If True, return a sorted list of existing extension folders
            in the directory. Defaults to False.

    Returns:
        Union[List[str], str]: If show_existing_dirs is True, return a sorted list of existing extension folders
            in the directory. If ext_type is provided, return a string with a message indicating that the
            extension folder was created and files were moved into it. Otherwise, return a list of all extension
            folders created in the directory.
    """

    os.chdir(path)
    
    just_files = [file for file in os.listdir(path) if os.path.isfile(file) if not file.startswith('.')]
    
    ext_folders = set([f"{((os.path.splitext(file))[1]).removeprefix('.')}files" for file in just_files])
    
        #The 'ext_folders' variable above is the summary of this code only that it is in a list
        # And yes i am aware i am obsessed with list comprehension   
            
        # for self_file in normal_files:     
        #     name,ext = os.path.splitext(self_file)                
        #     raw_ext = ext.removeprefix('.')                
        #     folder_names = f"{raw_ext}files"            
        #     return set(folder_names)
        
    # return list of all the available extention based folder in the directory
    if show_existing_dirs:
        all_dirs= [dirs for dirs in os.listdir(path) if os.path.isdir(dirs) if dirs.endswith("files") and len(dirs)<=20]
        
        return sorted(all_dirs)
        
    # used to create just one type of extention folder
    if bool(ext_type):
        for file in just_files:
            splfile = os.path.splitext(file)
            
            if bool(splfile[1]) == False:
                just_files.remove(file)
                continue
                
            rawext = splfile[1].removeprefix('.')
            
            if rawext == ext_type:
                extfpath = f"{path}/{rawext}files"
                filepath = f"{path}/{file}"
                #creating ext dir
                if os.path.exists(extfpath):
                    #moving proper files into it
                    try:
                        shutil.move(filepath,extfpath)
                        print(f"Moved {file} to {extfpath}",end="\n\n")
                    except shutil.Error:
                        pass
                else:
                    os.mkdir(extfpath)
                    print(f"Created {extfpath} in {path}\n\n")
                    shutil.move(filepath,extfpath)
                    print(f"Moved {file} to {extfpath}",end="\n\n")
                    
            
        return f"Created '{ext_type}files' directory in {path} and moved all {ext_type} files into it"
                
    
    for file in just_files:
        splfile = os.path.splitext(file)
        
        if bool(splfile[1]) == False:
            just_files.remove(file)
            continue
            
        rawext = splfile[1].removeprefix('.')
        
        extdirpath = f"{path}/{rawext}files"
        filepath = f"{path}/{file}"
        #creating ext dir
        if os.path.exists(extdirpath):
            #moving proper files into it
            if filepath == f"{path}/organize.py":
                continue
            shutil.move(filepath,extdirpath)
            print(f"Moved {file} to {extdirpath}",end="\n\n")
        else:
            os.mkdir(extdirpath)
            print(f"Created {extdirpath} in {path}\n\n")
            shutil.move(filepath,extdirpath)
            print(f"Moved {file} to {extdirpath}",end="\n\n")
            
    # print(f"Created the extension folders in {path}\n\n")
    all_dirs = [dirs for dirs in os.listdir(path) if os.path.isdir(dirs) if dirs.endswith("files") and len(dirs)<=15]
    
    return all_dirs
    

# Deleting existing extension folders
def delete_ext_dir(path: str,ext_type: str = "",all: bool = False):
    
    """
        Delete extension-based folders in the specified path.

        Args:
        - path: A string representing the path where the folders will be deleted.
        - ext_type: A string representing the extension keyword of the folder to delete. Default is an empty string.
        - all: A boolean value indicating whether to delete all extension-based folders. Default is False.

        Returns:
        - A string message indicating that the specified or all extension-based folders have been deleted.

        The function first creates a dictionary of extension types and their corresponding folder names.
        It then attempts to delete the specified or all extension-based folders.
        
        If the ext_type argument is not an empty string, the function attempts to delete the folder corresponding to the
        specified extension type. If the folder exists, the function deletes the folder and returns a message indicating that
        the folder was deleted.
        
        If the all argument is True, the function iterates over the keys in the extension directory dictionary and attempts
        to delete each corresponding folder. If a folder exists, the function deletes the folder and prints a message
        indicating that the folder was deleted. The function then returns a message indicating that all extension-based
        created folders have been deleted.

    """
    
    os.chdir(path)
    only_dirs = [file for file in os.listdir(path) if os.path.isdir(file) and (file.endswith("files") and len(file)<=25)]
    
    only_files = [file for file in os.listdir() if os.path.isfile(file)]
    
    
    exts_from_dir = [ext.replace("files","") for ext in only_dirs]
    
    exts_from_file= set([(os.path.splitext(file)[1]).removeprefix('.') for file in only_files])
    

    ext_dir_dict = {}
    

    for ext in exts_from_dir:
        for dirs in only_dirs:
            if ext != " \/-_.," and dirs.startswith(ext):
                ext_dir_dict[ext] = dirs
            else:
                pass
    
    # Now for the main reason of the function
    
    if bool(ext_type) == True:
        
        if ext_type in exts_from_dir:
            path_to_del = f"{path}/{ext_dir_dict[ext_type]}"
    
            for files in os.listdir(path_to_del):
                shutil.move(f"{path_to_del}/{files}",path)
                print(f"moved {path_to_del}/{files} to {path}\n")
                
            if os.path.exists(path_to_del):
                shutil.rmtree(path_to_del)
                print(f'Deleted {ext_dir_dict[ext_type]} from the directory\n')
        else:
            print(f'There is no "{ext_type}" based dir in {path}, it must have been deleted.')

        
    elif all == True:

        if bool(exts_from_dir):
            
            for ext in exts_from_dir:
                print(ext)
                
                delpath = f"{path}/{ext_dir_dict[ext]}"
                
                for files in os.listdir(delpath):
                    if not os.path.exists(files):
                        shutil.move(f"{delpath}/{files}",path)
                        print(f"moved {delpath}/{files} to {path}\n")
                    else:
                        pass
                    
                if os.path.exists(delpath):
                    shutil.rmtree(delpath)
                    print(f'Deleted {ext_dir_dict[ext]} from the directory\n')
                    
        print(f"\nDeleted all ext based folders\n")
    else:
        if bool(ext_dir_dict):
            print(ext_dir_dict,end="\n\n")
            print("\nChoose an extension keyword to delete the folder by specifying the 'ext_type' argument in the function.\n")
        else:
            print("\nNo ext based folder in path\n")
        

# file Grouping algorithm

def similar_file_group(path: str,substr_len: int = 3):
    
    """
        Groups similar filenames in a directory based on a common substring of a certain length.
        
        Args:
            - path (str): The path to the directory containing the files.
            
            - substr_len (int, optional): The minimum length of the common substring required to group files together.
                Defaults to 5.
        
        Returns:
            dict: A dictionary containing groups of similar filenames, grouped by their common substrings.
    """
    files_with_ext = [file for file in sorted(os.listdir(path)) if '.' in file and not file.startswith('.')]
    
    asciilettterandspace = string.ascii_letters + " "
    
    similarfdict = {}
    
    
    similarfdict = {}
    
    for i in range(len(files_with_ext)-1):
        
        curr = str(files_with_ext[i])

        similar_grp = set()
        

        for j in range(i+1,len(files_with_ext)-1):

            currcomp = str(files_with_ext[j])
            
            common_sub = ""
            
            for i in range(min(len(curr),len(currcomp))):
                
                if curr[i].lower() == currcomp[i].lower() and curr[i] in asciilettterandspace:
                    
                    if common_sub.count(' ') > 1:
                        break
                    common_sub += curr[i].lower()

                else:

                    break 
            if len(common_sub) >= 3 :
                
                similar_grp.add(curr)
                
                similar_grp.add(currcomp)

                if common_sub not in similarfdict:             
                    similarfdict[common_sub] = list(similar_grp)
                else:
                    similarfdict[common_sub].extend(similar_grp)
                    similarfdict[common_sub]=list(set(similarfdict[common_sub]))
                                

    return similarfdict
            


def organize_by_relation(dstpath: str = str(os.getcwd()),group_len: int=3):
    
    """
        Group and organize files in the specified destination path based on their filename.

        Args:
        - dstpath: A string representing the path to be organized. Default is the current working directory
        - group_len: An integer representing the length of the group in which the files will be organized. The default value is 4.

        Returns:
        - A string message indicating that the files moving process is complete.

        The function uses the similar_file_group function to group similar files in the destination path by a specified
        substring length. If no files are grouped, the function will print a message indicating that files must have been
        grouped and return 0.

        If files are grouped, the function will iterate over the grouped files and create a new folder for each group using
        the keyword in the file name. The function checks if the folder already exists; if it does, the function prints a
        message indicating that the folder exists. If the folder does not exist, the function creates a new folder and prints
        a message indicating that the folder was created.

        After creating the folder, the function iterates over the files in the group, moves them to the corresponding folder,
        and prints a message indicating that the file was moved. Once all files have been moved, the function returns a message
        indicating that the files moving process is complete.

        Note: The function uses the shutil module to move files and the os module to check if a folder exists and create a new
        folder.
    """
    
    grouped_files_dict = similar_file_group(dstpath,substr_len=group_len)
    
    if bool(grouped_files_dict) == False:
        print(f"Files must have been grouped check {dstpath} for the groups\n")
        return 0

    dictitems = list(grouped_files_dict.items())
    # print(dictitems)
    
    for sets in dictitems:
        
        keywordspath =f"{dstpath}/{sets[0]}"
        # print(keywordspath)
        
        if os.path.exists(keywordspath):
            print(f"{keywordspath} exists\n")
        else:
            os.mkdir(keywordspath)
            print(f"created {keywordspath}\n")
        
        for i in range(len(sets[1])):
            valspath = f"{dstpath}/{sets[1][i]}"
            shutil.move(valspath,keywordspath)
            print(f"moved file {sets[1][i]} -> {keywordspath}\n")
            
    print("Files moving complete")

    

def organize_by_extension(path: str = os.getcwd(),sublen: int = 3,group: bool = False):
    """
    Organizes files in the specified directory by their file extension.

    Args:
        path (str): The directory path to organize. Defaults to the current working directory.
        sublen (int): The length of the subdirectory names for each file extension. Defaults to 3.
        group (bool): Whether to use group related files. Defaults to False.

    Returns:
        None

    Raises:
        OSError: If the specified path does not exist.
        ValueError: If the specified sublen is less than 1.
    """
    os.chdir(path)
    
    ext_dirs = create_ext_dir(path)
    
    if group:
        for exts in ext_dirs:
            extpath = f"{path}/{exts}"
            organize_by_relation(dstpath=extpath)
    else:
        for ext in ext_dirs:
            print(f"Created {ext} in {path}\n")




#=========================== ARGUMENT HANDLING =============================
if marg:
    result = similar_file_group(marg)
    print(result)
else:
    pass

if carg:
    ced = create_ext_dir(parg)
    print(ced)
else:
    pass

if cearg:
    ced = create_ext_dir(parg,ext_type=cearg)
    print(ced)
else:
    pass


if obrarg:
    obr = organize_by_relation(parg)
    print(obr)
else:
    pass
    
if obearg:
    obe = organize_by_extension(parg,group=True)
    print(obe)
else:
    pass
    
if darg:
    delete_ext_dir(parg,all=True)
else:
    pass
    
if dearg:
    delete_ext_dir(parg,ext_type=dearg)
else:
    pass
    
                

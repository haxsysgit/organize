

## Introduction

This is a python script that is designed to automate some file management tasks. It is designed to be run from the command line and supports various options to handle different scenarios. 

## Prerequisites

This script is designed to work with Python 3. You must have Python 3 installed on your system in order to use this script. 

## Getting Started

To use this script, simply run it from the command line. Depending on the operating system you are using, you may need to modify the code to specify the path you want to work with. 

The script supports several command line arguments that can be used to specify what action you want to perform. 

## Arguments

#### `-m / --file-match`

Accepts a path-like string and prints out a dictionary of which the key is the matching word and the values is the list of matched files.

#### `-p / --path`

Accepts a path-like string (will be used for all as input for other argument).

#### `-c / --create_ext_dir`

Create folders in relation to the existing file extension in the path and moves the related files to the newly created folder. For example, `example.mp4` will cause an `mp4files` folder to be created.

#### `-obr / --organize_by_relation`

Create a folder according to matching files and organize them (i.e the output from the `-match/-m`).

#### `-obe / --organize_by_extension`

Uses the `create_ext_dir` function to make extension directories and uses the `obr` function to arrange the files by name.

#### `-d / --delete_ext_dir`

Empty the extension directories created and deletes them.

#### `-de / --delete_ext_dirtype`

Used to delete a specific extension directory, e.g., `mp4->mp4files`.

#### `-ce / --create_ext_dirtype`

Used to create a specific extension directory, e.g., `html->htmlfiles`.

## Usage

Here are some examples of how you can use this script:

### Match files with that are related

```python
python file_manager.py -m "/path/to/files"
```

This command will match all files in the specified path that contain the word "word".

### Create extension-based directories

```python
python file_manager.py -c -p "/path/to/files"
```

This command will create folders for each file extension in the specified path and move the related files into the newly created folder.

### Organize files by relation

```python
python file_manager.py -obr -p "/path/to/files"
```

This command will create a folder for each matching file and organize them accordingly.

### Organize files by extension

```python
python file_manager.py -obe -p "/path/to/files"
```

This command will create folders for each file extension in the specified path and move the related files into the newly created folder, then organize the files within each folder by name.

### Delete extension-based directories

```python
python file_manager.py -d -p "/path/to/files"
```

This command will empty the extension directories created and delete them.

### Delete a specific extension-based directory

```python
python file_manager.py -de "mp4" -p "/path/to/files"
```

This command will delete the `mp4files` directory in the specified path.

### Create a specific extension-based directory

```python
python file_manager.py -ce "html" -p "/path/to/files"
```

This command will create an `htmlfiles` directory in the specified path.

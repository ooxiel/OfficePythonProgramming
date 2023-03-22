# NOTE
# Not every code works in jupyters notebook. Therefore this chapters is written in a .py file

# REPL
# The Python standard shell, or REPL (Read-Eval-Print Loop), allows you to run Python code interactively while working on a project or learning the language. This tool is available in every Python installation, so you can use it at any moment.

#%%
__IMPORT_MODULE_OS = ''
import os

#%% 
DIR__CWD = ''
os.getcwd()  # compare: cwd.png

#%%
DIR__CHANGE_CWD = ''
os.chdir('/mac_files/mac_img')  # specific sub path
os.chdir('..')  # one directory up
os.chdir(os.path.dirname(os.getcwd()))  # one directory up

#%%
DIR__CONTENT = ''
os.listdir()

# %%
DIR__MAKING = ''
# os.mkdir(os.path.join(os.getcwd(), 'data_dir'))  # for the sake of "join" but not necessary
os.mkdir('data_dir')  # python uses always the cwd execpt it's told otherwise

# %%
DIR__TEST_EXISTENCE = ''
# os.path.isdir(os.path.join(os.getcwd(), 'new_dir'))  # for the sake of "join" but not necessary
os.path.isdir('new_dir')  # python uses always the cwd execpt it's told otherwise

# %%
DIR__CREATE_TREE = ''
if not os.path.isdir('lauras_proj/lauras_assets'):
    os.makedirs('lauras_proj/lauras_assets')
    # os.makedirs(os.path.join('lauras_proj', 'lauras_assets'))
else:
    print('folder exists')

#%%
DIR__REMOVE_ONE_DIR = ''
os.rmdir('folder/subfolder')  # remove the subfolder

#%%
DIR__REMOVE_FOLDERS = ''
os.removedirs('folder')  # removes files with the folder but throws excpetion if folders are within the folder

#%%
DIR__REMOVE_FOLDER_WITH_ANY_CONTENT = ''
import shutil
shutil.rmtree('lauras_proj')  # removes the top folder and anything in it


#%%
_FILE__CREATE = ''
open('my_new_file2.txt', 'w')  # w: wipes content, writes; r: read-only; a: appends content to the end

#%%
_FILE__CREATE_WITH = ''
with open('my_new_text_file3.txt', 'w') as f:  # w: wipes content, writes
   f.write('My first line of text')
   f.close  # Closing is optinal. Python will close the file automatically either during garbage collection or the context manager or at program exit.

with open('my_new_text_file3.txt', 'r') as f:  # r: read-only
   print(f.read())
   print()

with open('my_new_text_file3.txt', 'a') as f:  # a: appends content to the end
   f.write('\nA new line, a new life')

with open('my_new_text_file3.txt', 'r') as f:
   print(f.read())
   print()

with open('my_new_text_file3.txt', 'w') as f:
   f.write('the old lines are gone')

with open('my_new_text_file3.txt', 'r') as f:
   print(f.read())

#%%
_FILE__CREATE_WITH_SOME_LINES = ''
with open('my_file_with_lines.txt', 'w') as f:
   f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

with open('my_file_with_lines.txt', 'r') as f: x = f.read().splitlines()  # splitlines() splits a string into a list
for line in x:
   print(line)

#%%
_FILE__PRINT_SENTENCES_INTO_NEW_LINE = ''
# -*- coding: utf-8 -*-
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

x = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

split_into_sentences(x)

#%%
_FILE__CREATE_10_FILES = ''
import os
newfolder = 'my_new_folder'
newfile = 'ny_newfile_'
count = 0
if os.path.isdir(newfolder):
    print('dir exists')
else:
    os.makedirs(newfolder)

os.chdir(newfolder)

while count < 10:
    with open(newfile + str(count), 'w')  as f:
        f.write('arbitrary text in the new file')
        # f.close() -> isn't necessary since the file automatically closes when the block of code within the with statement is exited. 
    count += 1

os.listdir()

# %% 
_FILE__GET_PATH = ''
os.path.realpath(__file__)

#%%
_FILE__LIST_FILES_FOR_LOOP = ''
os.listdir()

for obj in os.listdir():
    if not os.path.isdir(obj) and not obj.startswith('.'):
        print(obj)

#%%
_FILE__LIST_FILES_LIST_COMPREHENSION = ''
os.listdir()

files = [obj for obj in os.listdir() if not os.path.isdir(obj) and not obj.startswith('.')]
print(files)

#%%
_FILE__REMOVE = ''
os.remove('file_to_be_removed')

#%%
_FILE__RENAME = ''
os.rename('mymodules/testfile.txt', 'mymodules/testfilenewname.txt')  # os.rename(src, dst)


#%%
_FILE_DIR__RENAME = ''
os.rename('oldname', 'newname')

#%%
_FILE__MOVE = ''
import os
import shutil

"""three possibilities: os.rename(), os.replace(), shutil.move()"""
# (1) The filename ("file.foo") must be included in both the source and destination arguments. If it differs between the two, the file will be renamed as well as moved.
# (2) The directory within which the new file is being created must already exist.
# (3) On Windows, a file with that name must not exist or an exception will be raised
# (4) shutil.move simply calls os.rename in most cases. However, if the destination is on a different disk than the source, it will instead copy and then delete the source file.
# (5) CAVE: os.replace() will silently replace a file if it exists

os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

#%%
META__MODIFICATION_TIME_UNFORMATED = ''
files = [obj for obj in os.listdir() if not os.path.isdir(obj) and not obj.startswith('.')]
for file in files:
    print(os.stat(file).st_mtime) 

#%%
META__MODIFICATION_TIME_FORMATED = ''
import datetime

files = [obj for obj in os.listdir() if not os.path.isdir(obj) and not obj.startswith('.')]
for file in files:
    timestamp = os.stat(file).st_mtime
    date = datetime.datetime.fromtimestamp(timestamp)
    print(date)

#%%
META__OLDER_THAN_A_DAY = ''
# Notification: Is a file younger or older then a day?
# Possible usecase: Decision if file is going to be archived
import datetime

files = [obj for obj in os.listdir() if not os.path.isdir(obj) and not obj.startswith('.')]
for file in files:
    timestamp = os.stat(file).st_birthtime
    birthdate = datetime.datetime.fromtimestamp(timestamp)
    nowdate = datetime.datetime.now()
    one_day_in_hist = nowdate - datetime.timedelta(days=1)  # minus a day from the actual date'n time
    file_name = file
    if birthdate > one_day_in_hist:
        print(f'{file_name} is younger then a day')
    else:
        print(f'{file_name} is older then a day')












#%%
TREE__OVERVIEW_IN_TREESTRUCTURE = ''  # but not in a graphical way as showed below
os.chdir('/Users/pk/Documents/A3/1Lect_Python')  # os.chdir('subfolder')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('DirPath:', dirpath)
    print('Filenames', filenames)

#%%
TREE__CONCEPTUAL_DESIGN = ''  # the nodes don't create folders or files of any sorts!
# from treelib import Node, Tree  # treelib isn't packaged properly, doesn't work smoothly with pip install bc of a missing wheel file

# tree = Tree()

# tree.create_node("Harry", "harry")  # No parent means its the root node
# tree.create_node("Jane",  "jane"   , parent="harry")
# tree.create_node("Bill",  "bill"   , parent="harry")
# tree.create_node("Diane", "diane"  , parent="jane")
# tree.create_node("Mary",  "mary"   , parent="diane")
# tree.create_node("Mark",  "mark"   , parent="jane")

# tree.show()

#%%
TREE__ENCAPSULATED_LIST = ''
# import treelib, itertools as it, collections as ct  # treelib isn't packaged properly, doesn't work smoothly with pip install bc of a missing wheel file
# lst = [1,['a','b','c','d',['s','t',['ab','cd',['a','b'],'ef'],'u'],'f']] 
# tree = treelib.Tree()
# c = ct.defaultdict(lambda :it.count(1))
# def build_tree(d, t, p = None):
#    last_p = None
#    for a, b in it.groupby(d, key=lambda x:not isinstance(x, list)):
#       if a:
#          for i in b:
#             t.create_node(i, (last_p:=(i if (n:=next(c[i])) == 1 else f'{i}{n}')), parent=p)
#       else:
#          for i in b:
#             build_tree(i, t, p = last_p)

# build_tree(lst, tree)
# tree.show()

# %%
TREE__2ND = ''
# import treelib, itertools as it, collections as ct
# lst = [1,['a','b','c','d',['s','t',['ab','cd',['a','b'],'ef'],'u'],'f','t',['ab','cd',['a','b'],'ef']]] 
# tree = treelib.Tree()
# c = ct.defaultdict(lambda :it.count(1))
# build_tree(lst, tree)
# tree.show()

# %%
TREE__BUILT_WITHOUT_ASSIGNMENT = ''
# import treelib
# def build_tree(d, t, p = None):
#    last_p = None
#    for a, b in it.groupby(d, key=lambda x:not isinstance(x, list)):
#       if a:
#          for i in b:
#             n = next(c[i])
#             last_p = i if n == 1 else f'{i}{n}'
#             t.create_node(i, last_p, parent=p)
#       else:
#          for i in b:
#             build_tree(i, t, p = last_p)

# tree.show()

# %%
TREE__WITHOUT_REPETITIVE_COMPONENTS = ''
# import treelib
# from itertools import zip_longest as zl
# from contextlib import suppress
# def tree_eq(tree, t1, t2):
#    if not hasattr(t1, 'tag') or not hasattr(t2, 'tag'):
#       return False
#    if t1 is None or t2 is None:
#       return False
#    return t1.tag == t2.tag and t1._identifier < t2._identifier and \
#    all(tree_eq(tree, *i) for i in zl(tree.children(t1._identifier), tree.children(t2._identifier)))

# def prune_tree(d, tree):
#    yield d
#    for i in tree.children(getattr(d, 'root', d._identifier)):
#        yield from prune_tree(i, tree)

# tag_d = ct.defaultdict(list)
# for i in prune_tree(tree, tree):
#    if hasattr(i, 'tag') and tree.children(getattr(i, 'root', i._identifier)):
#       tag_d[i.tag].append(i)

# for a, *b in tag_d.values():
#    for i in b:
#       with suppress(treelib.exceptions.NodeIDAbsentError):
#          if tree_eq(tree, a, i):
#              tree.remove_node(i._identifier)

# tree.show()

# %%
_____TODO__LIST_ONLY_TXT_FILES_ETC = ''
# Source: yt: OS Module in Python: Mit Python auf das Filesystem zugreifen
# Source: yt: Corey Schafer
# Source: realpython: https://realpython.com/lessons/with-open-pattern/
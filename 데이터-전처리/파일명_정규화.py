
## TODO 폴더 돌아다니는 것도 자동화할 수 있나?

import os
import re

## set variables
file_path = r"C:\Export\Study & Thoughts\2021-1\프랑스영화탐색_송태효"
name_list = os.listdir(file_path)

## space -> _
def space_to_underbar(name_list):
    for name in name_list:
        src = os.path.join(file_path, name)
        new_name = name.replace(" ", "_")
        dst = os.path.join(file_path, new_name)
        os.rename(src, dst)
    name_list = os.listdir(file_path)


## remove notion page ID(32 alphanumeric tags)
def removeID(name_list):
    md_names = [x for x in name_list
                        if x.endswith(".md")]

    folder_names = [x for x in name_list
                            if x.endswith(".md") == False]

    for name in md_names:
        print("before: ", name)
        try:
            pat = "(.+?)(_[a-z0-9]{32})(.md)"

            src = os.path.join(file_path, name)
            new_name = ''.join(re.search(pat, name).group(1,3))
            dst = os.path.join(file_path, new_name)
            os.rename(src, dst)
            print("after: ",new_name, '\n')

        except:
            print("!error: ",new_name, '\n')


    for name in folder_names:
        print("before: ", name)
        try:
            pat = "(.+?)(_[a-z0-9]{32})"
            src = os.path.join(file_path, name)
            new_name = ''.join(re.search(pat, name).group(1))
            dst = os.path.join(file_path, new_name)
            os.rename(src, dst)
            print("after: ", new_name, '\n')
        except:
            print("!error: ", new_name, "\n")


class obs:
    


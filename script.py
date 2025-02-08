
# read the foundation file until "visited" token found

# create the new entries to add to the markdown                 
#                           ------------------------------------*
# read the entire markdown file                                 |
# add the new entries to the start of the markdown file data    |-------
# write the data back to the file after truncating              |       |
#                           ------------------------------------*       |
# create a "visited" token                                              |---- One function
#                           ------------------------------------*       |
# read the entire foundation file                               |       |
# add the new entries to the start of the foundation file data  |-------
# write the data back to the file after truncating              |
#                           ------------------------------------*
def main(*args, **kwargs):
    _foundation_parser(args[0])

def _foundation_parser(filepath: str):
    with open(filepath, 'r+') as foundation:
        # read the lines in the file until "visited" token found
        data = foundation.read()
        print(data + "\n" + 30*"-")

def _update_markdown_file(file: str):
    with open(filepath, 'r+'):
        # do formulaic operations
        pass

if __name__ == "__main__":
    fp = "./General_Job_App_List.foundation"
    main(fp)
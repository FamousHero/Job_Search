
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

# Foundation entry example:
# "Part Time Front Desk Receptionistjob description opens in a new window
#  Synergy Planning GroupSeal Beach, CA"
def main(*args, **kwargs):
    visit_token = 30 * '-'
    visit_token += '\n'

    _foundation_parser(args[0], visit_token)

def _foundation_parser(filepath: str, visit_token: str):
    print(visit_token+'Reading Entries...')
    with open(filepath, 'r+') as foundation:
        lines = []
        line = foundation.readline()
        # read the lines in the file until "visited" token found
        while line != visit_token:
            lines.append(line)
            line = foundation.readline()
        
        lines.append('\n')
        print('End of new entries...\n')

        new_entries = _group_entries(lines) 
        print('Entries Grouped...') 

        print('\n*.foundation parsed...\nExiting Program\n'+visit_token)
        print(lines)
        print(30*'*')
        print(new_entries)

def _group_entries(lines: list[str]):
    entries = []
    entry = ''

    for line in lines:
        if line == '\n':
            entries.append(entry)
            entry = ''    
            continue
        if entry.find('job description opens in a new window'):
            entry = entry.replace('job description opens in a new window', '')
        entry += line

    return entries

def _update_markdown_file(file: str):
    with open(filepath, 'r+'):
        # do formulaic operations
        pass

if __name__ == "__main__":
    fp = "./General_Job_App_List.foundation"
    main(fp)
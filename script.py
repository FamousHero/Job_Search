import os
import sys
from dotenv import load_dotenv
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
def main():
    load_dotenv()

    visit_token = 30 * '-'
    visit_token += '\n'
    foundation_fp = os.environ.get('FOUNDATION_FILE') 
    markdown_fp = os.environ.get('MD_FILE')
    markdown_entries = _foundation_parser(foundation_fp, visit_token)
    print('\n'+30*'-'+'\n\nUpdating markdown file...')
    _update_markdown_file(markdown_fp, markdown_entries)
    print('\n'+30*'-'+'\n\nComplete!\nTerminating Program...')

    sys.exit(0)

def _foundation_parser(filepath: str | None, visit_token: str):
    print(visit_token+'Reading Entries...')
    with open(filepath, 'r+') as foundation:
        lines = []
        line = foundation.readline()
        # read the lines in the file until "visited" token found
        if line == visit_token:
            print('No new entries to add...\nTerminating Program...')
            sys.exit(0)
        while line != visit_token:
            lines.append(line)
            line = foundation.readline()
        lines.append('\n')
        print('End of new entries...\n')

        new_entries: list[str] = []
        _group_entries(lines, new_entries)

        print('Entries Grouped...') 
        print('Formatting...')
        new_markdown_entries = [_create_markdown_entry(e) for e in new_entries]
        
        print('\n*.foundation parsed...\nNew markdown entries created...\n')
        print(30*'*')
        print(new_markdown_entries)
        print(30*'*')
        foundation.seek(0)
        data = foundation.read()
        foundation.seek(0)
        foundation.write(visit_token)
        foundation.write(data)
        return new_markdown_entries

# Changed this to take output var, might be broken
def _group_entries(lines: list[str], new_entries: list[str]):
    entry = ''

    for line in lines:
        # if blank new-line, entry is complete, append it to list and start new one
        if line == '\n':
            new_entries.append(entry)
            entry = ''    
            continue
        if entry.find('job description opens in a new window'):
            entry = entry.replace('job description opens in a new window', '')
        entry += line

    return new_entries
def _create_markdown_entry(base_entry: str):
    job_title_prefix = ' * '
    job_title_postfix = '\n'
    company_name_prefix = '<span style="color: cyan;"> ('
    company_name_postfix = ') </span> - \n'
    location_prefix = '<span style="color: green; font-size: 20px;">**'
    location_postfix = '**</span>\n'
    job_description_prefix = '   * [Job Description]('
    job_description_postfix = ')\n'
    app_details_prefix = '   * [Application Details]('
    app_details_postfix = ')\n\n'
    title, CompanyLocation, job_description, app_details = (e.strip() for e in base_entry.split('\n')[:-1])
    company, location = CompanyLocation.split('?')
    return (
        f'{job_title_prefix}{title}{job_title_postfix}'
        f'{company_name_prefix}{company}{company_name_postfix}' 
        f'{location_prefix}{location}{location_postfix}'
        f'{job_description_prefix}{job_description}{job_description_postfix}'
        f'{app_details_prefix}{app_details}{app_details_postfix}'
    )

def _update_markdown_file(filepath: str, new_entries: list[str]):
    with open(filepath, 'r+') as markdown_file:
        data = markdown_file.read()
        filename = filepath[:filepath.index('.md')]
        print('Saving copy of old entries...')
        with open(filename+'_OLD.md', 'w') as old_f:
            old_f.write(data)
        print('Complete.\n')
        startpoint = data.find(' * ')
        print('Separating header...')
        top_markdown = data[:startpoint]
        print('Caching old entries...')
        bottom_markdown = data[startpoint:]

        for e in new_entries:
            top_markdown += e
            
        markdown_file.seek(0)
        print('Writing new entries...')
        markdown_file.write(top_markdown)
        print('Writing old entries...')
        markdown_file.write(bottom_markdown)     # do formulaic operations
        

if __name__ == "__main__":
    main()
    # main calls sys.exit(0) this code should never reach
    sys.exit(1)
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.
    #
    # Copyright (c) 2021, Kalcifer



# NOTE: Should I add Docstrings?
import os
import argparse
import re



# This is the directory for the Gnome App-Grid application files. By default, 
# the directory is defined as `/usr/share/applications`; however, it can be 
# modified to point to any directory.
DEFAULT_APPLICATION_DIRECTORY = '/usr/share/applications'


parser = argparse.ArgumentParser()
# TODO: Perhaps look into verbosity level with verbose being not listed being
#       equal to the minimum level of verbosity (ie quiet which is default).
parser.add_argument('--verbose', '-v', action='store_true',
        help="Display verbose command output.")

subparsers = parser.add_subparsers(dest='subcommand')

parser_whitelist = subparsers.add_parser('whitelist', 
        help="Commands pertaining to the modification of the whitelist's \
                contents.")
parser_whitelist.add_argument('--add', '-a', action='store', nargs='+', 
        help="Add entries to the whitelist.")
parser_whitelist.add_argument('--remove', '-r', action='store', nargs='+',
        help="Remove entries frome the whitelist")
parser_whitelist.add_argument('--list', '-l', action='store_true',
        help="List all entries contained within the whitelist")
# parser_whitelist.add_argument('--discriminate', '-d', action='store_true')

parser_clean = subparsers.add_parser('clean', help="Apply the whitelist, and \
        remove unwanted applications from the Gnome App-Grid")

args = parser.parse_args()

if args.subcommand == 'whitelist':  # For modifying the whitelist.
    if args.add:    # For adding entries to the whitelist.
        with open('whitelist', 'r+') as whitelist:
        # 'r+' is for read and write, but the file pointer is placed at the
        # beginning of the file. The following `read()` command will then put
        # the file pointer at the end of the file.
            whitelist_content = whitelist.read()    # Store whitelist contents.
            # Loop thuough all of the files that were specified in the command.
            for application_filename in args.add:
                # If the application filename is already within the whitelist, 
                # then don't add it.
                if application_filename in whitelist_content:
                    print(application_filename + " is already whitelisted.")
                # If the application filename is not within the whitelist, then
                # add it.
                elif application_filename not in whitelist_content: 
                    whitelist.write(application_filename + '\n')
                    if args.verbose:
                        print("Added " + application_filename)
    elif args.remove:   # For removing entries from the whitelist.
        with open('whitelist', 'r') as original_whitelist:
            original_whitelist_contents = original_whitelist.read()
            original_whitelist.seek(0)  # Reset the file-pointer after reading.
            # Check if the requested application filename to be removed is
            # already absent from the whitelist. If so, raise a warning.
            if args.verbose:
                for application_filename in args.remove:
                    if application_filename not in original_whitelist_contents:
                        print(application_filename + " is not whitelisted.")
            with open('new_whitelist', 'w') as new_whitelist:
                # Go through the whitelist's contents, and only keep that which
                # has not been requested to be removed.
                for line in original_whitelist:
                    # Must strip the newline, `\n` character from the end of
                    # each line so that a match can be made.
                    if line.strip("\n") not in args.remove:
                        new_whitelist.write(line)
                    # File is removed by simply not writing it to the new
                    # whitelist.
                    elif (line.strip("\n") in args.remove) and args.verbose:
                        print('Removed ' + line.strip("\n"))
        # Update the whitelist file.
        os.remove('whitelist')
        os.rename('new_whitelist', 'whitelist')
    elif args.list:
        with open('whitelist', 'r') as whitelist:
            for line in whitelist:
                print(line.strip("\n"))
                # NOTE: The newline is stripped off of each entry so that there
                # isn't an extra newline character. The other newline character
                # is generated by the print command.
    # elif args.discriminate:   # Not sure if this is really needed yet.
        # pass
# Apply the whitelist to clean the Gnome App-Grid.
elif args.subcommand == 'clean':
    # Read the contents of the whitelist into a list
    with open('whitelist', 'r') as whitelist:
        whitelist_contents = whitelist.read()
    for application_filename in os.listdir(DEFAULT_APPLICATION_DIRECTORY):
        # Ignore the file if it is not an application file.
        if '.desktop' not in application_filename:
            pass
        else:
            # In case the file already contains a line matching `NoDisplay=`, 
            # then remove it so that there aren't duplicates.
            nodisplay_match = re.compile('NoDisplay=')
            with open(DEFAULT_APPLICATION_DIRECTORY + '/' + application_filename,
                    'r') as application_file:
                with open(DEFAULT_APPLICATION_DIRECTORY + '/new_' 
                        + application_filename, 'w') as new_application_file:
                    for line in application_file:
                        # Write the original application file line to the new
                        # application file if it does not match `NoDisplay`
                        if not nodisplay_match.search(line):
                            new_application_file.write(line)
                    # After we are sure that `NoDisplay` is no longer present, 
                    # rewrite it to the file as true to hide the application.
                    if application_filename in whitelist_contents:
                        new_application_file.write('NoDisplay=false')
                        if args.verbose:
                            print("Preserved " + application_filename)
                    else:
                        new_application_file.write('NoDisplay=true')
                        if args.verbose:
                            print("Removed " + application_filename)
            # Replace the original application file with the new version.
            os.remove(DEFAULT_APPLICATION_DIRECTORY + '/'
                    + application_filename)
            os.rename(DEFAULT_APPLICATION_DIRECTORY + '/new_'
                    + application_filename, DEFAULT_APPLICATION_DIRECTORY 
                    + '/' + application_filename)

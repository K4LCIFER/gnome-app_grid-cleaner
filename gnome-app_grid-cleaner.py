
import os
import argparse


gnome_application_directory = './test-directory'



parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subcommand')

parser_whitelist = subparsers.add_parser('whitelist')
parser_whitelist.add_argument('--add', '-a', action='store', nargs='+')
parser_whitelist.add_argument('--remove', '-r', action='store', nargs='+')
parser_whitelist.add_argument('--list', '-l', action='store_true')
parser_whitelist.add_argument('--discriminate', '-d', action='store_true')

parser_clean = subparsers.add_parser('clean')

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
                    print("Added " + application_filename)
                    whitelist.write(application_filename + '\n')
    elif args.remove:   # For removing entries from the whitelist.
        with open('whitelist', 'r') as original_whitelist:
            original_whitelist_contents = original_whitelist.read()
            original_whitelist.seek(0)  # Reset the file-pointer after reading.
            # Check if the requested application filename to be removed is
            # already absent from the whitelist. If so, raise a warning.
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
                    elif line.strip("\n") in args.remove:
                        print('Removed ' + line)
        # Update the whitelist file.
        os.remove('whitelist')
        os.rename('new_whitelist', 'whitelist')
    elif args.list:
        pass
    elif args.discriminate:
        pass
    else:
        pass
elif arges.subcommand == 'clean':
    pass
else:
    pass

#application_directory = '/usr/share/applications'   # This is the directory where the applicaton `.desktop` files are kept.
#
#whitelist = {}  # Applications that are to be kept, are added to this list as a string.
#
##blacklist = {} # Not sure if this will ever be used. 
#
#applications_to_remove = os.listdir(application_directory)  # Load all the applications into a list. The ones that are to not be removed will be removed from this list in the following lines.
#
#for application in os.listdir(application_directory):   # Loop through all files in the application directory.
#    if (application in whitelist) or ('.desktop' not in application):   # If the file is in the whitlisted applications to keep, or if the file is not an application, then add the file to the remove list.
#        applications_to_remove.remove(application)
#    with open(application_directory + '/' + application, 'r') as application_file:
#        for line in application_file:
#            if 'NoDisplay=true' in line:    # Check if the file has already been removed from the application list.
#                applications_to_remove.remove(application)
#
#for application in applications_to_remove:
#    print(application)
#    with open(application_directory + '/' + application, 'a') as application_file:
#        application_file.write('NoDisplay=true')    # Hide the application from the application menu

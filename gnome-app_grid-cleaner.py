import os
import argparse





parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subcommand')

parser_whitelist = subparsers.add_parser('whitelist')
parser_whitelist.add_argument('--add', action='store', nargs='+')
parser_whitelist.add_argument('--remove', action='store', nargs='+')
parser_whitelist.add_argument('--list', action='store_true')
parser_whitelist.add_argument('--discriminate', action='store_true')

parser_clean = subparsers.add_parser('clean')

args = parser.parse_args()

print(args)

if args.subcommand == 'whitelist':
    if args.add:
        pass
    elif args.remove:
        pass
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

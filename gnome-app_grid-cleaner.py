import os

application_directory = '/usr/share/applications'   # This is the directory where the applicaton `.desktop` files are kept.

whitelist = {}  # Applications that are to be kept, are added to this list as a string.

#blacklist = {} # Not sure if this will ever be used. 

applications_to_remove = os.listdir(application_directory)  # Load all the applications into a list. The ones that are to not be removed will be removed from this list in the following lines.

for application in os.listdir(application_directory):   # Loop through all files in the application directory.
    if (application in whitelist) or ('.desktop' not in application):   # If the file is in the whitlisted applications to keep, or if the file is not an application, then add the file to the remove list.
        applications_to_remove.remove(application)
    with open(application_directory + '/' + application, 'r') as application_file:
        for line in application_file:
            if 'NoDisplay=true' in line:    # Check if the file has already been removed from the application list.
                applications_to_remove.remove(application)

for application in applications_to_remove:
    print(application)
    with open(application_directory + '/' + application, 'a') as application_file:
        application_file.write('NoDisplay=true')    # Hide the application from the application menu

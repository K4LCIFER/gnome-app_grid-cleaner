
# Gnome App-Grid Cleaner 

<!-- NOTE: Look into if App-Grid has a hyphen or not-->

---

## About

The purpose of this script is to clense the Gnome App-Grid of all applications
which are, for you, unwanted. The script functions by modifing each
non-whitelisted application's `.desktop` file in `/usr/share/applications` to
have it's `NoDisplay` parameter set to true which will, in turn, hide the
application from the Gnome App-Grid.

## Usage

To use this script, simply add the applications that you wish to have displayed
in the Gnome App-Grid to the whitelist using the `whitelist` subcommnad, and
then run the `clean` command to hide the unwanted applications.

> **NOTE:** You may need to run the program as root (i.e. run it with `sudo`) as
`/usr/share/applications` is typically a protected directory.

### Command Documentation

- `--verbose`, `-v`
  - Enables verbose command output.
- `whitelist`
  - Commands pertaining to the management of the whitelist.
  - `--add`, `-a`
    - Add an entry to the whitelist. If the whitelist doesn't exist, then it
      will be created.
  - `--remove`, `-r`
    - Remove an entry from the whitelist.
  - `--list`, `-l`
    - List all entries in the whitelist.
- `clean`
  - Clean the Gnome App-Grid, preserving those contained in the whitelist.

## Future Versions

An update to the way that applications are added to the whitelist.

Currently it can be a rather arduous task to search for the file names of the
app that one wishes to hide from the app grid. A future update could add a known
list of file names associated with a program so that adding a program to the
whitelist would be as easy as just typing the name of the program, instead of
trying to track down the actual name of the application file that one wishes to
hide from the app grid. A future update could add a known list of file names
associated with a program so that adding a program to the whitelist would be as
easy as just typing the name of the program, instead of trying  to track down
the actual name of the application file.

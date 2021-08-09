
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

To use this script simply add the applications, found in
`/usr/share/applications`, that you want to keep in your App-Grid to the
whitelist, and then run the `clean` command.

> **NOTE:** You may need to run the program as root (i.e. run it with `sudo`) as
`/usr/share/applications` is typically a protected directory.

### Command Documentation

- `--verbose`, `-v`
  - Enables verbose command output.
- `whitelist`
  - Commands pertaining to the management of the whitelist.
  - `--add`, `-a`
    - Add an entry to the whitelist.
  - `--remove`, `-r`
    - Remove an entry from the whitelist.
  - `--list`, `-l`
    - List all entries in the whitelist.
- `clean`
  - Clean the Gnome App-Grid, preserving those contained in the whitelist.

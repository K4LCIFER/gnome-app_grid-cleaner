
# Gnome App-Grid Cleaner 

<!-- NOTE: Look into if App-Grid has a hyphen or not-->

---

## About

The purpose of this script is to clense the Gnome App-Grid of all applications
which are, for you, unwanted. The script functions by modifing each whitelisted
application's `.desktop` file in `/usr/share/applications` to have it's iaso
`NoDisplay` parameter set to true which will, in turn, hide the application from
the Gnome App-Grid.

## Usage

To use this script simply add the applications, found in
`/usr/share/applications`, that you want to keep in your App-Grid to the
whitelist in the python file, and then run the program.

> **NOTE:** You may need to run as `sudo` as `/usr/share/applications` is
typically a protected directory.

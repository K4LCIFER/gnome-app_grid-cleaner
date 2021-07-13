
# Gnome App-Grid Cleaner <!-- Look into if the name "App-grid" has a hypen or
not -->

---

## About

The purpose of this script is to clense the Gnome App-Grid of all applications
which are, for you, unwanted. The script functions by modifing each whitelisted
application's `.desktop` file in `/usr/share/applications` to have it's iaso
`NoDisplay` parameter set to true which will, in turn, hide the application from
the Gnome App-Grid.


import os
import sys
import pxtorem

# Iterates over files in a directory recursively
# and changes `font-size: *px` CSS declarations to 
# font size: *rem equivalent,
# the parameter `file_check` is a callback function
# which can be used to filter files in the directory
def pxToRemDirectory(path, file_check, css_property):
    for root, _, files in os.walk(path):
        for filename in files:
            if not file_check(filename):
                continue
            src_filename = os.path.join(root, filename)
            if css_property:
                pxtorem.makeAllPxToRemByProperty(src_filename, src_filename, css_property, 16)
            else:
                pxtorem.makeAllPxToRem(src_filename, src_filename, 16)

# checks if a file name has the given extensions
def check_file_name(file_name):
    allowed_extensions = ['html','scss']
    for extension in allowed_extensions:
        extension = '.'+extension
        if file_name.endswith(extension):
            return True

    return False

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print(f'Syntax: {args[0]} <directory-path> [CSS-property]')
        sys.exit(1)
    css_property=None
    if len(args) > 2:
        css_property=sys.argv[2]
    pxToRemDirectory(sys.argv[1], check_file_name, css_property )



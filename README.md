# make-font-sizes-rem
Change all font sizes in SCSS and HTML files in a directory from `px` to `rem`

## Usage
`python3 main.py dir/to/code/`
## Configuration
The file `main.py` has a list of file extensions that may be allowed to be modified.  
You may change that list to add or remove file extensions. For example, you may decide to add `.css` files and to remove `.html` files.  

The file `pxtorem.py` can be imported directly to modify any files that we pass.
This gives the programmer the ability to develop their own algorithm to traverse a directory and select which files they
are interested in changing.

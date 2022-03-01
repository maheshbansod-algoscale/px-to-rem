import re

## Takes a file and changes all CSS
## declarations `css_property: Apx` to 
## `css_property: Brem` where `B` is the
## equivalent size in rem for `A` px
def makeAllPxToRemByProperty(input_filename, output_filename, css_property, root_px=16):
    with open(input_filename) as source_file:
        data = source_file.read()
        pattern = f'{css_property}:\s*(\d+)px';
        new_data = re.sub(pattern, replaceFunction(root_px, css_property), data)
    with open(output_filename, "w") as dest_file:
        dest_file.write(new_data)

# converts all `px` values everywhere to `rem`
def makeAllPxToRem(input_filename, output_filename, root_px=16):
    with open(input_filename) as source_file:
        data = source_file.read()
        pattern = '(\d+)px';
        new_data = re.sub(pattern, replaceFunction(root_px), data)
    with open(output_filename, "w") as dest_file:
        dest_file.write(new_data)

## converts a px value to it's rem equivalent
def pxToRem(px, root_px):
    return px/root_px;

## converts a px value to it's rem equivalent
## returns a string formatted to upto 2 decimal places
def pxToRemFormatted(px, root_px):
    n = pxToRem(px, root_px)
    return ('%.2f' % n).rstrip('0').rstrip('.')

def replaceFunction(root_px, css_property=None):
    def replace_fn(c):
        try:
            val = int(c.group(1))
            val = pxToRemFormatted(val, root_px);
        except:
            val = c.group(1)
        val = f'{val}rem'
        if css_property:
            return f'{css_property}: {val}'
        return val
    return replace_fn

if __name__ == '__main__':
    # test
    filename = 'test-stylesheet.scss'
    op_file = 'test-stylesheet-op.scss'
    makeAllFontSizeToRem(filename, op_file);

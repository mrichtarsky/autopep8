#: W191
if False:
	print  # indented with 1 tab
#:


#: E126 W191
y = x == 2 \
	or x == 3
#: E101 W191
if (
        x == (
            3
        ) or
        y == 4):
	pass
#: E101 W191
if x == 2 \
    or y > 1 \
        or x == 3:
	pass
#: E101 W191
if x == 2 \
        or y > 1 \
        or x == 3:
	pass
#:

#: E101 W191
if (foo == bar and
        baz == frop):
	pass
#: E101 W191
if (
    foo == bar and
    baz == frop
):
	pass
#:

#: E101 W191
if start[1] > end_col and not (
        over_indent == 4 and indent_next):
	return(0, "E121 continuation line over-"
	       "indented for visual indent")
#:

#: E101 W191


def long_function_name(
        var_one, var_two, var_three,
        var_four):
	print(var_one)
#: E101 W191
if ((row < 0 or self.moduleCount <= row or
     col < 0 or self.moduleCount <= col)):
	raise Exception("%s,%s - %s" % (row, col, self.moduleCount))
#: E101 W191
if bar:
	return(
	    start, 'E121 lines starting with a '
	    'closing bracket should be indented '
	    "to match that of the opening "
	    "bracket's line"
	)
#
#: E101 W191
# you want vertical alignment, so use a parens
if ((foo.bar("baz") and
     foo.bar("frop")
     )):
	print "yes"
#: E101 W191
# also ok, but starting to look like LISP
if ((foo.bar("baz") and
     foo.bar("frop"))):
	print "yes"
#: E101 W191
if (a == 2 or
    b == "abc def ghi"
         "jkl mno"):
	return True
#: E101 W191
if (a == 2 or
    b == """abc def ghi
jkl mno"""):
	return True
#: E101 W191
if length > options.max_line_length:
	return options.max_line_length, \
	    "E501 line too long (%d characters)" % length


#
#: E101 W191
if os.path.exists(os.path.join(path, PEP8_BIN)):
	cmd = ([os.path.join(path, PEP8_BIN)] +
	       self._pep8_options(targetfile))
#: E101 W191
if foo is None and bar is "frop" and \
        blah == 'yeah':
	blah = 'yeahnah'
#:
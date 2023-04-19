#
# exception try block
#

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

#
raise NameError('HiThere')

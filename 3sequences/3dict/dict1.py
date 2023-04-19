#
# dictionaries
#

#stepbystep
employees={}
e1={'jrg':{'name':'jrg','last':'pulido','email':'@ucol'}}
e2={'jrg2':{'name':'jrg2','last':'pulido','email':'@ucol2'}}

employees.update(e1)
employees
employees.update(e2)
employees

employees.get('jrg2')

employees.keys()
employees.values()

#
#py2
#
#employees.has_key('jrg2')
#employees.has_key('jrg3')
#vs
#py3
e1.__contains__('jrg')
e1.__contains__('')

# Using String Template

from string import Template

t=Template('$name is the $job of $company')
u=t.substitute(name='Steve', job='CTO', company='Microsoft')
s=t.substitute(name='John', job='CEO', company='Apple')
print(u,s,sep='\n')
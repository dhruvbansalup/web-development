# Jinja Docs
# https://jinja.palletsprojects.com/en/3.1.x/

# Jinja by flask is a templating engine that allows you to generate HTML files programatically
from jinja2 import Template

t=Template("Hello {{Something}}!")
print(t.render(Something="World"))

t=Template("My favorite number: {% for n in range(1,10) %}{{n}}""{% endfor %}")
print(t.render())
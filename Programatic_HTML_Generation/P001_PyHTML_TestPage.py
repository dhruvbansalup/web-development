# Programatically create a simple HTML page using PyHTML library.
import pyhtml as h

t=h.html(
    h.head(
        h.title("Test Page")
    ),
    h.body(
        h.h1("This is a Title of the test page"),
        h.div("lorem ipsum dolor sit amet"),
        h.div(h.h2("This is a sub title"),
              h.p("This is a paragraph"))
    )
)

print(t.render())
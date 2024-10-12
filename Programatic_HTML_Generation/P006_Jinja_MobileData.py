from jinja2 import Template

# HelloTemplate="""
# Hello {{name}}
# """

data=[{"Brand":"Apple","Model":"iPhone 12","Price":1000},
      {"Brand":"Samsung","Model":"Galaxy S21","Price":900},
      {"Brand":"OnePlus","Model":"OnePlus 9","Price":800},
      {"Brand":"Google","Model":"Pixel 5","Price":700},
      {"Brand":"Xiaomi","Model":"Mi 11","Price":600},
      {"Brand":"Oppo","Model":"Find X3","Price":500},
      {"Brand":"Vivo","Model":"X60 Pro","Price":400},
      {"Brand":"Realme","Model":"X7 Pro","Price":300},
      {"Brand":"Huawei","Model":"P40 Pro","Price":200},
      {"Brand":"Sony","Model":"Xperia 1 II","Price":100},
      {"Brand":"LG","Model":"Velvet","Price":50},
      {"Brand":"Nokia","Model":"8.3","Price":25},
      {"Brand":"Motorola","Model":"Edge","Price":10},
      {"Brand":"Asus","Model":"Zenfone 7","Price":5},
      {"Brand":"Lenovo","Model":"Legion Duel","Price":1}]


# HTMLTemplate="""
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Mobile Data</title>
# </head>
# <body>
#     <h1>Mobile Data</h1>
#     <table border="1">
#         <thead><tr>
#             <th>Brand</th>
#             <th>Model</th>
#             <th>Price</th>
#         </tr></thead>
#     <tbody>
#     {% for line in data %}
#         <tr>
#             <td>{{ line.Brand }}</td>
#             <td>{{ line['Model'] }}</td>
#             <td>{{ line.Price }}</td>
#         </tr>
#     {% endfor %}
#         </tbody>
#     </table>
# </body>
# </html>
# """





def main():
    # t=Template(HelloTemplate)
    # print(t)
    # print(t.render(name="World"))


    # Read the HTML Template from a file
    HTMLTemplateFile=open("P006_Jinja_HTML_Template.html.jinja2","r")
    HTMLTemplate=HTMLTemplateFile.read()
    HTMLTemplateFile.close()

    #Render the Template using Jinja2
    h=Template(HTMLTemplate)
    content=h.render(data=data)

    # Save the rendered content
    htmlfile=open("P006_Jinja_MobileData.html","w")
    htmlfile.write(content)
    htmlfile.close()


if __name__ == "__main__":
    #execute only if run as a script
    main()
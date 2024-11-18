TEMPLATE="""
HELLO {name}
"""
T2="This is {p} and {q}"
T3="This is {p:+} and {q:+}"
T4="This is in decimal {value:d} and in hex {value:x}"

def main():
    print(TEMPLATE.format(name="World"))
    print(T2.format(p=5,q=-7))
    print(T3.format(p=5,q=-7))
    print(T4.format(value=10))

    print(f"This is in decimal {10} and in hex {10:x}")
    

if __name__ == "__main__":
    #execute only if run as a script
    main()
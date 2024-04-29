import CPP
while True:
    text = input("test-lexer>")
    result, error = CPP.run(text)

    if error: print(error.as_string())
    else:
        print(result)
    print(text)

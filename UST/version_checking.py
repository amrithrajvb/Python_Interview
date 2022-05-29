import platform

def main():
    message()

def message():
    print("python version {}".format(platform.python_version()))

if __name__=="__main__": main()
import traceback


def tempFunc():
    print("In Temp Fucntion")


def main():
    tempFunc()


if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.format_exc())

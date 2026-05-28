import sys

def fib(i):
    if i <= 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

def main():
    i = int(sys.argv[1])
    print(sys.argv)

    print(">>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>")
    print(f"Calculando fib({i})")
    print(fib(i))
    print("<<<<<<<<<<<<<<<<<<<<<<<")
    print("<<<<<<<<<<<<<<<<<<<<<<<")

if __name__ == "__main__":
    main()

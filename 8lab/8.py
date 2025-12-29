import argparse


def main():
    parser = argparse.ArgumentParser(description="Простой калькулятор")
    subparsers = parser.add_subparsers(dest="command", required=True)
    add_parser = subparsers.add_parser("add", help="Сложить два числа")
    add_parser.add_argument("a", type=float, help="Первое число")
    add_parser.add_argument("b", type=float, help="Второе число")
    mul_parser = subparsers.add_parser("mul", help="Умножить два числа")
    mul_parser.add_argument("a", type=float, help="Первое число")
    mul_parser.add_argument("b", type=float, help="Второе число")
    args = parser.parse_args()
    if args.command == "add":
        result = args.a + args.b
        print(f"{args.a} + {args.b} = {result}")
    elif args.command == "mul":
        result = args.a * args.b
        print(f"{args.a} * {args.b} = {result}")


if __name__ == "__main__":
    main()

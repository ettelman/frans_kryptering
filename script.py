import argparse

parser = argparse.ArgumentParser(description="Mitt kryperingsverktyg")

parser.add_argument("name", help="Ange ditt namn")
parser.add_argument("age", type=int, help="Ange din ålder")

parser.add_argument("-v", "--verbose", action="store_true", help="Visa mer information")

args = parser.parse_args()

if args.verbose:
    print(f"Hej {args.name}, din ålder: {args.age}")
else:
    print(f"Hej {args.name}")
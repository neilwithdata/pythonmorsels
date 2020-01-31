import argparse
import csv


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('in_filename')
    parser.add_argument('out_filename')
    parser.add_argument('--in-delimiter')
    parser.add_argument('--in-quote')

    args = parser.parse_args()

    with open(args.in_filename, 'r', newline='') as in_file, \
            open(args.out_filename, 'w', newline='') as out_file:

        dialect = csv.Sniffer().sniff(in_file.read())
        in_file.seek(0)

        if args.in_delimiter is None:
            args.in_delimiter = dialect.delimiter

        if args.in_quote is None:
            args.in_quote = dialect.quotechar

        reader = csv.reader(in_file,
                            delimiter=args.in_delimiter,
                            quotechar=args.in_quote)
        writer = csv.writer(out_file)

        for row in reader:
            writer.writerow(row)


if __name__ == '__main__':
    main()

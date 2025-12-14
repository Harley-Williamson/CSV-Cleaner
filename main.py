import utils_csv as uc
import argparse

def main():

    parser = argparse.ArgumentParser(description="Clean CRM SCV files")
    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()
    cleaned_data = uc.read_csv(args.input_file)

    uc.write_csv(cleaned_data, args.output_file)

if __name__ == "__main__":
    main()
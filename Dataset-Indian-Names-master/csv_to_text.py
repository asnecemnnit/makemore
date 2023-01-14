import argparse

if __name__ == '__main__':

    # parse command line args
    parser = argparse.ArgumentParser(description="Convert csv to text")
    # system/input/output
    parser.add_argument('--input_csv_path', type=str, default='C:/Users/u7oh2m/WorkingStudent/Personal/GitHub/makemore/Dataset-Indian-Names-master/Indian_Names.csv', help="input file with things one per line")
    parser.add_argument('--output_text_path', type=str, default='C:/Users/u7oh2m/WorkingStudent/Personal/GitHub/makemore/Dataset-Indian-Names-master/Indian_Names.txt', help="input file with things one per line")
    parser.add_argument('--post_process', type=str, default=False, help="input file with things one per line")
    args = parser.parse_args()

    # 1. Open the CSV file in reading mode and the TXT file in writing mode
    with open(args.input_csv_path, 'r') as f_in, open(args.output_text_path, 'w') as f_out:
        # 2. Read the CSV file and store in variable
        content = f_in.read()

        if args.post_process:
            content = content.replace(",", "")
            content = ''.join((x for x in content if not x.isdigit()))
        # 3. Write the content into the TXT file
        f_out.write(content)
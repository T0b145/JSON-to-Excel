import pandas as pd
import json
import argparse
import os

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        # Handle dictionaries by recursive flattening
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        # Handle lists based on their content type
        elif isinstance(x, list):
            # If all items in the list are simple types (str, int, float)
            if all(isinstance(i, (str, int, float)) for i in x):
                # Join the list items into a single string separated by semicolons
                out[name[:-1]] = ';'.join(map(str, x))
            else:
                # If list contains complex types (e.g., dict), flatten recursively
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
        # Base case: store the non-list, non-dict value
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def process_json_file(json_file):
    # Read JSON data from the file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Flatten the JSON data
    flat_data = flatten_json(data)

    # Convert the flattened data into a DataFrame
    df = pd.DataFrame([flat_data])
    return df

def process_jsonl_file(jsonl_file):
    # List to hold all flattened JSON objects
    flattened_data = []

    # Read JSON Lines data from the file line by line
    with open(jsonl_file, 'r') as f:
        for line in f:
            data = json.loads(line.strip())  # Parse each line as JSON
            flat_data = flatten_json(data)  # Flatten the JSON object
            flattened_data.append(flat_data)  # Add the flattened JSON to the list

    # Convert the list of flattened JSON objects into a DataFrame
    df = pd.DataFrame(flattened_data)
    return df

def main():
    # Set up argument parsing with flags
    parser = argparse.ArgumentParser(description='Flatten a JSON or JSON Lines file and convert it to a Pandas DataFrame.')
    parser.add_argument('--file', type=str, required=True, help='Path to the JSON or JSON Lines file to be flattened')
    parser.add_argument('--file-type', type=str, choices=['json', 'jsonl'], default='jsonl', help='Specify the file type: "json" for a regular JSON file or "jsonl" for a JSON Lines file (default: "jsonl")')
    args = parser.parse_args()

    # Process the file based on the file type
    if args.file_type == 'json':
        df = process_json_file(args.file)
    elif args.file_type == 'jsonl':
        df = process_jsonl_file(args.file)

    # Export to Excel
    base_name = os.path.splitext(os.path.basename(args.file))[0]
    output_file = os.path.join(os.path.dirname(args.file), f"{base_name}.xlsx")
    df.to_excel(output_file, index=True)
    print(f"Data saved to {output_file}")

if __name__ == '__main__':
    main()

# JSON/JSONL to Excel Converter

This script is designed to flatten complex JSON or JSON Lines (JSONL) files and convert them into a tabular format, saved as an Excel file (`.xlsx`). The script is flexible and can handle JSON objects that contain nested dictionaries and lists of any depth. Lists with primitive data types (strings, integers, floats) are joined into a single string, separated by semicolons.

## Features

- **Supports both JSON and JSONL formats**: Users can specify the file format (regular JSON or JSON Lines) through a command-line argument.
- **Automatic flattening**: Complex nested structures in JSON are recursively flattened into a single level, making the data easier to handle in tabular form.
- **Automatic Excel output**: The script generates an Excel file with the same name as the input file, saved in the same directory, but with an `.xlsx` extension.

## Usage

### Installation

1. Ensure that you have Python installed (version 3.6+).
2. Install required dependencies by running:
   `pip install pandas openpyxl`

### Running the Script

To convert a JSON or JSONL file to Excel, use the following command:

`python flatten_jsonl.py --file <path_to_your_file> [--file-type <json|jsonl>]`

#### Arguments:

- `--file`: The path to the JSON or JSONL file that you want to flatten and convert.
- `--file-type`: (Optional) The type of file you are processing. It can be either `json` (for regular JSON files) or `jsonl` (for JSON Lines files). The default is `jsonl`.

#### Examples:

1. **For a JSON Lines file (default behavior):**
   `python flatten_jsonl.py --file path_to_your_file.jsonl`
   This command will flatten the JSON Lines file and save the output as `path_to_your_file.xlsx`.

2. **For a regular JSON file:**
   `python flatten_jsonl.py --file path_to_your_file.json --file-type json`
   This command will flatten the regular JSON file and save the output as `path_to_your_file.xlsx`.

### Output

- The script will create an Excel file (`.xlsx`) in the same directory as the input file, with the same base name as the input file.
- For example, if your input file is `data.jsonl`, the output will be `data.xlsx`.

## Contributions are welcome!

- **Add error handling**: Improve the script to handle potential edge cases, such as malformed JSON files or permission issues when saving the output file.
- **Add unit tests**: Implement tests to verify that the flattening process works correctly with various types of JSON structures.
- **Support other output formats**: Extend the script to support additional formats, such as CSV or Parquet.


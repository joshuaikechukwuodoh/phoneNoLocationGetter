# Phone Number Info Finder

A simple Python script to extract information about a phone number using the `phonenumbers` library. This tool provides location and carrier information for phone numbers with country codes.

## Features

- Takes a phone number (with country code) as input.
- Returns the geographical location (country or region) of the phone number.
- Returns the carrier information (if available).
- Handles errors for invalid inputs and missing libraries.

## Requirements

- Python 3.x
- phonenumbers

## Installation

1. Clone this repository or copy the code into a `.py` file.
2. Install the required library:
    ```bash
    pip install phonenumbers
    ```

> **Optional for carrier info:**  
> To ensure carrier information works fully, install with:
> ```bash
> pip install phonenumbers[carrier]
> ```

## Usage

1. Run the script:
    ```bash
    python your_script_name.py
    ```

2. When prompted, enter a phone number with its country code:
    ```
    Enter phone number with country code: +14155552671
    ```

3. The program will output location and carrier details:
    ```
    Location: California
    Carrier: AT&T
    ```

## Example Output
Enter phone number with country code: +2348012345678 Location: Nigeria Carrier: MTN

## Notes

- Make sure to include the `+` sign and country code (e.g., `+1` for US, `+234` for Nigeria).
- Carrier information may not be available for all numbers, depending on the country and number type.
- Handle numbers responsibly and respect user privacy.

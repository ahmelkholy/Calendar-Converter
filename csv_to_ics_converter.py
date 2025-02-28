#!/usr/bin/env python3
"""
Ramadan Calendar Converter

This script converts Ramadan prayer times from CSV format to ICS calendar format
that can be imported into most calendar applications.
"""

import csv
import os
import sys
import argparse
from datetime import datetime
from icalendar import Calendar, Event

def csv_to_ics(csv_file_path, ics_file_path):
    """
    Convert a CSV file containing prayer times to an ICS calendar file.

    Args:
        csv_file_path (str): Path to the input CSV file
        ics_file_path (str): Path where the output ICS file should be saved

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Create a new calendar
        cal = Calendar()
        cal.add('prodid', '-//Ramadan Calendar Converter//mxm.dk//')
        cal.add('version', '2.0')

        # Check if file exists
        if not os.path.exists(csv_file_path):
            print(f"Error: File not found - {csv_file_path}")
            return False

        # Read CSV file, skip comment line if present
        with open(csv_file_path, 'r') as file:
            content = file.readlines()

        # Remove comment line if it exists
        if content and content[0].startswith('//'):
            content = content[1:]

        # Process CSV data
        reader = csv.DictReader(content)
        events_count = 0

        for row in reader:
            # Create event
            event = Event()
            event.add('summary', row['Subject'])

            # Parse start date and time
            try:
                start_datetime_str = f"{row['Start Date']} {row['Start Time']}"
                start_datetime = datetime.strptime(start_datetime_str, '%m/%d/%Y %I:%M %p')
                event.add('dtstart', start_datetime)
            except ValueError as e:
                print(f"Error parsing start date/time for event '{row['Subject']}': {e}")
                print(f"Format should be 'MM/DD/YYYY' and 'HH:MM AM/PM'")
                continue

            # Parse end date and time
            try:
                end_datetime_str = f"{row['End Date']} {row['End Time']}"
                end_datetime = datetime.strptime(end_datetime_str, '%m/%d/%Y %I:%M %p')
                event.add('dtend', end_datetime)
            except ValueError as e:
                print(f"Error parsing end date/time for event '{row['Subject']}': {e}")
                print(f"Format should be 'MM/DD/YYYY' and 'HH:MM AM/PM'")
                continue

            # Add description
            event.add('description', row['Description'])

            # Add unique identifier
            event_id = f"{row['Subject']}-{start_datetime.strftime('%Y%m%d%H%M%S')}"
            event.add('uid', event_id)

            # Add creation timestamp
            event.add('dtstamp', datetime.now())

            # Add event to calendar
            cal.add_component(event)
            events_count += 1

        # Check if any events were added
        if events_count == 0:
            print("No valid events were found in the CSV file.")
            return False

        # Write to file
        with open(ics_file_path, 'wb') as file:
            file.write(cal.to_ical())

        print(f"Calendar successfully converted with {events_count} events.")
        print(f"Saved to {ics_file_path}")
        return True

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False

def main():
    """Main function to handle command line arguments and run the converter"""
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description='Convert Ramadan prayer times from CSV to ICS format'
    )
    parser.add_argument(
        '--input', '-i',
        help='Input CSV file path',
        default=os.path.join(os.path.dirname(__file__), 'RamadanCSV.csv')
    )
    parser.add_argument(
        '--output', '-o',
        help='Output ICS file path',
        default=os.path.join(os.path.dirname(__file__), 'RamadanCalendar.ics')
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    # Parse arguments
    args = parser.parse_args()

    # Show file paths in verbose mode
    if args.verbose:
        print(f"Input CSV file: {args.input}")
        print(f"Output ICS file: {args.output}")

    # Convert CSV to ICS
    success = csv_to_ics(args.input, args.output)

    # Return appropriate exit code
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())

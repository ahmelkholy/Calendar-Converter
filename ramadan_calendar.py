#!/usr/bin/env python3
"""
Ramadan Calendar Command-Line Interface

A CLI tool for managing Ramadan prayer times calendar.
"""

import os
import sys
import argparse
import csv_to_ics_converter as converter


def main():
    """
    Main function that processes command line arguments and runs the appropriate action
    """ 
    parser = argparse.ArgumentParser(
        description="Ramadan Calendar Manager - Convert and manage Ramadan prayer times",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Convert CSV to ICS:
    python ramadan_calendar.py convert RamadanCSV.csv RamadanCalendar.ics

  Show help for a specific command:
    python ramadan_calendar.py convert --help
    """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Convert command
    convert_parser = subparsers.add_parser(
        "convert", help="Convert CSV to ICS calendar"
    )
    convert_parser.add_argument("input_file", help="Input CSV file")
    convert_parser.add_argument("output_file", help="Output ICS file")
    convert_parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    # Info command
    info_parser = subparsers.add_parser(
        "info", help="Show information about the calendar"
    )
    info_parser.add_argument("file", help="Calendar file (CSV or ICS)")

    # Version command
    version_parser = subparsers.add_parser("version", help="Show version information")

    # Parse arguments
    args = parser.parse_args()

    # Handle no command
    if not args.command:
        parser.print_help()
        return 0

    # Handle commands
    if args.command == "convert":
        return handle_convert(args)
    elif args.command == "info":
        return handle_info(args)
    elif args.command == "version":
        return handle_version(args)
    else:
        parser.print_help()
        return 0


def handle_convert(args):
    """Handle the convert command"""
    return converter.csv_to_ics(args.input_file, args.output_file)


def handle_info(args):
    """Handle the info command"""
    if not os.path.exists(args.file):
        print(f"Error: File not found - {args.file}")
        return 1

    if args.file.lower().endswith(".csv"):
        count = count_events_in_csv(args.file)
        if count > 0:
            print(f"CSV file contains {count} prayer time events")
            return 0
        else:
            print(f"No valid prayer times found in CSV file")
            return 1
    elif args.file.lower().endswith(".ics"):
        print(f"ICS calendar file: {args.file}")
        print("Use a calendar application to view the contents")
        return 0
    else:
        print(f"Error: Unsupported file format - {args.file}")
        print("Supported formats: .csv, .ics")
        return 1


def count_events_in_csv(csv_file):
    """Count events in a CSV file"""
    try:
        with open(csv_file, "r") as file:
            content = file.readlines()

        # Remove comment line if it exists
        if content and content[0].startswith("//"):
            content = content[1:]

        # Count rows (excluding header)
        count = len(list(csv.DictReader(content)))
        return count
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return 0


def handle_version(args):
    """Handle the version command"""
    print("Ramadan Calendar Converter v1.0.0")
    print("A tool for converting Ramadan prayer times to calendar format")
    print("Copyright © 2023")
    return 0


if __name__ == "__main__":
    sys.exit(main())

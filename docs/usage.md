# Detailed Usage Guide

This guide provides detailed instructions for using the Ramadan Calendar Converter.

## Command-Line Interface

The Ramadan Calendar Converter provides a command-line interface for easy conversion of calendar files.

### Basic Commands

#### Convert CSV to ICS

To convert a CSV file containing prayer times to an ICS calendar file:

```bash
python ramadan_calendar.py convert input.csv output.ics
```

#### Show Information About a Calendar File

To view information about a calendar file:

```bash
python ramadan_calendar.py info calendar_file.csv
```

#### Show Version Information

To display version information:

```bash
python ramadan_calendar.py version
```

### Advanced Usage

#### Verbose Output

Add the `-v` or `--verbose` flag for more detailed output:

```bash
python ramadan_calendar.py convert input.csv output.ics --verbose
```

## CSV File Format

The CSV file should follow this format:

```
Subject,Start Date,Start Time,End Date,End Time,Description
Fajr (Ramadan 1),3/1/2025,5:18 AM,3/1/2025,5:23 AM,First day of Ramadan - Fajr prayer
```

### Required Columns

1. **Subject**: Name of the prayer event
2. **Start Date**: Date in MM/DD/YYYY format
3. **Start Time**: Time in HH:MM AM/PM format
4. **End Date**: Date in MM/DD/YYYY format
5. **End Time**: Time in HH:MM AM/PM format
6. **Description**: Additional information about the prayer

### Example Entry

```
Fajr (Ramadan 1),3/1/2025,5:18 AM,3/1/2025,5:23 AM,First day of Ramadan - Fajr prayer
```

## ICS File Format

The ICS file follows the iCalendar standard (RFC 5545) and can be imported into most calendar applications.

### Example Event in ICS Format

```
BEGIN:VEVENT
SUMMARY:Fajr (Ramadan 1)
DTSTART:20250301T051800
DTEND:20250301T052300
DTSTAMP:20250228T212250Z
UID:Fajr (Ramadan 1)-20250301051800
DESCRIPTION:First day of Ramadan - Fajr prayer
END:VEVENT
```

## Importing Calendar Files

### Google Calendar

1. Visit [Google Calendar](https://calendar.google.com/)
2. Click on the gear icon (Settings)
3. Click "Import & Export"
4. Select your ICS file
5. Choose the calendar to add the events to
6. Click "Import"

### Apple Calendar

1. Open the Calendar app
2. From the File menu, select "Import..."
3. Select your ICS file
4. Choose which calendar to add the events to
5. Click "Import"

### Microsoft Outlook

1. Open Outlook
2. Click on "File" > "Open & Export" > "Import/Export"
3. Select "Import an iCalendar (.ics) or vCalendar file"
4. Browse to and select your ICS file
5. Choose to add to your calendar or create a new calendar

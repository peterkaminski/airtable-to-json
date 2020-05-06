#!/usr/bin/env python

################################################################
#
# airtable-to-json
#
# Export an Airtable table to a JSON file.
#
# Copyright 2020 Peter Kaminski. See LICENSE.TXT.
#
################################################################

from airtable import Airtable # pip install airtable-python-wrapper
import argparse # pip install argparse
import datetime # core
import json # core
import os # core
import signal # core
import sys # core

# Gracefully exit on control-C
signal.signal(signal.SIGINT, lambda signal_number, current_stack_frame: sys.exit(0))

# Define a fatal error handler
class FatalError(Exception):
    pass

# Set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Export an Airtable table to a JSON file.')
    parser.add_argument('--base', required=True, help='base ID (looks like "appXXXXXXXXXXXXXX")')
    parser.add_argument('--table', required=True, help='table name')
    parser.add_argument('--formula', help='formula to filter with')
    parser.add_argument('--output', help='filename to write to (otherwise writes to BASE-TABLE_DATE.json)')
    parser.add_argument('--apikey', help='Airtable API key (looks like "keyXXXXXXXXXXXXXX") (or specify with AIRTABLE_API_KEY environment variable')
    return parser

# Main entrypoint
def main():
    try:
        # get arguments
        argparser = init_argparse();
        args = argparser.parse_args();

        # get API key from environment if not in args
        if args.apikey is None:
            try:
                airtable_api_key = os.environ['AIRTABLE_API_KEY']
            except KeyError:
                raise FatalError("Please specify your Airtable API key in the 'AIRTABLE_API_KEY' environment variable.")

        else:
            airtable_api_key = args.apikey

        # set up Airtable connection
        table = Airtable(args.base, args.table, api_key=airtable_api_key)

        # read table
        table_data = table.get_all(formula=args.formula)

        # write JSON
        if args.output is None:
            run_time = str(datetime.datetime.utcnow().isoformat()) + 'Z'
            output_filename = "{}-{}_{}.json".format(args.base, args.table, run_time.replace(':','_'))
        else:
            output_filename = args.output
        with open(output_filename, 'w') as outfile:
            json.dump(table_data, outfile, indent=True)

        print("Wrote '{}'".format(output_filename), file=sys.stderr)

    except FatalError as err:
        print("\n\nFatal error, exiting: {}\n".format(err));
        sys.exit(1)

# Run this script
if __name__ == "__main__":
    exit(main())

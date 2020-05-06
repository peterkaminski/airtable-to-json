# PK Airtable Dump

## Overview

Export an Airtable table to a local file.

This is a utility which connects to an Airtable base and exports one table to a local file, currently in JSON format.

To run `pk-airtable-dump.py`, you specify your Airtable API key, the base ID (found by going to "Help -> API Documentation" when in your base), the table name, and an optional formula which causes the tool to only export records for which the formula evaluates as TRUE (basically, a filter).

### Installation

Clone the git repo.

```shell
git clone https://github.com/peterkaminski/pk-airtable-dump.git
cd pk-airtable-dump
```



(Optional) Set up a Python virtual environment.

```shell
virtualenv -p python3 venv
source venv/bin/activate
```

## Examples

Make sure to keep your  Airtable API key safe.  You can specify it either on the command line, or if it is more secure in your environment, you can specify it as an environment variable.

### Specify API Key

Copy `env.sh-template` to `env.sh`.  Add your API key to the file.

Set the key:

```shell
source env.sh
```

You only need to do this once per shell session.

Alternatively, you can specify the API key with the `--apikey` flag each time.

### Run pk-airtable-dump.py

```shell
./pk-airtable-dump.py --base appXXXXXXXXXXXXXX --table Movies
```

The output file will be named after the base, the table, and the current time:

```
Wrote 'appXXXXXXXXXXXXXX-Movies_2020-05-06T15_57_10.231881Z.json'
```

If you prefer a different output filename, specify it with the `--output` flag.

### Run pk-airtable-dump.py with a Formula

```shell
./pk-airtable-dump.py --base appXXXXXXXXXXXXXX --table Movies --formula '({Year} = 1948) = 1'
```

Note that the formula needs to be a boolean, so you may need to wrap your formula with "(formula) = 1" or "(formula) = 0".

## License

Copyright 2020 Peter Kaminski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


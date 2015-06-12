#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanize
import argparse
import re, os, sys
from datetime import date, timedelta
br = mechanize.Browser()
parser = argparse.ArgumentParser()
parser.add_argument('-date', type=str, default='today',
        help='Date of Commit. YYYY-MM-DD'\
                + ' or Relative Date i.e today,'\
                + ' yesterday or 4 days ago')
flags = parser.parse_args()
__REL_PATTERN_ = "^(today)|(yesterday)|([1-9][0-9]?) days? ago$"
__ABS_PATTERN_ = "(2\d\d\d)-([0-1]\d)-([0-3]\d)"
__rel_ = re.match(__REL_PATTERN_, flags.date)
__abs_ = re.match(__ABS_PATTERN_, flags.date)
__DIR_ = 'CommitStrip'
if __rel_:
    if __rel_.groups()[0]:
        __COMMIT_DATE_ = str(date.today())\
                .replace('-', '/')
    elif __rel_.groups()[1]:
        __COMMIT_DATE_ = str(
                    date.today() - timedelta(1)
                ).replace('-', '/')
    elif __rel_.groups()[2]:
        __COMMIT_DATE_ = str(
                    date.today() - timedelta(
                        int(__rel_.groups()[2])
                    )
                ).replace('-', '/')
    else:
        print 'Invalid Operation.'
        sys.exit(1)
elif __abs_:
    __COMMIT_DATE_ = "/".join(__abs_.groups())
else:
    print 'Invalid Operation.'
    print 'Exiting...'
    sys.exit(1)

def main():
    print 'Requested Date: ', __COMMIT_DATE_
    try:
        response = br.open(
                "http://www.commitstrip.com/"+__COMMIT_DATE_
                ).read().replace('"', "'")
        url = re.findall("<img class='aligncenter size-full "\
                + "wp-image-(?:\d+)' src='(.+)' alt=''", response)[0]
        filename = re.findall("(?:.+)(Strip(?:.+))", url)[0]
        if not os.path.exists('./' + __DIR_):
            os.makedirs('./' + __DIR_)
        if os.path.exists(__DIR_ + os.sep + filename):
            print 'File already downloaded.'
            sys.exit(0)
        print 'Downloading...'
        br.retrieve(url, __DIR_ + os.sep + filename)
        print 'Downloaded.'
    except IndexError:
        print 'Website might have had a different '\
                + 'structure at that time.'
        sys.exit(0)
    except Exception as e:
        if 'HTTP Error 404' in str(e):
            print 'No commits on that day.'
            sys.exit(0)
        else:
            raise e

if __name__ == '__main__':
    try:
        main()
        print 'Exiting...'
    except KeyboardInterrupt:
        print "Operation Cancelled."
        sys.exit(1)

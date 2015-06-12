#CommitStrip Strips Fetcher

CSF is a Python2 tool that automates downloading commits from
[CommitStrip](http://www.commitstrip.com).


##Usage

- Launch the tool with an optional argument `-date`. If not specified, the
  `-date` argument will default to `today`.
- The requested date can be provided in two formats: Absolute or Relative, i.e
  `YYYY-MM-DD` or values like `today`, `yesterday`, `4 days ago`, `1 day ago`,
  etc.
- The tool connects to `http://www.commitstrip.com` and fetches the commit, if
  available, and if the structure is unchanged, with respect to the last git
  commit of this tool.
- If a commit is fetched, it is stored in `./CommitStrip/`. (The directory will
  be created automatically if it does not exist)


##Requirements

The following Python modules are needed:
- argparse
- mechanize
- datetime


##License

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                Version 2, December 2004

Copyright 2015 zshulu|Von Schmidt

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.

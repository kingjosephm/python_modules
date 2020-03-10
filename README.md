### Overview
This program seeks to standardize the Python packages available across computers in IDA's PII Enclave by creating one directory containing a new Python virtual environment with the most up-to-date version of _all_ packages (and dependencies) available in the Anaconda distribution. These ~600 packages, some of the most common Python libraries, are a superset of packages included in the default Anaconda distribution. We augment this with a list of other useful modules that are not part of Anaconda but still available on PiPy (see `extra_packages.csv`).

This program is designed to be push-button such that it can be run at regular intervals (perhaps every other month). As the list of packages available on Anaconda's website changes, so too may the list of extra packages need to be changed.

***Note:*** This program does _not_ account for updates to Python itself, which will still need to be manually downloaded and potentially overwrite older Python executables. The Python virtual environment version created by this program will be that of whatever main Python executable a user has on their machine.

### Requirements
To run this program you'll need Python (version 3.7) and Bash (version 4.4) installed and on your system's PATH. It takes several hours to complete all downloads, so a stable internet connection is essential. Though less problematic with today's machines, you'll also need about 4.5 GB of hard drive space to download everything. ***Note:*** You do not need to install any specific Python modules, the program does that for you.

### Running the program
- Depending on your system configuration, double click `driver.sh` or run this in Bash command prompt.

### Program overview
- Creates a new directory with the day's date at `../data/<YYYY-MM-DD>`
- Creates a new Python virtual environment under `../data/<YYYY-MM-DD>`
- Downloads the required Python modules for web scraping (described below)
- Scrapes Anaconda's website for the full package list associated with the latest version of Python win-64, saving this to `../data/<YYYY-MM-DD>/anaconda_pkg_list`
- Concatenates `extra_packages.csv` to the Anaconda list
- Package-by-package downloads the complete list from PyPi (via pip install). _Note:_ Bulk installing all packages at once leads to program failure due to version conflicts across packages. While downloading packages (and their dependencies) sequentially allows the program to complete, version conflicts may remain and need to be resolved on a case-by-case basis.

<br>

Author: Joe King <br>
Date: 2020-03-10

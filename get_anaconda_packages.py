import os
from datetime import date
from requests_html import HTMLSession
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # Scrape Anaconda main page for latest version of Python, with link to list
    session = HTMLSession()
    url = 'https://docs.anaconda.com/anaconda/packages/pkg-docs/'
    r = session.get(url, verify=False)
    links = list(r.html.absolute_links)

    link = ''.join(sorted([i for i in links if "win-64" in i])[-1]) # search for latest win-64 version package list and save link

    # Scrape website with Anaconda package list using latest list
    r = session.get(link, verify=False)

    # Get the table of packages
    bs = BeautifulSoup(r.text, "lxml")
    tr_elements = bs.find_all('table')

    # Reduce to package names, removing HTML formatting strings
    for row in tr_elements:
        elements = row.find_all('td')
        elements = [x.text.strip() for x in elements]

    # Every 4th item is package name in table
    pkgs = []
    for i in range(0, len(elements), 4):
        pkgs.append(elements[i])

    pkgs = pkgs[2:] # first two appear to be Anaconda config files

    # Output list of packages to text file
    path = '../data/' + str(date.today()) + '/anaconda_pkg_list/'
    os.makedirs(path, exist_ok=True)
    with open(path+'packages.txt', 'w') as output:
        for pkg in pkgs:
            output.write(pkg + '\n')
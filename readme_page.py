'''
This script creates a simple readme GitHub Page for a repository.

The page is only based on the README.md of the master branch of your project
repository that is retrieved automatically by the remote origin url.

The following resources are created:

    * mkdocs.yml - mkdocs configuration file
    * docs - documentation folder
    * docs/index.md - Index page of the documentation

The building and deployment of a GitHub Page is done by mkdocs.

Author: Fernando Felix do Nascimento Junior
License: The MIT License
'''
import os
import yaml
import subprocess
from six.moves.urllib.request import urlopen
from six.moves.urllib.request import urlretrieve
from bs4 import BeautifulSoup


def cmd(s):
    '''Execute the command (a string) in a subshell and return its output.'''
    return subprocess.check_output(s.split())


def create_configuration(repo_url):
    '''Create configuration with its settings based on the repository.'''
    soup = BeautifulSoup(urlopen(repo_url).read())

    data = dict(
        repo_url=repo_url,
        site_name=soup.find('article').find('h1').contents[1].strip(),
        site_description=soup.find(attrs={'name': 'description'})['content'],
        theme='bootstrap'
    )

    with open('mkdocs.yml', 'w') as f:
        f.write(yaml.dump(data, default_flow_style=False))


def create_index(repo_url):
    '''Create the index of the documentation with the repository readme.'''
    readme_url = repo_url + '/raw/master/README.md'
    urlretrieve(readme_url, 'docs/index.md')


def create_docs():
    '''Create the documentation folder if it does not already exist.'''
    if not os.path.exists('docs'):
        os.makedirs('docs')

remote_url = cmd('git config --get remote.origin.url').decode('utf-8').strip()
repo_url = 'https://' + remote_url.split('@')[1].replace(':', '/')
create_configuration(repo_url)
create_docs()
create_index(repo_url)
cmd('mkdocs build --clean')
cmd('mkdocs gh-deploy --clean')

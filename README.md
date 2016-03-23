# Readme Page

A script to create a simple readme [GitHub Page](https://help.github.com/articles/creating-project-pages-manually) for your project.

The page is only based on the README.md of the master branch of your project repository.

## Usage

1. Download the [Readme Page](https://github.com/fernandojunior/readme-page/archive/master.zip) inside your local repository.

2. Unpack it `unzip *.zip`.

4. Change the current working directory to `cd readme-page*`.

3. Run `make readme-page` to create your repository GitHub Page.

    Run `make help` for more information.

4. Checkout the repository page at `http://<your_github_username>.github.io/<repository_name>`

    See an [example](http://fernandojunior.github.io/readme-page).

    Run `make clean` to remove all generated artifacts.

## Contributing

See [CONTRIBUTING](/CONTRIBUTING.md).

## License

[![CC0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The MIT License.

-

Copyright (c) 2016 [Fernando Felix do Nascimento Junior](https://github.com/fernandojunior/).

-

This project uses [mkdocs](http://mkdocs.github.io/mkdocs-bootstrap/), a Python tool to create project documentation with markdown.

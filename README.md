# Sublime DjHTML

A plugin for [Sublime Text](https://www.sublimetext.com/) that integrates [DjHTML](https://github.com/rtts/djhtml) to provide auto-indentation for Django/Jinja templates.

**Requirements**: Sublime Text 4

## Installation

This plugin can be cloned into the `Packages/` directory of Sublime Text:

1. Find the local directory (`Preferences -> Browse Packages`).

2. Clone the repo:

```shell
git clone https://github.com/jordaneremieff/sublime_djhtml
```

## Usage

The auto-indent command can be applied in a different few ways:

- From the Command Palette by selecting `DjHTML: Indent File`
- Using a keyboard shortcut (default `ctrl + shift + i`)
- Configuring the `indent_on_save` setting (see settings section below)

As an example, consider a template that looks like this:

<img width="280" alt="Screen Shot 2021-06-06 at 3 11 29 pm" src="https://user-images.githubusercontent.com/1376648/120913355-d9d8d080-c6d9-11eb-8fb2-b8d9e33129a1.png">

Running the auto-indent command will process the current file using DjHTML and update the editor directly:

<img width="280" alt="Screen Shot 2021-06-06 at 3 12 07 pm" src="https://user-images.githubusercontent.com/1376648/120913354-d8a7a380-c6d9-11eb-9289-0807130db145.png">

## Settings

- `tabwidth` (default=`4`):

    The number of spaces used in indentation.

- `indent_on_save` (default=`false`)

    Run indentation automatically on file save.

- `enabled_syntax` (default=`["Packages/HTML/HTML.sublime-syntax", "Packages/Djaneiro/Syntaxes/HTML (Django).tmLanguage"]`)

    A list of file [syntax definitions](https://www.sublimetext.com/docs/syntax.html) eligible for auto-indentation when `indent_on_save` is enabled.




If you encounter any problems, please open an issue.

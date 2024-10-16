# Charminal (Charm Terminal)

Charminal is a simple and fun Python library designed to enhance your terminal output with emojis, colors, and styles! Whether you're developing scripts or building command-line tools, Charminal can help you make your terminal messages more vibrant and expressive.

![Charminal-logo](./Charminal-v01.png)

## Features

- **Emojis**: A collection of commonly used emojis to add fun and meaning to your terminal messages.
- **Colors**: Use ANSI escape codes to style your output text with different colors (red, green, yellow, blue, etc.).
- **Text Styles**: Apply bold or underline styles to your text for emphasis.

## Installation

You can install Charminal via pip:

```bash
pip install charminal
```

## Usage
1. Import
```python
from charminal import *
```

2. Show available emojis
```python
show_emojis()
```
Example output:
```bash
  >> EMOJI_BEGIN: 🚀
  >> EMOJI_ERROR: 💥
  >> EMOJI_WARNING: 🚨
  >> EMOJI_HINT: 💡
```

3. Show available colors
```python
show_colors()
```
Example output:
```bash
  >> \033[31mCOLOR_RED\033[0m
  >> \033[32mCOLOR_GREEN\033[0m
  >> \033[33mCOLOR_YELLOW\033[0m
  >> \033[34mCOLOR_BLUE\033[0m
```

4. Show available styles
```python
show_styles()
```
Example output:
```bash
  >> STYLE_BOLD
  >> STYLE_UNDERLINE
```

5. Find Emoji
```python
find_emoji('error')
```
Example output:
```bash
EMOJI_ERROR: 💥
```

6. Show Usage
```python
show_usage()
```
Example output:
```bash
==== [🚀User Guide🚀] ====
1. Import the emojis or colors:
   `from pwnwas_emoji import emojis, colors`
2. Use emojis in print statements:
   `print(f'{EMOJI_WARNING} Warning message')`
   >> 🚨 Warning message
3. Use colors:
   `print(f'{COLOR_RED}{EMOJI_WARNING}Error message{RESET}')`
   >> 💥 Error message
```

7. Find an Emoji
```python
help_me()
```
Example output:
```python
There are some "helper" functions that you can call
Try:
    show_emojis(),
    show_colors(), 
    show_styles(),
    show_usage(),
    find_emoji(keyword)
```

## Contribution
Contributions are welcome! Feel free to open an issue or create a pull request on [GitHub](https://github.com/sulaimanfawwazak/Charminal).

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Author
Charminal is developed and maintained by Sulaiman Fawwaz Abdillah Karim. You can reach me at sulaimanfawwazak@gmail.com.

## Behind The Logo
The name of this package is "Charminal", a combination of "Charm" and "Terminal". The name "Charminal" itself is similar to a Pokemon character, "Charmander". Hence, I decided to make the logo to be the combination of "Charmander" and "Terminal". Though it looks simple, but subjectively I kinda like it!. Hope you like it too!
# charminal.py

########## START OF DEFINITIONS ##########
# Message Emojis
EMOJI_BEGIN = '\U0001F680'
EMOJI_ERROR = '\U0001F4A5'
EMOJI_WARNING = '\U0001F6A8'
EMOJI_HINT = '\U0001F4A1'
EMOJI_SAVING = '\U0001F4BE'
EMOJI_TIME = '\U000023F1'
EMOJI_DEBUG = '\U0001f514'
EMOJI_FINISH = '\U0001F3C1'
EMOJI_TIME = '\U0000231B'
EMOJI_STAR = '\U00002B50'
EMOJI_CHAT = '\U0001F4AC'
EMOJI_STATISTIC = '\U0001F4CA'
EMOJI_BATTERY = '\U0001F50B'
EMOJI_FIRE = '\U0001F525'
EMOJI_AIR = '\U0001F4A8'
EMOJI_JOYSTICK = '\U0001F3AE'
EMOJI_MAP = '\U0001F5FA'
EMOJI_CALENDAR = '\U0001F4C5'
EMOJI_CLOCK = '\U0001F550'
EMOJI_CHART = '\U0001F4CA'
EMOJI_PIN = '\U0001F4CC'
EMOJI_CHECKPOINT = '\U0001F6A9'

# ANSI escape codes for different colors
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"

# ANSI escape codes for different colors
TEXT_BLACK = "\x1b[30m"
BACKGROUND_RED = f"\x1b[41m{TEXT_BLACK}"
BACKGROUND_GREEN = f"\x1b[42m{TEXT_BLACK}"
BACKGROUND_YELLOW = f"\x1b[43m{TEXT_BLACK}"
BACKGROUND_BLUE = f"\x1b[44m{TEXT_BLACK}"
BACKGROUND_MAGENTA = f"\x1b[45m{TEXT_BLACK}"
BACKGROUND_CYAN = f"\x1b[46m{TEXT_BLACK}"
BACKGROUND_WHITE = f"\x1b[47m{TEXT_BLACK}"

# ANSI escape codes for text styles
STYLE_BOLD = "\033[1m"
STYLE_ITALIC = "\x1b[3m"
STYLE_UNDERLINE = "\033[4m"
STYLE_BLINK = "\033[5m"
STYLE_STRIKETHROUGH = "\x1b[9m"
STYLE_HIDDEN = "\x1b[8m"

# ANSI escape code to reset all colors and styles
RESET = "\033[0m"
########## END OF DEFITIONS ##########

########## START OF FUNCTIONS ##########
EMOJIS_DICT = {
  'EMOJI_BEGIN' : '\U0001F680',
  'EMOJI_ERROR' : '\U0001F4A5',
  'EMOJI_WARNING' : '\U0001F6A8',
  'EMOJI_HINT' : '\U0001F4A1',
  'EMOJI_SAVING' : '\U0001F4BE',
  'EMOJI_TIME' : '\U000023F1',
  'EMOJI_DEBUG' : '\U0001f514',
  'EMOJI_FINISH' : '\U0001F3C1',
  'EMOJI_TIME' : '\U0000231B',
  'EMOJI_STAR' : '\U00002B50',
  'EMOJI_CHAT' : '\U0001F4AC',
  'EMOJI_STATISTIC' : '\U0001F4CA',
  'EMOJI_BATTERY' : '\U0001F50B',
  'EMOJI_FIRE' : '\U0001F525',
  'EMOJI_AIR' : '\U0001F4A8',
  'EMOJI_JOYSTICK' : '\U0001F3AE',
  'EMOJI_MAP' : '\U0001F5FA',
  'EMOJI_CALENDAR' : '\U0001F4C5',
  'EMOJI_CLOCK' : '\U0001F550',
  'EMOJI_CHART' : '\U0001F4CA',
  'EMOJI_PIN' : '\U0001F4CC',
  'EMOJI_CHECKPOINT' : '\U0001F6A9'
}

COLORS_DICT = {
  'COLOR_RED' : "\033[31m",
  'COLOR_GREEN' : "\033[32m",
  'COLOR_YELLOW' : "\033[33m",
  'COLOR_BLUE' : "\033[34m",
  'COLOR_MAGENTA' : "\033[35m",
  'COLOR_CYAN' : "\033[36m"
}

BACKGROUNDS_DICT = {
  "BACKGROUND_RED": f"\x1b[41m{TEXT_BLACK}",
  "BACKGROUND_GREEN": f"\x1b[42m{TEXT_BLACK}",
  "BACKGROUND_YELLOW": f"\x1b[43m{TEXT_BLACK}",
  "BACKGROUND_BLUE": f"\x1b[44m{TEXT_BLACK}",
  "BACKGROUND_MAGENTA": f"\x1b[45m{TEXT_BLACK}",
  "BACKGROUND_CYAN": f"\x1b[46m{TEXT_BLACK}",
  "BACKGROUND_WHITE": f"\x1b[47m{TEXT_BLACK}"
}

STYLES_DICT = {
  "STYLE_BOLD": "\033[1m",
  "STYLE_ITALIC": "\x1b[3m",
  "STYLE_UNDERLINE": "\033[4m",
  "STYLE_BLINK": "\033[5m",
  "STYLE_STRIKETHROUGH": "\x1b[9m",
  "STYLE_HIDDEN": "\x1b[8m"
}

def show_emojis():
  print(f'Available emojis:')
  for name, emoji in EMOJIS_DICT.items():
    print(f'  >> {name}: {emoji}')

def show_colors():
  print(f'Available colors:')
  for name, color in COLORS_DICT.items():
    print(f'  >> {color}{name}{RESET}')

def show_backgrounds():
  print(f'Available backgrounds:')
  for name, background in BACKGROUNDS_DICT.items():
    print(f'  >> {background}{name}{RESET}')

def show_styles():
  print(f'Available styles:')
  for name, style in STYLES_DICT.items():
    print(f'  >> {style}{name}{RESET}')

def show_usage():
  print(f"===== [{EMOJI_BEGIN}User Guide{EMOJI_BEGIN}] =====")
  print("1. Import the emojis or colors:")
  print("   `from pwnwas_emoji import emojis, colors`")
  print("2. Use emojis in print statements:")
  print("   `print(f'{EMOJI_WARNING} Warning message')`")
  print(f"   >> {EMOJI_WARNING} Warning message")
  print("3. Use colors:")
  print("   `print(f'{COLOR_RED}{EMOJI_WARNING}Error message{RESET}')`")
  print(f"   >> {COLOR_RED}{EMOJI_ERROR} Error message{RESET}")

def find_emoji(keyword: str):
  """
  This function is used to find an emoji according to the keyword
  """
  found = -1
  print(f"Searching for emojis containing: {keyword}")
  for name, emoji in EMOJIS_DICT.items():
    if keyword.lower() in name.lower():
      print(f'{name}: {emoji}')
      found = 1
  
  if found == -1:
    print(f'{COLOR_RED}[{EMOJI_ERROR}] No emoji(s) found!{RESET}')

def help_me():
  print(f'There are some "helper" functions that you can call')
  print(f"""Try:
    `show_emojis()`,
    `show_colors()`, 
    `show_backgrounds()`, 
    `show_styles()`,
    `show_usage(),
    `find_emoji(keyword)`
  """)

def max_verstappen():
  print(f"{BACKGROUND_RED}          {RESET}")
  print(f"{BACKGROUND_WHITE}          {RESET}")
  print(f"{BACKGROUND_BLUE}          {RESET}")

def cyka_blyat():
  print(f"{BACKGROUND_WHITE}          {RESET}")
  print(f"{BACKGROUND_BLUE}          {RESET}")
  print(f"{BACKGROUND_RED}          {RESET}")

def bomboclat():
  print(f"{BACKGROUND_GREEN}   {RESET}{BACKGROUND_WHITE}    {RESET}{BACKGROUND_GREEN}   {RESET}")
  print(f"{BACKGROUND_GREEN}   {RESET}{BACKGROUND_WHITE}    {RESET}{BACKGROUND_GREEN}   {RESET}")
  print(f"{BACKGROUND_GREEN}   {RESET}{BACKGROUND_WHITE}    {RESET}{BACKGROUND_GREEN}   {RESET}")

def bonjour():
  print(f"{BACKGROUND_BLUE}  ", end="");print(f"{BACKGROUND_WHITE}  ", end="");print(f"{BACKGROUND_RED}  ", end="")
  print(f"{BACKGROUND_BLUE}  ", end="");print(f"{BACKGROUND_WHITE}  ", end="");print(f"{BACKGROUND_RED}  ", end="")
  print(f"{BACKGROUND_BLUE}  ", end="");print(f"{BACKGROUND_WHITE}  ", end="");print(f"{BACKGROUND_RED}  ", end="")

def konnichiwa():
  print(f"{BACKGROUND_WHITE}           {RESET}")
  print(f"{BACKGROUND_WHITE}    {RESET}", end="");print(f"{BACKGROUND_RED}   {RESET}", end="");print(f"{BACKGROUND_WHITE}    {RESET}")
  print(f"{BACKGROUND_WHITE}           {RESET}")

def india():
  print(f"{BACKGROUND_YELLOW}           {RESET}")
  print(f"{BACKGROUND_WHITE}    {RESET}", end="");print(f"{BACKGROUND_BLUE}   {RESET}", end="");print(f"{BACKGROUND_WHITE}    {RESET}")
  print(f"{BACKGROUND_GREEN}           {RESET}")

def sweden():
  print(f"{BACKGROUND_BLUE}   {RESET}{BACKGROUND_YELLOW}  {RESET}{BACKGROUND_BLUE}     {RESET}")
  print(f"{BACKGROUND_YELLOW}          {RESET}")
  print(f"{BACKGROUND_BLUE}   {RESET}{BACKGROUND_YELLOW}  {RESET}{BACKGROUND_BLUE}     {RESET}")

def austria():
  print(f"{BACKGROUND_RED}          {RESET}")
  print(f"{BACKGROUND_WHITE}          {RESET}")
  print(f"{BACKGROUND_RED}          {RESET}")


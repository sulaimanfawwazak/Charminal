# pwnwas_emoji.py

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

# ANSI escape codes for text styles
STYLE_BOLD = "\033[1m"
STYLE_UNDERLINE = "\033[4m"

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

STYLES_DICT = {
  STYLE_BOLD : "\033[1m",
  STYLE_UNDERLINE : "\033[4m"
}

def show_emojis():
  print(f'Available emojis:')
  for name, emoji in EMOJIS_DICT.items():
    print(f'{name}: {emoji}')

def show_colors():
  print(f'Available colors:')
  for name, color in COLORS_DICT.items():
    print(f'{color}{name} COLOR{RESET}')

def show_styles():
  print(f'Available styles:')
  for name, style in STYLES_DICT:
    print(f'{style}{name}{RESET}')

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
    `show_styles()`,
    `show_usage(),
    `find_emoji(keyword)`
  """)
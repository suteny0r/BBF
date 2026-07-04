"""Startup banner: prints the project's ASCII art logo in red, with the
tool's title underneath, once per invocation."""

# ANSI color codes. RESET must follow any RED-wrapped text so it doesn't
# bleed into whatever the CLI prints next.
_RED = "\033[31m"
_RESET = "\033[0m"

_LOGO = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠶⠒⠒⠲⠶⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡾⠁⠀⡠⠀⠀⠀⠀⠀⣠⡴⢾⡉⠉⠁⠀⠀⣠⠤⣄⠀⠀⢈⣻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡷⠴⠾⢧⣀⢀⣀⣴⣞⠻⠗⢠⠇⠀⠀⣰⣿⠁⠀⠘⣆⠀⠈⠻⣝⠃⠀⣠⠖⠋⣛⢢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⠛⠒⣄⠤⠄⢻⠉⠁⠈⠊⠑⠊⠁⠀⠀⢰⡇⢧⠀⠀⠀⢹⡀⠀⠀⠈⢷⣼⠁⡴⠋⠁⠹⣿⠀⠀⠀⠀⠀⠀⠀
⣼⠁⠀⠀⠈⠐⠢⡈⢙⣛⡓⠲⠶⣖⡆⠀⠀⢸⠃⠈⢳⠀⠀⢸⢹⡄⠀⠀⡼⢠⠘⡇⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀
⣯⠀⠀⠀⢀⡤⠖⣉⣠⣔⡚⠉⠉⠁⠀⠀⠀⢸⡀⠀⠈⡇⠀⢸⣨⣇⣠⡞⠁⠀⠓⡏⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀
⢹⡄⠀⢸⠵⠖⠛⣏⠀⠀⠀⠁⠀⠀⠀⠀⠀⢀⣷⠴⠚⣷⠀⣾⠉⠉⠉⠉⠛⠲⢶⠃⠀⣸⣿⣠⠖⠛⠛⠽⠷⢦⡀
⠀⠙⢦⣸⡀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⣠⡞⠉⠀⠀⠀⢸⢀⡇⠀⠀⠀⠀⠀⠀⡞⠀⡴⠻⣏⠀⡔⠀⡴⠚⠛⢦⣷
⠀⠀⠀⠈⠁⠀⢰⡇⠀⠀⠀⠀⠀⢠⣾⣟⠀⠀⠀⠀⠀⢸⣼⠁⠀⠀⠀⠀⠀⣸⢁⠞⠁⢀⢼⣷⡇⠀⡇⠀⠀⣸⠇
⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⣰⠏⣽⢎⢄⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⢰⣷⡋⠤⣒⡵⣫⠞⢻⡴⠃⢀⡴⠃⠀
⠀⠀⠀⠀⢀⡾⠁⢀⣠⠾⡆⢠⠇⠀⠕⡷⣇⠇⠆⡄⡄⡀⢠⠠⡀⢄⠰⡄⣙⢦⠼⡎⠃⠃⠃⣠⢞⣡⣴⠋⠀⠀⠀
⠀⠀⠀⠀⠾⠗⠚⠋⠁⠀⠻⣾⠀⠀⠈⠘⢡⢋⡗⡳⢳⠞⡼⢲⢓⡞⢹⢉⡇⠸⠀⠁⠀⠀⠚⠛⠉⠈⣇⠙⠶⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠈⠀⠁⠋⠘⠀⠃⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠴⠛⠒⢀⠈⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠖⠛⢓⣄⡷⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡤⠖⠋⠁⢀⣠⠾⠞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⣹⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⢾⡼⡄⣇⣎⣰⣠⠆⣠⡟⠀⢠⠀⡀⡀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡷⣬⡈⠁⠁⠑⠘⡼⢣⠏⡓⡳⢺⢴⢵⣡⣐⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⡽⢶⣤⣠⠞⢁⡞⠀⠀⠀⠀⣁⣡⡽⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣞⠀⠛⠉⠀⣠⠞⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢤⣤⡤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

TITLE = "BBF -- BD_ADDR(UAP) Brute-Forcer"


def print_banner():
    """Print the logo in red with the tool title beneath it.

    Uses raw ANSI escapes rather than a dependency like colorama since
    the rest of the tool has no third-party runtime deps; on terminals
    that don't support ANSI (or when stdout isn't a tty) the escape
    codes are simply invisible/no-ops around plain text.
    """
    print(f"{_RED}{_LOGO}{TITLE}{_RESET}")

import os
import sys


def main():
    """Run administrative tasks."""
    # Green color ANSI escape code
    GREEN = "\033[92m"
    RESET = "\033[0m"
    
    print(f"{GREEN}")
    print(r"""
    ____      ______ _____ ____ 
   / __ \__  /__  /|__  /|  _ \
  / /_/ / / / / / /  /_ < | |_) |
 / ____/ /_/ / / /____/ / |  _ < 
/_/    \__, / /____/____/ |_| \_\
      /____/                     
    """)
    print("    pyz3r | 2026 | Algebra")
    print(f"{RESET}")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offers_calculator.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

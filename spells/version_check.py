"""Check running version of Python against a minimum version value.
    https://github.com/pypa/get-pip"""

import sys


def version_check(min_version_tuple):
    """Check running version of Python against a minimum version value."""
    output = None

    this_python = sys.version_info[:2]
    if this_python < min_version_tuple:
        message_parts = [
            f"This script does not work on Python {this_python[0]}.{this_python[1]}",
            "The minimum supported Python version is " + 
                f"{min_version_tuple[0]}.{min_version_tuple[1]}.",
        ]
        output = "ERROR: " + " ".join(message_parts)

    return output


def main(message):
    """Print message if there is one, otherwise do the thing."""
    if message:
        print(message)
        sys.exit(0)
    else:
        print("Version checks out. Doing the thing." + "\n")


min_version = (3, 7)
print(f"Checking for version {min_version}")
main(version_check(min_version))

min_version = (3, 99)
print(f"Checking for version {min_version}")
main(version_check(min_version))

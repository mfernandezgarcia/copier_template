from copier import run_copy
import os

# Option 1: Use home directory
destination = os.path.expanduser("./copier-destination")

# Or Option 2: Use current working directory
# destination = os.path.join(os.getcwd(), "copier-destination")

run_copy("https://github.com/copier-org/copier.git", destination)

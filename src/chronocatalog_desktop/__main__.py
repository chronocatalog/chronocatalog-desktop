import sys

from chronocatalog_desktop.app import main

# Guarded because parallel hashing uses spawn-based worker processes,
# which re-import the main module (see chronocatalog.hashing).
if __name__ == "__main__":
    sys.exit(main())

import runpy
import sys

import localizer

localizer.install()
runpy.run_path(sys.argv[1], run_name="__main__")
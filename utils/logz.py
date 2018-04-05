


import os
import shutil
import glob
from utils import *

def configure_log_dir(logname, name, copy = True):
	"""
	Set output directory to d, or to /tmp/somerandomnumber if d is None
	"""

	path = os.path.join(log_dir(), logname, name)
	os.makedirs(path)  # create path
	if copy:
		filenames = glob.glob('*.py')  # put copy of all python files in log_dir
		for filename in filenames:  # for reference
			shutil.copy(filename, path)
	return path
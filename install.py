import os
import shutil

# Script to install the generator.
# Simply a copy of the install script I made for yeoman-wordpress (https://github.com/romainberger/yeoman-wordpress)

generatorPath = '/usr/local/lib/node_modules/yeoman/node_modules/yeoman-generators/lib/generators'
currentDir = os.path.dirname(os.path.abspath(__file__))
yeomanFlaskPath = os.path.join(generatorPath, 'yeoman-flask')

# Check if Yeoman is installed
if not os.path.isdir(generatorPath):
	print 'It seems that Yeoman is not installed.'
	print 'If you have trouble installing the generator please refer to the install instructions in the Readme.'
	os.exit()

# if the generator is already installed we remove it to avoid errors
if os.path.isdir(yeomanFlaskPath):
	shutil.rmtree(yeomanFlaskPath)
try:
	shutil.copytree(currentDir, yeomanFlaskPath)
	print '\033[32mGenerator installed successfully.\033[37m\n'
except :
	print 'Oops, something went wrong, sorry'
	print 'If you have trouble installing the generator please refer to the install install instructions in the Readme.'
	raise
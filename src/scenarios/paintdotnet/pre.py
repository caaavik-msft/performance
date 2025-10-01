'''
pre-command
'''
import zipfile
from performance.logger import setup_loggers
from os.path import dirname
from shared.precommands import PreCommands
from shared import const
from logging import getLogger
from shutil import rmtree

setup_loggers(True)

precommands = PreCommands()

output = precommands.output or const.PUBDIR
with zipfile.ZipFile(precommands.pathtozip, 'r') as publish:
    publish.extractall(output)
rmtree(dirname(precommands.pathtozip))
getLogger().info(f"Unpacked {precommands.pathtozip} into {output}.")
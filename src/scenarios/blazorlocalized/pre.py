'''
pre-command
'''
from performance.logger import setup_loggers
from shared.precommands import PreCommands

setup_loggers(True)
precommands = PreCommands()
precommands.uninstall_workload("wasm-tools")
precommands.existing("src", "BlazorLocalized.sln")
precommands.execute()

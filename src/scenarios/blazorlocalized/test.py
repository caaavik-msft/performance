'''
Localized Blazor Wasm Template
'''
from shared.runner import TestTraits, Runner

EXENAME = 'blazorlocalized'

if __name__ == "__main__":
    traits = TestTraits(exename=EXENAME,
                        guiapp='false'
                        )
    Runner(traits).run()

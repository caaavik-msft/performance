from shared.runner import TestTraits, Runner

EXENAME = 'WinformsNetCorePerfApp1'

def main():
    traits = TestTraits(exename=EXENAME,
                        guiapp='true',
                        startupmetric='GenericStartup',
                        timeout=30,
                        measurementdelay='6',
                        runwithoutexit='false',
                        processwillexit="false",
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()

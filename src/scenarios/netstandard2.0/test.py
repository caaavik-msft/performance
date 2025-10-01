from shared.runner import TestTraits, Runner

EXENAME = 'NetCoreApp(Library)'

def main():
    traits = TestTraits(exename=EXENAME,
                        guiapp='false', 
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()

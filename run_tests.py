def main():
    import unittest

    from wiktionary_stardict.mathjax import shutdown_deno, start_deno

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests")
    runner = unittest.TextTestRunner(buffer=True)
    start_deno()
    result = runner.run(suite)
    shutdown_deno()
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    import sys

    sys.exit(main())

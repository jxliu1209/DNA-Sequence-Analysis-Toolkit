"""Basic package import checks."""


def test_package_imports() -> None:
    import dna_toolkit

    assert dna_toolkit.__version__ == "0.1.0"

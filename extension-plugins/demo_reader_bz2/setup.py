import setuptools

setuptools.setup(
    name="demo_reader_bz2",
    version="0.0.0",
    description="demo reader plugin for reading bz2 files",
    package_dir={"": "src"},
    entry_points={
        "demo_reader.compression_plugins": [
            "bz2 = demo_reader_bz2.bzipped"
        ]
    }
)
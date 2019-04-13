import setuptools

setuptools.setup(
    name="demo_reader_gzip",
    version="0.0.0",
    description="demo reader plugin for reading gzip files",
    package_dir={"": "src"},
    entry_points={
        "demo_reader.compression_plugins": [
            "gzip = demo_reader_gzip.gzipped"
        ]
    }
)
import gzip
from demo_reader.util import writer

extension = ".gzip"
opener = gzip.open

if __name__ == "__main__":
    writer.main(opener)

from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def write_data(self, data):
        print(f"FileDataSource: Writing {data}...")

    def read_data(self):
        print("FileDataSource: Reading...")


class DataSourceDecorator(DataSource):

    def __init__(self, source: DataSource):
        self.wrappee = source

    def write_data(self, data):
        self.wrappee.write_data(data)

    def read_data(self):
        return self.wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):

    def write_data(self, data):
        print(f"EncryptionDecorator: Encrypting {data}...")

    def read_data(self):
        print("EncryptionDecorator: Decrypting...")


class CompressionDecorator(DataSourceDecorator):

    def write_data(self, data):
        print(f"CompressionDecorator: Compressing {data}...")

    def read_data(self):
        print("CompressionDecorator: Decompressing...")


class Application:

    def run(self):
        source = FileDataSource("somefile.txt")
        source.write_data("hello")

        source = CompressionDecorator(source)
        source.write_data("hello2")

        source = EncryptionDecorator(source)
        source.write_data("hello3")


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()

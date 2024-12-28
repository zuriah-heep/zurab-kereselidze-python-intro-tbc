from datetime import datetime
from time import sleep

class TimestampMixin:
    def __init__(self):
        self._creation_time = datetime.now()
        self._modification_time = self._creation_time

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time


class File(TimestampMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self._modification_time = datetime.now()


class User(TimestampMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self._modification_time = datetime.now()


# Example Usage
def main():
    file = File("file.txt")
    print("\nCreated file", file.name)
    print("Creation time:", file.get_creation_time())
    print("Modification time:", file.get_modification_time())

    sleep(1)
    file.name = "new_file.txt"
    print("\nModified file name:", file.name)
    print("Creation time:", file.get_creation_time())
    print("Modification time:", file.get_modification_time())

    sleep(1)
    user = User("zuriah-heep")
    print("\nCreated user", user.name)
    print("Creation time:", user.get_creation_time())
    print("Modification time:", user.get_modification_time())

    sleep(1)
    user.name = "zukaka"
    print("\nModified user name:", user.name)
    print("Creation time:", user.get_creation_time())
    print("Modification time:", user.get_modification_time())

if __name__ == "__main__":
    main()

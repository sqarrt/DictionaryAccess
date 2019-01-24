class DictionaryAccess:
    def __init__(self, data):
        super().__init__()
        self.__data = data
        try:
            for a in self.__data.keys():
                if isinstance(self.__data[a], dict):
                    self.__data[a] = DictionaryAccess(self.__data[a])
        except AttributeError:
            pass

    def __getattr__(self, item):
        return self.__data[str(item)]

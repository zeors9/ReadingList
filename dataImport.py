import pandas as pd


class DataImporter:
    __data__ = pd.DataFrame()
    def __init__(self, file_path):
        self.file_path = file_path

    def __load_data__(self):
        try:
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
    def __clean_data__(self, data):
        data = data.copy(deep=True)
        data['AuthorNames'] = data['AuthorNames'].str.split('|', expand=False)
        data['TagNames'] = data['TagNames'].str.split('|', expand=False)
        data.rename(columns={'TitleName': 'Title', 'AuthorNames': 'Authors', 'URLString':'URL', 'TypeName':'Media', 'TagNames': 'Tags'}, inplace=True)
        return data
    def load(self):
        self.__data__ = self.__load_data__()
        #self.__data__ = self.__clean_data__(self.__data__)
        #return self.__data__
        return self.__clean_data__(self.__data__)

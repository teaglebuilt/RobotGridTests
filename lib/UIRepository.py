import yaml


class Repository(object):

    def __init__(self, repository_path, delimiter='.'):
        self._repo_path = repository_path
        self._delimiter = delimiter
        self._repo = self._parse_repository(self._repo_path)

    def _parse_repository(self, repository_path):
        with open(repository_path, 'r') as fp:
            repo = yaml.load(fp)
        return repo

    def _parse_item_into_selectors(self, selector):
        return selector.split(self._delimiter)

    def __getitem__(self, item_selector):
        if len(item_selector) <= 0:
            raise Exception('Item selector is empty!')
        item = self._repo
        selectors = self._parse_item_into_selectors(item_selector)
        while len(selectors) > 0:
            item = item[selectors.pop(0)]
        if type(item) == dict and 'x' not in item.keys():
            raise Exception('Item "{}" does not contain XPath selector!'
                .format(item_selector))
        if type(item) == str:
            return item
        return item['x']

class UIRepository:
    @classmethod
    def load_repository(cls, repository_path):
        '''Creates instance of repository class'''
        return Repository(repository_path)
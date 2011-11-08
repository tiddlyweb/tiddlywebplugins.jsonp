"""
JSONP serialization for TiddlyWeb.

If callback is in tiddlyweb.query on a request that
would otherwise be JSON, send the results as JSONP,
otherwise, do the normal JSON results.
"""


from tiddlyweb.serializations.json import Serialization as JSON

SERIALIZERS = {
        'application/json': ['tiddlywebplugins.jsonp',
            'application/json; charset=UTF-8'],
        }


def init(config):
    """
    Update serializers configuration to include this one.
    """
    config['serializers'].update(SERIALIZERS)


class Serialization(JSON):
    """
    Subclass the core tiddlyweb.serializations.json to add support
    for JSONP. If there is a callback in the query_string then the
    outgoing JSON will be wrapped in a function with the value of
    the callback.
    """

    def _get_jsonp(self):
        """
        Determine if JSONP is requested.
        """
        jsonp = self.environ['tiddlyweb.query'].get('callback', [None])[0]
        if jsonp:
            return '%s(' % jsonp, ')'
        else:
            return '', ''

    def list_recipes(self, recipes):
        """
        Provide a list, wrapped in a JavaScript function named
        by callback, of recipes.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.list_recipes(self, recipes) + suffix

    def list_bags(self, bags):
        """
        Provide a list, wrapped in a JavaScript function named
        by callback, of bags.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.list_bags(self, bags) + suffix

    def list_tiddlers(self, bag):
        """
        Provide a list, wrapped in a JavaScript function named
        by callback, of tiddlers.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.list_tiddlers(self, bag) + suffix

    def recipe_as(self, recipe):
        """
        Provide a dictionary representing a recipe, wrapped in a
        JavaScript function named by callback.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.recipe_as(self, recipe) + suffix

    def bag_as(self, bag):
        """
        Provide a dictionary representing a bag, wrapped in a
        JavaScript function named by callback.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.bag_as(self, bag) + suffix

    def tiddler_as(self, tiddler):
        """
        Provide a dictionary representing a tiddler, wrapped in a
        JavaScript function named by callback.
        """
        prefix, suffix = self._get_jsonp()
        return prefix + JSON.tiddler_as(self, tiddler) + suffix

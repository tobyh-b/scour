"""

"""

import os
import sys
import json
import factories


# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
class Scour(factories.Factory):
    """
    This class gives access to the asset types within the scope of scour.
    
    Use example:
    
    ..code-block:: python
        
        >>> import scour
        >>>
        >>> # -- Instance scour - which will register any default
        >>> # -- plugins
        >>> scour_inst = scour.Scour()
        >>>
        >>> # -- Cycle over all the asset types available
        >>> for asset_type in scour_inst.factory.available():
        >>>     asset = scour_inst.factory.get(asset_type)
        >>>     
        >>>     # -- get dependency data
        >>>     asset_data = asset().dependencies()
    
    """

    # --------------------------------------------------------------------------
    # noinspection PyUnusedLocal
    def __init__(self, *args, **kwargs):

        # -- This property holds the instance of the represented file
        self.instance = None

        # -- This property holds the data gathered from the represented file
        self.data = dict(
            (key, list())
            for key in ['dependencies', 'metadata']
        )

        # -- This property holds all logging for the instance
        self.messages = ScourMessages()

        # -- get any passed search paths
        self.search_paths = kwargs.pop(
            'search_paths',
            [],
        )
        
        # -- Initiate the factory
        super(Scour, self).__init__(
            abstract=ScourPlugin,
            plugin_identifier='Name',
            versioning_identifier='Version',
            paths=paths,
        )


# ------------------------------------------------------------------------------
class ScourPlugin(object):
    """
    This is a plugin abstract of a represented file
    """

    # -- unique name which allows the plugin to be differentiated
    # -- from any other plugins of the same type.
    Name = None

    # -- Version for plugin hierarchies
    Version = 1

    # --------------------------------------------------------------------------
    def __init__(self, locator, *args, **kwargs):

        # -- This is the container for our per-instance options
        self.options = attrdict.AttrDict()

        # -- This property holds log info to report
        self.messages = ScourPluginMessages()

        self.locator = locator

    # --------------------------------------------------------------------------
    @classmethod
    def viable(cls, locator):
        """
        Opportunity to specify prerequisites for the plugin
        Validates environment, software

        :param locator: full file path
        :type locator: string
        
        :return: result
        :rtype: bool
        """
        
        return True

    # --------------------------------------------------------------------------
    def dependencies(self,  locator):
        """
        Get dependencies of passed locator.

        :param locator: full file path
        :type locator: string
        
        :return: files referenced from within the locator
        :rtype: list
        """
        
        return list()

    # --------------------------------------------------------------------------
    def metadata(self,  locator):
        """
        Get metadata of passed locator.

        :param locator: full file path
        :type locator: string
        
        :return: data gathered from locator
        :rtype: dict
        """
        
        return dict()


# ------------------------------------------------------------------------------
class ScourPluginMessages(object):

    def __init__(self):
        self.viability = list()
        self.execution = list()

from abc import ABC, abstractmethod


class scraperInterface(ABC):
    """
    Defines a list of methods a scraper for a grocery store should contain
    """

    @abstractmethod
    def getGroceryPrice(grocery):
        pass
    
    @abstractmethod
    def getGroceryInfo(grocery):
        pass
    

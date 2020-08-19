import dependency_injector.containers as containers
import dependency_injector.providers as providers

from .tag_list import TagListField

from ..parsers import Parsers


class Fields(containers.DeclarativeContainer):

    TagList = providers.Factory(TagListField, Parsers.tags_str)

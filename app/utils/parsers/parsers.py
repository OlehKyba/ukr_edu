import dependency_injector.containers as containers
import dependency_injector.providers as providers

from .tags_to_str import TagsStrParser


class Parsers(containers.DeclarativeContainer):

    tags_str = providers.Factory(TagsStrParser)

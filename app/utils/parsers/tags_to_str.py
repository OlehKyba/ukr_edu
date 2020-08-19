from app.models import get_or_create, Tag


class TagsStrParser:

    def parse(self, data):
        values = data.split(',')
        tag_list = [get_or_create(Tag, value=value) for value in values]
        return tag_list

    def stringify(self, tag_list):
        values = [tag.value for tag in tag_list]
        return ','.join(values)
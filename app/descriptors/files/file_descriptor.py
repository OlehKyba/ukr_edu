from werkzeug.utils import secure_filename


class FileDescriptor():

    def __init__(self, strategy, **kwargs):
        self.name = kwargs.get('name')
        self.name_from = kwargs.get('name_from')
        self.strategy = strategy

    def __set_name__(self, owner, name):
        if not self.name:
            self.name = '_' + name

    def __get__(self, instance, owner):

        filename = getattr(instance, self.name)

        if not filename:
            return filename

        result = self.strategy.get_file_link(filename)

        return result

    def __set__(self, instance, file):

        if self.name_from:
            filename = getattr(instance, self.name_from)
            extention = file.filename.split('.')[-1]
            filename = '.'.join([filename, extention])
        else:
            filename = file.filename

        filename = secure_filename(filename)

        if getattr(instance, self.name):
            self.__delete__(instance)

        self.strategy.save_file(file, filename)
        setattr(instance, self.name, filename)

    def __delete__(self, instance):

        filename = getattr(instance, self.name)
        setattr(instance, self.name, None)
        self.strategy.delete_file(filename)

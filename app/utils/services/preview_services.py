

class PreviewService:

    def __init__(self, s3):
        self.storage = s3

    def link(self, filename=None):
        link = f'http//:{self.storage.name}.s3.amazonaws.com'
        if filename:
            link += f'/{filename}'
        return link

    def upload_file(self, file, filename):
        response = self.storage.put_object(Key=filename, Body=file)
        return response

    def delete_file(self, filename):
        response = self.storage.Object(filename).delete()
        return response

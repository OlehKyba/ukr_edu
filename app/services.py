from .settings import *
from .utils import di_config
from .utils.services import Services

di_config.update({
    'aws': {
        'preview_bucket': S3_IMG_BUCKET
    }
})

preview_storage = Services.preview()

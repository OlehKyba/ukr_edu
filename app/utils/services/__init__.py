from .preview_services import PreviewService
from ..storage import Storage

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Services(containers.DeclarativeContainer):

    preview = providers.Factory(PreviewService, s3=Storage.s3_preview_bucket)

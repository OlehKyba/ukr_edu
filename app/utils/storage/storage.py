import dependency_injector.containers as containers
import dependency_injector.providers as providers

import boto3

from .. import di_config


class Storage(containers.DeclarativeContainer):

    s3_preview_bucket = providers.ThreadSafeSingleton(boto3.resource('s3').Bucket, di_config.aws.preview_bucket)

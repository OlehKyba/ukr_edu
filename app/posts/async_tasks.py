from app.extentions import db, celery
from app.services import preview_storage
from app.models import Post, File, FileTypes


@celery.task()
def upload_post_preview(post_id, file, file_extension, file_name=None):

    post = Post.query.get(post_id)

    file_name = file_name or f'{post.slug}.{file_extension}'
    preview_storage.upload_file(file, file_name)

    if post.image:
        post.image.name = file_name
        post.image.path = preview_storage.link()
    else:
        post.image = File(
            name=file_name,
            description=f'Preview for post: "{post.title}".',
            path=preview_storage.link(),
            file_type=FileTypes.post_preview,
        )

    db.session.add(post)
    db.session.commit()

from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse

from ella.photos.models import Photo, Format
from ella.core.cache.utils import get_cached_object


def format_photo_json(request, photo, format):
    "Used in admin image 'crop tool'."
    try:
        photo = get_cached_object(Photo, pk=photo)
        format = get_cached_object(Format, pk=format)
        content = {
            'error': False,
            'image':settings.MEDIA_URL + photo.image,
            'width':photo.width,
            'height': photo.height,
            'format_width':format.max_width,
            'format_height':format.max_height
}
    except (Photo.DoesNotExist, Format.DoesNotExist):
        content = {'error':True}
    return HttpResponse(simplejson.dumps(content))

import magic

def get_mimetype(fobject):
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype

def valid_image_mimetype(fobject):
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False

MAX_SIZE = 2048000  #2mb

def valid_image_size(image, max_size=MAX_SIZE):
    image_size = len(image)
    if image_size > max_size:
        return False
    else:
        return True
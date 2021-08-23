from imgurpython import ImgurClient


def get_album_images(album_id, client_id=None, client_secret=None):
    client = ImgurClient(client_id, client_secret)
    album = client.get_album(album_id)
    images = album.__dict__["images"]
    extract_fields = ["description", "width", "height", "link"]
    images = [{field: image.get(field) for field in extract_fields} for image in images]
    return images

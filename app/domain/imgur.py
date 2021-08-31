from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError, ImgurClientRateLimitError


def get_album_images(album_id, client_id=None, client_secret=None):
    client = ImgurClient(client_id, client_secret)

    try:
        album = client.get_album(album_id)
    except (ImgurClientError, ImgurClientRateLimitError):
        return []

    images = album.__dict__["images"]
    extract_fields = ["description", "width", "height", "link"]
    images = [{field: image.get(field) for field in extract_fields} for image in images]
    return images

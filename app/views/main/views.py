from flask import render_template

from app.models.main import MainPage, SocialMedia

def index():
    content = MainPage.objects.first()
    social_media = SocialMedia.objects.filter(active=True)
    return render_template(
        "index.html", 
        content=content, 
        social_media=social_media
    )

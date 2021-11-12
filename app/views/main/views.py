from flask import render_template

from app.models.main import MainPage, SocialMedia

def index():
    content = MainPage.objects.first()
    social_media = SocialMedia.objects.all()
    return render_template(
        "index.html", 
        content=content, 
        social_media=social_media
    )

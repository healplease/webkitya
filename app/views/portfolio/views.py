from flask import render_template

from app.models.portfolio import PortfolioImage, PortfolioPage

def portfolio():
    content = PortfolioPage.objects.first()
    images = PortfolioImage.objects.filter(active=True)
    return render_template(
        "portfolio.html", 
        content=content, 
        images=list(images)
    )

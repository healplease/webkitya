from flask import render_template, url_for, redirect

from app.views.commissions.forms import ContactUsForm
from app.models.commissions import CommissionsPage

def commissions():
    contact_form = ContactUsForm()
    if contact_form.validate_on_submit():
        return redirect(url_for("commissions.commissions"))

    content = CommissionsPage.objects.first()
    return render_template(
        "commissions.html",
        content=content,
        form=contact_form
    )

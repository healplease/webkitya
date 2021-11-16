from flask import render_template, url_for, redirect, flash, request

from app.domain.email import send_mail
from app.views.commissions.forms import ContactUsForm
from app.models.commissions import CommissionsPage

def commissions():
    form = ContactUsForm()
    if form.validate_on_submit():
        success = send_mail(form.contact.data, form.subject.data, form.body.data)
        if success:
            flash("Your message was successfully sent!", category="success")
        else:
            flash("Your message wasn't sent. Try again later.", category="danger")
        return redirect(url_for("commissions.commissions"))

    content = CommissionsPage.objects.first()
    return render_template(
        "commissions.html",
        content=content,
        form=form
    )

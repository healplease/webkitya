import traceback

from flask import render_template, url_for, redirect, flash, request

from app.domain.email import send_mail
from app.views.commissions.forms import ContactUsForm
from app.models.commissions import CommissionsPage

def commissions():
    form = ContactUsForm()

    if form.validate_on_submit():
        try:
            send_mail(form.contact.data, form.subject.data, form.body.data, request.files.getlist("references"))
            flash("Your message was successfully sent!", category="success")
        except Exception:
            flash("Your message wasn't sent. Try again later.", category="danger")
            traceback.print_exc()
        return redirect(url_for("commissions.commissions"))

    content = CommissionsPage.objects.first()
    return render_template(
        "commissions.html",
        content=content,
        form=form
    )

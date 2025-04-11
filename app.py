from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

@app.route('/contact_form')
def contact_form():
    return render_template_string('contact_form.html')

@app.route('/submit',method='POST')
def submit():
    name=request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    custom_subject = request.form.get('custom_subject')
    preferred_contact = request.form.get('preferred_contact')
    agreement = request.form.get('agreement')

    errors = []
    if not name or not email or not phone or not message:
        errors.append('Please fill all required forms')
    if not phone.isnumeric():
        errors.append('Phone number must be numeric')
    if subject == "other" and not custom_subject:
        errors.append('Please specify custom subject')
    if not agreement:
        errors.append('You must agree with the terms and conditions')

    if errors:
        return render_template('contact_form.html', errors=errors, form=request.form)
    subject=custom_subject if subject == 'Other' else subject
    return render_template('confirmation.html', name=name, email=email, phone=phone, message=message, subject=subject, preferred_contact=preferred_contact, agrrement="YES" if agreement else "NO")

if  __name__ == "__main__":
    app.run(debug=True)
from flask import render_template, request, flash
from .model import ContactForm
from app import app
from flask_mail import Message, Mail

mail = Mail()

@app.route('/', methods=['GET', 'POST'])
def index():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender='hnativ159@gmail.com', recipients=['dreee1998@gmail.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)

			return 'Form posted.'

	elif request.method == 'GET':
		return render_template('index.html', form=form)


mail.init_app(app)
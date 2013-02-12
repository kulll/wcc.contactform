from five import grok
from zope import interface
from Products.CMFCore.utils import getToolByName
from smtplib import SMTPException

grok.templatedir('templates')


class Index(grok.View):
    grok.require('zope2.View')
    grok.context(interface.Interface)
    grok.name('contact-wcc')
    grok.template('contact')

    def update(self):
        data = self.request.form
        import ipdb; ipdb.set_trace()
        if data:
            self.create_email(data)
            self.send_email()

    def send_email(self):
        mail_host = getToolByName(self.context, 'MailHost')

        # Send email
        try:
            mail_host.send(
                    self.message,
                    "anwarorchid88@gmail.com",
                    "anwarorchid88@gmail.com",
                    self.subject,
                    charset='utf-8'
                    )
        except SMTPException:
            raise SMTPException('Recipient address rejected by server')

    def create_email(self, data):
        email = data['email']
        name = data['name']
        city = data['city']
        country = data['country']
        phone = data['phone']
        original_message = data['message']
        self.subject = data['subject']

        self.message = """%s


        %s
        %s
        %s
        %s
        %s

        """ % (original_message, email, name, city, country, phone)

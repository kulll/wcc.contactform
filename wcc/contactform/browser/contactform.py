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

    def send_email(self):
        subject = "just a freakin subject"
        message = "i sent some shit"
        mail_host = getToolByName(self.context, 'MailHost')

        # Send email
        try:
            mail_host.send(
                    message,
                    "no-reply@oikoumene.org",
                    "no-reply@oikoumene.org",
                    subject,
                    charset='utf-8'
                    )
        except SMTPException:
            raise SMTPException('Recipient address rejected by server')

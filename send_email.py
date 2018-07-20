# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class Email(object):
    """发送邮件类

    :param username: 发送邮件的邮箱地址 必选 @type: str
    :param password: 发送邮件的邮箱密码 必选 @type: str
    :param to_username: 接受邮件的地址  必选 @type: str
    :param title: 发送邮件的邮箱密码 可选 @type: str
    :param content: 邮件正文部分 可选 @type: str
    :param fileobj: 文件对象 可选 @type: fileobject
    :param smtp_host: smtp服务器host 必选 @type: str
    :param smtp_port: smtp服务器port 必选 @type: int

    使用:
        Email(
            username="xxx", password="xxx", to_name="xxxx", title="this title"
            ).send_email()

    """

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if not getattr(self, "smtp_host", None):
            raise ValueError("smtp_hostparam missing!")
        if not getattr(self, "smtp_port", None):
            self.smtp_port = 25
        if not getattr(self, "to_username", None):
            raise ValueError("to_username param missing!")
        if not getattr(self, "password", None) or not getattr(self, "username", None):
            raise ValueError("username or password param missing!")
        if getattr(self, "fileobj", None):
            if self.fileobj.mode != "rb":
                raise IOError("fileobj need 'rb' mode, not '{}' mode".format(self.fileobj.mode))

    def _login_by_smtp(self):
        """连接并登陆smtp服务器

        :return: SMTP连接对象
        """
        smtpserver = smtplib.SMTP(host=self.smtp_host, port=self.smtp_port)
        smtpserver.login(self.username, self.password)
        return smtpserver

    def _build_message(self):
        msg = MIMEMultipart()
        msg["Subject"] = getattr(self, "title", "")
        msg["From"] = self.username
        msg["To"] = self.to_username
        if getattr(self, "content", None):
            msg.attach(MIMEText(self.content))
        if getattr(self, "fileobj", None):
            part = MIMEApplication(self.fileobj.read())
            part.add_header(
                'Content-Disposition', 'attachment',
                filename=("utf-8", "", os.path.basename(self.fileobj.name)))
            msg.attach(part)
        return msg

    def send_email(self):
        smtp_server = self._login_by_smtp()
        msg = self._build_message()
        smtp_server.sendmail(self.username, self.to_username, msg.as_string())


import feedparser
import datetime
import dateutil.parser
import os
import sendgrid
from fabric.api import task

@task
def check_github_dev_blog():
	github_developer_url = "https://developer.github.com/changes.atom"
	feed = feedparser.parse( github_developer_url )

	today = datetime.datetime.today().date()

	def contains_keywords( keywords , text ):
		for keyword in keywords:
			if keyword in text:
				return True
		return False

	def sendEmail ( link ):
		sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'))
		message = sendgrid.Mail()
		message.add_to('gtaylor@atlassian.com')
		message.set_subject('GitHub developer blog alert')
		message.set_text(link)
		message.set_from('GitHub developer blog alerts')
		status, msg = sg.send(message)

		
	fn = os.path.join(os.path.dirname(__file__), 'keywords.txt')

	with open(fn) as f:
	    keywords = f.read().splitlines()

	for item in feed["items"]:
		if dateutil.parser.parse(item["date"]).date() == today:
			if contains_keywords(keywords, item["summary"]):
				sendEmail(item["link"])




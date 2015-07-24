# GitHubApiChangeMonitor

This is a script for a simple rss feed monitor. I looks at each days entries and sends you an email if it contain
any of the words in keywords.txt.

I am using a heroku addon to send the email and to take care of running it reguarily.
Assuming you have a heroku account and the heroku toolbelt installed, you can get it running with the following

create a new heroku app

`heroku create` 


add the scheduler addon

`heroku addons:create scheduler`

add the sendgrid addon, this sets the sendmail username/password config vars
`heroku addons:create sendgrid:starter`

set the recipient email address as a config var
`heroku config:set EMAIL_ADDRESS= $YOUR_EMAIL_ADDRESS_HERE`

push the app to heroku
`git push heroku master`


Then it just a matter of going into the scheduler via the ui or the console and adding

`fab check_github_dev_blog`

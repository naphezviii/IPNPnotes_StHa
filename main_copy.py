#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import cgi
from google.appengine.api import users
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template,**kw))

class MainPage(Handler): 
	def get(self):
		content = {

		'lessons': ['Introduction to Networks'],

		'concepts': [
		['HL1', 'text1'],
		['HL2', 'text2'],
		['HL3', 'text3'],
		['HL3', 'text3']
		],

		}	
		template = jinja_env.get_template('notes_S4_S5.html')
		self.response.write(template.render(content))	

class TableOfContent(Handler): #FIX links in HTML & ADD link in main if time
	def get(self):
		self.render('T_o_C.html')

class Notes_S1_S3(Handler):  #ADD link in main if time
	def get(self):
		self.render("notes_S1_S3.html") 

# class Comments(Handler):  #ADD link in main if time
# 	def get(self):
# 		self.render("comments.html") 

class Comments(Handler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([('/', MainPage),
								('/T_o_C', TableOfContent), #MAKE main if time and LINK to notes directly
								('/notes_S1_S3', Notes_S1_S3),
								#('/notes_S4_S5', Notes_S4_S5), SEE above
								('/comments', Comments),
								],
								debug=True)







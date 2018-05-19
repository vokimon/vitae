#!/usr/bin/python
# -*- coding: utf-8 -*-

class Encoder :
	"""Encodes strings in a structure of dictionary like objects and sequences"""
	def escape(self, object) :
		if isinstance(object, str) : return self.escapeString(object)
		if isinstance(object, dict) : return self.escapeDict(object)
		return self.escapeSeq(object)

	def escapeSeq(self, seq) :
		return [self.escape(s) for s in  seq]

	def escapeDict(self, input) :
		return input.__class__(
			**dict( 
				(key, self.escape(value) )
				for key, value in input.items()) )

	def unicode(self, string) :
		if hasattr(string, 'encode'):
			return string
		return string.decode("utf8")

class HtmlEncoder(Encoder) :
	"""
	This class converts a Vitae structure into an HTML document.
	"""
	def escapeString(self, string) :
		encoded = self.unicode(string)
		substitutions = [
			"&", "&amp;",
			">", "&gt;",
			"<", "&lt;",
			]
		for old, new in zip(substitutions[::2],substitutions[1::2]) :
			encoded = encoded.replace(old, new)
		return encoded

class TexEncoder(Encoder) :
	def escapeString(self, string) :
		encoded = self.unicode(string)
		substitutions = [
			'\\', '\\\\',
			"_", '\_',
			"{", '\{',
			"}", '\}',
			"$", '\$',
			]
		for old, new in zip(substitutions[::2],substitutions[1::2]) :
			encoded = encoded.replace(old, new)
		return encoded

class ConstrainedDict(dict) :
	"""
	A constrained dict is a dictionary like object whose keys
	may be constrained given a list of mandatory keys
	and a list of optional keys with default values.
	"""
	class UnsupportedParameter(Exception) :
		def __init__(self, context, parameterName) :
			self._parameterName = parameterName
			self._context = context
		def __str__(self) :
			return "Unsuported parameter '%s' in '%s'"%(self._parameterName, self._context)

	class MissingRequiredParameter(Exception) :
		def __init__(self, context, parameterName) :
			self._parameterName = parameterName
			self._context = context
		def __str__(self) :
			return "Missing required parameter '%s' in '%s'"%(
				self._parameterName,
				self._context,
				)

	def __init__(self,  params={}, requiredFields=[], defaultValues={}, **kwd) :
		self._forceMustHaveParameters(kwd, requiredFields)
		self._forceNoAlienParameters(kwd, requiredFields, defaultValues)
		values = defaultValues.copy()
		values.update(kwd)
		dict.__init__(self, values)
		self.__dict__ = self

	def _forceNoAlienParameters(self, parameters, requiredFields, defaultValues) :
		for key in parameters.keys() :
			if key in requiredFields: continue
			if key in defaultValues: continue
			raise ConstrainedDict.UnsupportedParameter(
				self.__class__.__name__, key)

	def _forceMustHaveParameters(self, parameters, requiredFields) :
		for param in requiredFields :
			try : parameters[param]
			except KeyError: raise ConstrainedDict.MissingRequiredParameter(self.__class__.__name__,param)

class Vitae(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields=(
				'firstName surname birthDate profession '+
				'nationality contactEmail educations positions'
				).split(),
			defaultValues = dict(
					photo = '',
					summary = "",
					interests = [],
					languages = [],
					publications = [],
					portfolio = [],
					awards = [],
					courses = [],
					skills = [],
				),
			**params
			)

class Position(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params, 
			requiredFields = "start company title".split(),
			defaultValues = dict(
				end = 'Now',
				description = "",
				),
			**params
			)
class Education(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields ="start degree school field".split(),
			defaultValues = dict(
				end = 'Unfinished',
				thesis = '',
				topics = '',
				activities = [],
				),
			**params
			)
class Course(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields ="start title issuer duration".split(),
			defaultValues = dict(
				),
			**params
			)
class Award(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields ="year position contest work".split(),
			defaultValues = dict(
				),
			**params
			)
class Publication(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields = "author year title".split(),
			defaultValues = dict(
				notes = '',
				url = '',
				abstract = '',
				video = '',
				slides = '',
				),
			**params
			)
class Work(ConstrainedDict) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields = "title url description".split(),
			**params
		)

def htmlPosition(position) :
	return u"""
<dt><span class='positionPeriod'>[%(start)s - %(end)s]</span></dt>
<dd><span class='positionTitle'>%(title)s</span> at
<span class='positionCompany'>%(company)s</span>.<br />
%(description)s</dd>
"""%position

def htmlPublication(publication) :
	return (u"""
<div class='publication'>
<span class='pubAuthor'>%(author)s</span> %(year)s.<br />
<span class='pubTitle'>"%(title)s"</span><br />
%(notes)s
""" + (
"""<span class='pubUrl'><a target='_blank' href='%(url)s'>[Download]</a></span>
""" if publication.get('url',False) else "") + (
"""<span class='pubSlides'><a target='_blank' href='%(slides)s'>[Slides]</a></span>
""" if publication.get('slides',False) else "") + (
"""<span class='pubAbstract'>[Abstract]<div class='dropDown'>\n%(abstract)s</div></span>
""" if publication.get('abstract',False) else "") +
"""
</div>
""")%publication

def htmlEducation(education) :
	return (u"""
<dt><span class='educatiionPeriod'>[%(start)s - %(end)s]</span></dt>
<dd><span class='educationDegree'>%(degree)s</span> in
<span class='educationField'>%(field)s</span> at
<span class='educationSchool'>%(school)s</span>.<br />
%(thesis)s"""+(
	""" <a href='#'>[Details]<div class='dropDown'>%(topics)s</div></a>""" 
			if education.get('topics',False) else "")+
"""</dd>
""")%education

def texEducation(education) :
	return (r"""
\item[%(start)s - %(end)s]
{\bf %(degree)s} in {\bf %(field)s}
coursed at {\bf %(school)s}.
{\em %(thesis)s}"""+("""
Topics: %(topics)s""" 
			if education.get('topics',False) else "")
)%education

def htmlWork(sample) :
	return """
<dt><span class='sampleTitle'>%(title)s</span>, <a href='%(url)s'>%(url)s</a></dt>
<dd>
<span class='sampleDescription'>%(description)s</span>
</dd>
"""%sample

def texAward(award) :
	return (r"""
\item[%(year)s]
{\bf %(position)s}
at {\bf %(contest)s}
with the work {\em %(work)s}."""
)%award

def htmlWork(sample) :
	return """
<dt><span class='sampleTitle'>%(title)s</span>, <a href='%(url)s'>%(url)s</a></dt>
<dd>
<span class='sampleDescription'>%(description)s</span>
</dd>
"""%sample

def htmlSkill(skill, description) :
	return """
<dt><span class="skillName">%s:</span></dt>
<dd>%s</dd>
"""%(skill, description)

def htmlLanguage(language, level) :
	return """
<li><span class="languageName">%s:</span> %s</li>
"""%(language.capitalize(), level)

def htmlVitae(curriculum) :
	curriculum = HtmlEncoder().escape(curriculum)
	return u"""\
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style>
body {
	color: black;
	background-color: #fff;
}
.content {
	width: 40em;
	margin-left: auto;
	margin-right: auto;
	text-align: justify;
	background-color: #fff;
}
h2 {
	color: #834;
	border-bottom: solid 1pt black;
}
.publication {
	margin-top: 2ex;
	margin-bottom: 2ex;
}
.pubAuthor {
	color: #631;
	font-variant: small-caps;
}
.pubTitle {
	font-style:italic;
	color: #33a;
}
.positionPeriod, .educatiionPeriod {
	color: #262;
}
.positionTitle, .educationDegree, .educationField, .sampleTitle {
	font-weight: bold;
	color: #456
}
.positionCompany, .educationSchool, .skillName, .languageName {
	font-weight: bold;
	color: #964
}
a:link, a:visited, a:active, .pubAbstract {
	color: blue;
	text-decoration: none;
}
.dropDown {
	color: blue;
}
.dropDown {
	display: none;
}
:hover > div.dropDown ,
:hover > div.dropDown ,
:hover > div.dropDown {
	color: black;
	text-decoration: none;
	display: inline;
	display: block;
	background: #ffe;
	border: 1pt solid #aa8;
	opacity: .8;
	padding: 1ex;
	padding-left: 4ex;
	padding-right: 2ex;
}
.vitaePhoto {
	float: right;
	width: 25%%;
}
.toc {
	width: 10em;
	display: none;
	color: #555;
	background: eee;
	position: fixed;
	left: 3em;
	border: #ddd solid 1px;
}
@media only screen and (min-width: 70em) {
.toc {
	display: block;
}
}
.toc ul {
	padding: 1em;
	margin: 0;
	list-style-type: none;
	list-style-position: inside;
}
.toc li a {
	width: 100%%;
}
.toc li a:active {
	color: red;
}
.toc li a:hover {
	color: black;
	background: #fca;
	padding-left: 0.5em;
	transition: background-color 0.5s;
	-webkit-transition: background-color 0.5s; /* Safari */
}
.toc li a {
	transition: background-color 1s;
	-webkit-transition: background-color 1s; /* Safari */
	display: block;
	width: 100%%;
	padding: 5px;
}
.toc li a:visited,
.toc li a {
	color: #544;
}

</style>
</head>
<body>
<div class='toc'>
<ul>
<li><a href='#personal'>Personal Data</a></li>
<li><a href='#summary'>Summary</a></li>
<li><a href='#interests'>Interests</a></li>
<li><a href='#education'>Education</a></li>
<li><a href='#languages'>Languages</a></li>
<li><a href='#experience'>Experience</a></li>
<li><a href='#publications'>Publications</a></li>
<li><a href='#skills'>Skills</a></li>
<li><a href='#portfolio'>Portfolio</a></li>
</ul>
</div>
<div class='content'>
<h1>%(firstName)s %(surname)s's Vitae</h1>
<img class='vitaePhoto' src='%(photo)s'  />
<h2 id='personal'>Personal data</h2>
<ul>
<li><b>First name:</b> %(firstName)s</li>
<li><b>Surname:</b> %(surname)s</li>
<li><b>Profession:</b> %(profession)s</li>
<li><b>Contact:</b> %(contactEmail)s</li>
<li><b>Born:</b> %(birthDate)s</li>
<li><b>Nationality:</b> %(nationality)s</li>
</ul>
<h2 id='summary'>Summary</h2>
<p>
%(summary)s
</p>
"""%dict(curriculum) + """
<h2 id='interests'>Interests</h2>
<p>""" + ", ".join(curriculum.interests)+"""
</p>
<h2 id='education'>Education</h2>
<dl>
""" + "".join(htmlEducation(education) for education in curriculum.educations) + """
</dl>
<h2 id='languages'>Languages</h2>
<ul>
""" + "".join(htmlLanguage(language,level) for language, level in curriculum.languages.items()) + """
</ul>
<h2 id='experience'>Experience</h2>
<dl>
""" + "".join(htmlPosition(position) for position in curriculum.positions) + """
</dl>
<h2 id='publications'>Publications</h2>
""" + "".join(htmlPublication(publication) for publication in curriculum.publications) + """
<h2 id='skills'>Skills</h2>
<dl>
""" + "".join(htmlSkill(skill,description) for skill, description in curriculum.skills) + """
</dl>
<h2 id='portfolio'>Portfolio</h2>
<dl>
""" + "".join(htmlWork(sample) for sample in curriculum.portfolio) + """
</dl>
</div>
</body>
</html>
"""


Vitae.html = htmlVitae

def texVitae(curriculum) :
	curriculum = TexEncoder().escape(curriculum)
	result = r"""
\documentclass{article}
\usepackage{currvita}
\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage[dvips]{epsfig}
\usepackage{charter}
\usepackage{hyperref}

\oddsidemargin  0.5cm  %% Ancho Letter 21,59cm
\evensidemargin 0.5cm  %% Alto  Letter 27,81cm
\textwidth      15.5cm
\topmargin      0cm
\textheight     20cm
\parindent      2cm
\parskip        2ex

\begin{document}

\setlength{\cvlabelwidth}{45mm}

\begin{cv}{%(firstName)s %(surname)s. Curriculum Vitae}

%%\includegraphics[scale=.23]{%(photo)s}
\begin{cvlist}{Personal Data}
\item[Full name:] %(firstName)s %(surname)s
\item[Born] %(birthDate)s
\item[Nationality] %(nationality)s
\item[E-mail] %(contactEmail)s
\end{cvlist}

\begin{cvlist}{Summary}
\item[] %(summary)s
\end{cvlist}
"""%curriculum + r"""
\begin{cvlist}{Interests}
\item[] """ + ", ".join(curriculum.interests) + r"""
\end{cvlist}

"""
	result += r"""

\begin{cvlist}{Language skills}
"""
	for language, level in curriculum.languages.items() :
		result += "\\item[%s] %s\n"%(language.capitalize(), level)
	result += r"""
\end{cvlist}

"""
	result += r"""
\begin{cvlist}{Education}
""" + "".join(texEducation(education) for education in curriculum.educations) + r"""
\end{cvlist}
"""
	result += (r"""
\begin{cvlist}{Awards and Honors}
"""+ ''.join(texAward(award) for award in curriculum.awards) + r"""
\end{cvlist}
""") if curriculum.awards else ""

	result += r"""
\begin{cvlist}{Professional Experience}
"""
	for position in curriculum.positions :
		result += r"""
\item[%(start)s-%(end)s]
{\bf %(title)s} at
{\bf %(company)s.}\\
%(description)s
"""%position
	result += r"""	
\end{cvlist}

\begin{cvlist}{Publications}
"""
	for publication in curriculum.publications :
		result += r"""
\item[] {\sc %(author)s} %(year)s.
'{\em %(title)s}'
%(notes)s
"""%publication
	result += r"""	
\end{cvlist}

"""
	result += r"""
\begin{cvlist}{Technical skills}
"""
	for skill, description in curriculum.skills :
		result += r"""
\item[%s]
	%s
"""%(skill, description)
	result += r"""
\end{cvlist}

\begin{cvlist}{Courses}
"""
	for course in curriculum.courses :
		result += r"""
\item[%(start)s]
	{\bf %(title)s } provided by {\bf %(issuer)s} (%(duration)s)
"""%course
	result += r"""
\end{cvlist}

\begin{cvlist}{Portfolio}
"""

	for sample in curriculum.portfolio :
		result += "\\item[%(title)s]\n%(description)s\n"%sample
		if sample.url : result += "\\footnote{\\href{%(url)s}{%(url)s}}\n"%sample
	result += r"""
\end{cvlist}

\cvplace{Barcelona}

\vspace{2cm}

\end{cv}
\end{document}
"""
	return result

Vitae.tex = texVitae




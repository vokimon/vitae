#!/usr/bin/python
# -*- coding: utf-8 -*-

from vitae import Vitae, Position, Education, Publication, Work


myVitae = Vitae(
	firstName = 'David',
	surname = u'García Garzón',
	photo = 'http://canvoki.net/foto.jpg',
	profession = 'Researcher and Computer Engineer',
	birthDate = '10th May 1975, Barcelona, Spain',
	nationality = 'Spain',
	contactEmail = 'david.garcia at upf.edu',
	summary =
"""I am a researcher specialized on the domains of 3D Acoustics, Music Information Retrieval and Audio Software Engineering.
My current research is related to 3D Acoustics.
Some research topics I recently faced are:
Chord extraction, real-time convolution, 3D virtual scenario acoustics simulation, visual prototyping of audio applications.
I also have development experience on desktop, web and server applications, related to audio and multimedia.
I have strong experience using agile methodologies and open source tools and methods.
Some technologies I recently hacked with are Qt, C++, Python, Django, PHP, SCons, JACK, ALSA, PortAudio, Linux, bash, OpenGL... 
""",
	interests = [
		"Music software engineering",
		"Music information retrieval",
		"3D acoustics simulation",
		"3D audio production and playback",
		"Emergent evolutionary systems",
		"Free and Open Source Software",
		"Software project management",
		],
	languages = dict(
		spanish = 'Native speaker',
		catalan = 'Native speaker',
		english = 'Fluent (B2)',
		),
	positions = [
		Position(
			company = u'Barcelona Mèdia',
			title = 'Researcher',
			start = 'Jun 2007',
			description =
				"Design and develop real-time systems for 3D audio. "
				"The system became the basis for a commercial start-up (ImmSound). "
				"It was deployed in cinemas world wide, until Dolby decided to buy the technology. "
				"My contributions include defining the processing architecture as well as the application, "
				"algorithm transcription and optimization, and junior training. "
				"",
		),
		Position(
			company = 'BMAT, Barcelona Music and Audio Technologies',
			title = 'Co-founder and partner',
			start = 'Dec 2005',
		),
		Position(
			company = 'Universitat Pompeu Fabra',
			title = 'Professor',
			start = 'Sep 2002',
			description = 
				"""Teaching Software Engineering (Requirements gathering, UML, """+
				"""Design Patterns, Test Driven Development, Refactoring, """+
				"""Agile Methodologies, C++) and """+
				"""Programming III (Object oriented programming, Java).""",
		),
		Position(
			company = 'CLAM (C++ Library for Audio and Music)',
			title = 'Core developer',
			start = 'Jan 2000',
			description =
				"""I've take part of the team of core developers of the CLAM framework. """+
				"""CLAM has become a framework of reference in multimedia and audio. """+
				"""It won the 2006 ACM Award to the Best Multimedia Open Source Software """+
				"""and was a featured project for 2007 and 2008 editions of the Google Summer of Code.""",
		),
		Position(
			company = u'Fundació UPC',
			title = 'Professor',
			start = 'Sep 2002',
			end = 'Jun 2004',
			description =
				"""Course: 'Software Engineering Tools and Methodologies on """+
				"""Free Software Platforms' within the Free Software Master.""",
		),
		Position(
			company = 'Music Technology Group of the Universitat Pompeu Fabra',
			title = 'Research Assistant',
			start = 'Sep 2000',
			end = 'Dec 2006',
			description = 
				"""Providing group wide support for audio software engineering """+
				"""dealing with technology advising, software quality assurance, """+
				"""software integration, software architecture, graphic interfaces and packaging. """+
				"""Involved in projects such as CLAM, Agnula, Cuidado, and Simac. """+
				"""Specialized in Free Software and Music Information Retrieval.""",
		),
		Position(
			company = 'Electronic Engineering Department at Queen Mary Universtity of London',
			title = 'Visitor Researcher',
			start = 'Feb 2005',
			end = 'Apr 2005',
		),
		Position(
			company = 'Cards Engineering Spain, S.L.',
			title = 'Senior Programmer and Analyst',
			start = 'Aug 2000',
			end = 'Dec 2003',
			description =
				"""Developing intranet applications for industrial engineering environments. """+
				"""Deploying the development environment (CVS, Mantis, Automated tests...). """+
				"""Involved PHP, unix shell scripting and dealing multiple UNIX flavors.""",
		),
		Position(
			company = 'FUNITEC',
			title = 'Teacher',
			start = 'Sep 1998',
			end = 'Jun 1999',
			description = """Organizing and teaching an Ongoing Education Course on Computer Music at Enginyeria la Salle. (42 teaching hours)""",
		),			
		Position(
			company = 'NexTReT',
			title = 'Junior Programmer',
			start = 'Jul 1997',
			end = 'Dec 1997',
			description =
				"""Working at client site, EDS Iberia, on the ticketing section: """+
				"""Legacy code maintainance involving AIX, C, DB’s and """+
				"""ticket printer low level programming. """+
				"""Quality control and assurance on a developing system involving Oracle technologies.""",
		),
		Position(
			company = u'Software Technology section of the Departament d\'Informàtica of Enginyeria La Salle',
			title = 'Collaborator and teacher assistant',
			start = 'Sep 1994',
			end = 'Jun 1997',
			description =
				"""Preparing written materials (a Smalltalk-80 manual). """+
				"""Teaching departamental courses on Advanced C. """+
				"""Teaching laboratory sessions of Programming I course. """+
				"""Educational intensification on Programming II. """+
				"""Adapting a Genetic Algorithms tool to solve permutation problems (TSP). """,
		),
	],
	educations = [
		Education(
			school = "Universitat Pompeu Fabra",
			degree = "PhD",
			field = "Information, Communication and Audiovisual Media Technologies",
			start = "2007",
			thesis = "Proposal: Relating audio and 3D scenarios in audiovisual productions.",
		),
		Education(
			school = "Universitat Pompeu Fabra",
			degree = "Master",
			field = "Information, Communication and Audiovisual Media Technologies",
			start = "2006",
			end = "2007",
			thesis = "Thesis: Visual Prototyping for Audio Applications.",
			topics = "Audio Software Engineering, Frameworks, Domain Specific Languages, Prototyping tools",
			activities = [
				"Grup de Tecnologia Musical (MTG)",
			]
		),
		Education(
			school = "Enginyeria la Salle, Universitat Ramon Llull",
			degree = "Engineering",
			field = "Computer Science",
			start = "1997",
			end = "2002",
			thesis = "Final Career Project: XML support for an audio framework.",
			topics = "XML, C++ template metaprogramming, Audio processing, Frameworks design",
			activities = [
				"Departament d'Acústica",
				"Curs d'Informàtica Musical",
			],
		),
		Education(
			school = "Enginyeria la Salle, Universitat Ramon Llull",
			degree = "Technical Engineering",
			field = "Computer Science",
			start = "1993",
			end = "1997",
			thesis = "Final Career Work: Bioscena, an evolutionary environment with interaction among individuals.",
			topics = "Artificial Life, Genetic algorithms, Advanced OO Design",
			activities = [
				"Departament d'Informàtica",
			],
		),
		Education(
			school = "Col·legi Llor (Sant Boi de Llobregat)",
			degree = "BUP/COU (Bachelor)",
			field = "Cientific/Sanitary",
			start = "1988",
			end = "1993",
		),
	],
	skills = [
		('Programming Languages',
			"""I have a deep knowledge on programming and scripting languages """+
			"""such  as C++, Python, PHP, Smalltallk, Java and Bash. """),
		('Web Standards',
			"""I've been working on XHTML, HTML 4.1, CSS 2.0, DOM (JavaScript), XML, XPath, XSD, XQuery... """+
			"""I also have experience on building cross browser web pages."""),
		('Operating systems',
			"""I've been working with several Linux flavors, mostly with Debian, SuSe, Fedora and Ubuntu. """+
			"""I tend to forget anything i learnt about Windows, but i could manage to make it work when needed. """+
			"""I just have very slight knowledge of MacOsX but the underlying FreeBSD."""),
		('Networks',
			"""I have experience programing network applications and web services (php, python, django) and setting up basic apache servers."""+
			"""I have some experience on LAN administration and firewalls/routers configuration. """),
		('Databases',
			"""I am an experienced SQL programmer. """+
			"""I have used API's such as ADOdb, DAO and ODBC. """+
			"""I have experience administrating MySql databases. """+
			"""I have theoretical knowledge on the internal implementation of distributed database managers. """),
		('Sound',
			"""I've been involved on the development of an audio and music framework """+
			"""involving advanced real-time signal processing and """+
			"""multiplatform audio hardware programming. """+
			"""I've got a lot of experience analyzing existing audio software to port, to enhance or to optimize it. """+
			"""I have experience setting up MIDI networks. """+
			"""I have a deep knowledge of the Linux audio infrastructure (ALSA, Jack...) """+
			"""I have have experience programing plugins and hosts for different plugin platforms: Ladspa, Lv2, Vst, and AudioUnits. """),
		('3D Programming',
			"""I have experience programing the OpenGL API. """+
			"""I experience on programming raster, shading and texturization routines. """+
			"""I have some notions on modeling and animating scenes. """+
			"""I have experience on modeling languages such as PovRay. """),
		('2D Graphics',
			"""I have experience using Gimp (PaintShop equivalent) and Inkscape (Freehand/Illustrator equivalent). """+
			"""I used them for both artistic and professional purposes. """),
		],
	publications = [
		Publication(
			author = "Jun Wang, Xavier Amatriain, David Garcia Garzón, Jinlin Wang",
			title ="Combining multi-level audio descriptors via web identification and aggregation",
			year = "2009",
			notes = "Presented at World Wide Web Conference'09, Developers Track, Madrid",
#			abstract = """In this paper, we present the CLAM Aggregator, a tool included in the CLAM framework that allows combining multi-level audio descriptors. The tool includes a reliable method to identify the user’s local music collection using open data resources and allows users to configure, aggregate and edit music information ranging from low-level descriptors to any metadata from the semantic Web. All these steps are designed in a flexible, graphical, and user-adaptive way.""",
#			url = "http://xavier.amatriain.net/pubs/wang_www09.pdf",
		),
		Publication(
			author = "D. Garcia, D. Arteaga,  J.  Usher, T. Mateos",
			title ="Determining a room geometry from its impulse response",
			year = "2010",
			notes = "Presented at Internoise10, Lisbon, June 2010.",
#			abstract = """This paper reports on the development of a system to characterize the geometric properties of a space from an acoustic impulse response measured within it. This can be thought of as the inverse problem to the common practice of obtaining impulse responses from either a real-world or a virtual space. Starting from a measured or synthesized impulse response in an original scene, the method described here defines a space of possible scenes and a distance measure on it, and discusses a strategy to select a scene from this space, which is perceptually as close as possible to the original one. Potential applications of this novel method include audio forensics, re-equalization and re-mixing of music and audio.""",
#			url = "http://www.20203dmedia.eu/materials/papers/SCENE_GEOMETRY.pdf",
		),
		Publication(
			author= "Bailer, W. Arumi, P. Mateos, T. Garriga, A. Durany, J. and Garcia, D.",
			title ="Estimating 3D Camera Motion for Rendering Audio in Virtual Scenes",
			year = "2009",
			notes = "5th European Conference on Visual Media Production, 2008.",
#			abstract = """Abstract: In the production phase of digital cinema content it is important to allow the director not only to preview the final rendered scene early in the shooting process, but also to prehear the 5.1 surround and HRTF-based binaural versions, thus enabling visual and auditive artistic decisions to be taken at the shooting stage. In many cases camera tracking data is not available for all cameras on the set (e.g. handheld ones) and thus the motion of the camera needs to be estimated. In this paper we describe an approach for estimation of 3D camera motion and its use for real-time audio rendering.""",
		),
		Publication(
			author = "P. Arumi, D. Garcia, T. Mateos, A. Garriga and J. Durany.",
			title = "Real-time 3D audio for digital cinema",
			year = "2008",
			notes = "ASA Conference ACOUSTICS'08 Paris."
#			abstract = """We present a real-time 3D audio system with a number of nice features: it is suited for plausible reference with the visual environment, it is real-time capable, it can process multiple moving sound sources and listeners in a normal CPU. In our approach, a database of pressure and velocities impulse-responses (IRs) is computed offline for each (architectural) environment using physically based ray-tracing techniques. During playback, the real-time system retrieves IRs corresponding to the sources and target positions, performs a low-latency partitioned convolution and smoothes IR transitions with cross-fades. Finally, the system is flexible enough to decode to any surround exhibition setup. The software has been developed within the CLAM open-source audio framework. We present a real scenario where these techniques were successfully applied: an augmented-reality film with 3D audio within the context of the IP-RACINE project for digital cinema. The shooting was done with a high-end prototype camera with zoom and position tracking which enabled the real-time motion of a subjective listener within the scene. Our technology enabled the film director to both pre-hear surround audio of an augmented-reality scene shooting and fine-tune audio rendering in post-production.""",
#			slides = "http://www.20203dmedia.eu/materials/papers/slides_acoustics08_realtime.pdf",
		),
		Publication(
			author = "Garcia, D.",
			title = "Visual Prototyping of Audio Applications",
			year = "2007",
			notes= "Master Thesis, Master Program in Information, Communication and Audiovisual Media. Advisors: Xavier Serra and Xavier Amatriain. Department of Information and Communication Technologies, Universitat Pompeu Fabra. Barcelona, September 2007.",
			),
		Publication(
			author = u'Olaiz, N. Arumí, P. Mateos, T. García, D.',
			year ='2009',
			title = "3D-Audio with CLAM and Blender's Game Engine",
			notes = "Proceedings of the 7th International Linux Audio Conference (LAC09); April 2009; Parma, Italy.",
#			video = "http://lac.linuxaudio.org/2009/cdm/Thursday/05_Arumi/index.html",
		),
		Publication(
			author = u'Arumí, P. Amatriain, X. García, D.',
			year = '2008',
			title = 'A Framework for Efficient and Rapid Development of Cross-platform Audio Applications',
			notes = 'ACM Multimedia Systems Journal; 14(1) June 2008',
			),
		Publication(
			author = u'García, D. Arumí, P. Amatriain, X.',
			year = '2007',
			title = 'Visual prototyping of audio applications',
			notes = 'Proceedings of Linux Audio Conference 2007; Berlin; Germany',
			),
		Publication(
			author = u'Arumí, P. García, D. Amatriain, X.',
			year = '2006',
			title = 'A Data Flow Pattern Language for Audio and Music Computing',
			notes = 'Proceedings of Pattern Languages of Programs 2006; Portland, Oregon',
#			uri = "dataflow_patterns_plop06.pdf",
			),
		Publication(
			author = u'Amatriain, X. Arumí, P. García, D.',
			year = '2006',
			title = 'CLAM: A Framework for Efficient and Rapid Development of Cross-platform Audio Applications',
			notes = 'Proceedings of ACM Multimedia 2006; Santa Barbara, CA',
			),
		Publication(
			author = u'Arumí, P. Sordo, M. García, D. Amatriain, X.',
			year = '2006',
			title = 'Testfarm, una eina per millorar el desenvolupament del programari lliure',
			notes = 'Proceedings of V Jornades de Programari Lliure; Barcelona',
			),
		Publication(
			author = u'García, D. Arumí, P. Amatriain, X.',
			year = '2006',
			title = u'Extracció d\'acords amb l\'Anotador de Música de CLAM',
			notes = 'Proceedings of V Jornades de Programari Lliure; Barcelona',
			),
		Publication(
			author = u'Amatriain, X. Massaguer, J. García, D. Mosquera, I.',
			year = '2005',
			title = 'The CLAM Annotator: A Cross-platform Audio Descriptors Editing Tool',
			notes = 'Poster presented at 6th International Conference on Music Information Retrieval; London, UK',
			),
		Publication(
			author = u'Cano, P. Koppenberger, M. Wack, N. G. Mahedero, J. Masip, J. Celma, O. García, D. Gómez, E. Gouyon, F. Guaus, E. Herrera, P. Massaguer, J. Ong, B. Ramírez, M. Streich, S. Serra, X.',
			year = '2005',
			title = 'An Industrial-Strength Content-based Music Recommendation System',
			notes = 'Proceedings of 28th Annual International ACM SIGIR Conference; Salvador, Brazil'
			),
		Publication(
			author = u'Cano, P. Koppenberger, M. Wack, N. G. Mahedero, J. Aussenac, T. Marxer, R. Masip, J. Celma, O. García, D. Gómez, E. Gouyon, F. Guaus, E. Herrera, P. Massaguer, J. Ong, B. Ramírez, M. Streich, S. Serra, X.',
			year = '2005',
			title = 'Content-based Music Audio Recommendation',
			notes = 'Proceedings of ACM Multimedia 2005; Singapore, Singapore',
			),
		Publication(
			author = u'Herrera, P. Celma, O. Massaguer, J. Cano, P. Gómez, E. Gouyon, F. Koppenberger, M. García, D. G. Mahedero, J. Wack, N.',
			year = '2005',
			title = 'Mucosa: a music content semantic annotator',
			notes = 'Proceedings of 6th International Conference on Music Information Retrieval; London, UK',
			),
		Publication(
			author = u'Arumí, P. García, D. Amatriain, X.',
			year = '2003',
			title = 'CLAM, Una llibreria lliure per Audio i Música',
			notes = 'Proceedings of II Jornades de Software Lliure; Barcelona',
			),
		Publication(
			author = u'Celma, O. Gómez, E. Janer, J. Gouyon, F. Herrera, P. García, D.',
			year = '2004',
			title = 'Tools for Content-Based Retrieval and Transformation of Audio Using MPEG-7: The SPOffline and the MDTools',
			notes = 'Proceedings of 25th International AES Conference; London, UK',
			),
		Publication(
			author = u'García, D.',
			year = '2002',
			title = u'Suport de XML/MPEG-7 per una llibreria de processat d\'àudio i música.',
			notes = 'Enginyeria La Salle. Barcelona',
			),
		Publication(
			author = u'Amatriain, X. de Boer, M. Robledo, E. García, D.',
			year = '2002',
			title = 'CLAM: An OO Framework for Developing Audio and Music Applications',
			notes = 'Proceedings of 17th Annual ACM Conference on Object-Oriented Programming, Systems, Languages and Applications. Seattle, WA, USA',
			),
		Publication(
			author = u'García, D. Amatriain, X.',
			year = '2001',
			title = 'XML as a means of control for audio processing, synthesis and analysis',
			notes = 'Proceedings of MOSART Workshop on Current Research Directions in Computer Music. Barcelona',
			),
		],
	portfolio = [
		Work(
			title = 'CLAM (C++ Library of Audio and Music)',
			url = 'http://clam-project.org',
			description = 
				"""Being one of the core developers I have been involved """+
				"""in most of the aspects of that awarded free software project. """+
				"""XML support, GUI, audio back-end's, architecture, reflection, """+
				"""processing algorithms, quality assurance...""",
			),
		Work(
			title = "My technical blog and web page",
			url = "http://canvoki.net/coder",
			description =
				"""Daily discussion on technical stuff I work on."""+
				"""My technical web page contains some tutorials and """+
				"""several minor projects not listed here including """+
				"""an SConstruct tool to support Qt4, """+
				"""an UML Use Case diagram generator, """+
				"""a continuous integration efficiency tracker..."""+
				"",
			),
		Work(
			title = "Course materials",
			url = "http://canvoki.net/docencia.html",
			description =
				"""A compilation of most of the material elaborated for the courses I teach."""+
				"",
			),
		Work(
			title = "Personal GitHub page",
			url = "http://github.com/vokimon",
			description =
				"""Several projects I maintain in GitHub and public contributions to other projects hosted there.""",
			),
		Work(
			title = 'WiKo (The wiki compiler)',
			url = 'http://wiko.sourceforge.net',
			description = 
				"""It is a Python script to generate webs, scientific articles and blogs from files in wiki format. """+
				"""I developed this tool to ease the maintaining of my own web sites. """+
				"""Since them it has become a community project at sourceforge """+
				"""and we have successfully used it in several projects I was involved in. """+
				"""Some nice features are: produces multiple output (pdf/html) from a single input (wiki), """+
				"""supports BiBTeX and LaTeX formulae, imports blogs from blogger, generates image galleries... """,
			),
		Work(
			title = 'CeView',
			url = 'http://www.cardse.com',
			description = 
				"""A product I developed when I was working on Cards Engineering. """+
				"""It is a web based collaborative application to share and annotate CAD files from several TDM-like systems. """+
				"""Besides developing the product, I deployed the company development infrastructure """+
				"""to meet agile development requirements. """+
				"""The system was successfully implanted on Ford Ibérica, CASA, and Metro de Madrid. """,
			),
		Work(
			title = "PyVitae",
			url = "",
			description =
				"""PyVitae is a python project to define curriculum vitae using a simple """+
				"""text based syntax and generating several outputs including html and pdf. """+
				"""Like WiKo, it follows a write-once-generate-many principle. """+
				"""This curriculum has been generated using it.""",
			),
#		Work(
#			title = "Bioscena",
#			url = "",
#			description =
#				"""Bioscena was a multiplatform C++ environment to simulate evolutive biologic system. """+
#				"""The system was highly configurable to simulate different biotopes and  """+
#				"""different physical and biological rules. """+
#				"""You can play with differents mechanisms for genic expression and phenotypical interaction. """+
#				"""Some real-like genic expression mechanism were included such as  """+
#				"""codon decoding, intron and exon zones, promoter zones, multiple chromosomes """+
#				"""several kinds of mutations... """+
#				"""By monitoring and analyzing the system output you can get insight about """+
#				"""the emergent life features such the aparition self-reproducing beings, """+
#				"""the self regulation of mortality, """+
#				"""some interactions (family support, depredation, and several kinds of symbiosy), """+
#				"""and adaptation to short term periodic changes on the environment. """+
#				""),
		],
			
)

import vitae, os, codecs
codecs.open("output.html","w", encoding="utf8").write(myVitae.html())
codecs.open("output.tex", "w", encoding="utf8").write(myVitae.tex())
#os.system("pdflatex output")



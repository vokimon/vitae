#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vitae import Vitae, Position, Education, Publication, Work, Course, Award
from yamlns import namespace as ns
import vitae, os, codecs, sys

def fromYamlFile(filename):
	data = ns.load(filename)
	data.positions = [Position(**item) for item in data.positions]
	data.educations = [Education(**item) for item in data.educations]
	data.publications = [Publication(**item) for item in data.publications]
	data.portfolio = [Work(**item) for item in data.portfolio]
	data.courses = [Course(**item) for item in data.courses]
	data.awards = [Award(**item) for item in data.awards]
	data.skills = [item for item in data.skills.items()]
	return  Vitae(**data)

outputbase = os.path.splitext(sys.argv[1])[0]
myVitae = fromYamlFile('{}.yaml'.format(outputbase))

codecs.open("%s.html"%outputbase,"w", encoding="utf8").write(myVitae.html())
codecs.open("%s.tex"%outputbase, "w", encoding="utf8").write(myVitae.tex())
os.system("pdflatex %s"%outputbase)



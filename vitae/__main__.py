#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vitae import Vitae
import os, io, sys

def main():
	outputbase = os.path.splitext(sys.argv[1])[0]
	yamlfile = outputbase+'.yaml'
	htmlfile = outputbase+'.html'
	texfile = outputbase+'.tex'

	myVitae = Vitae.fromYamlFile(yamlfile)

	io.open(htmlfile,"w").write(myVitae.html())
	io.open(texfile, "w").write(myVitae.tex())
	os.system("pdflatex %s"%outputbase)

if __name__ == '__main__':
	main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from vitae import HtmlEncoder, ConstrainedDict

class HtmlEncoderTest(unittest.TestCase) :
	
	def helper_test_escapeString(self, input, expected) :
		result = HtmlEncoder().escapeString(input)
		self.assertEquals(expected.__class__, result.__class__)
		self.assertEquals(expected, result)

	def test_escapeString_unicodeString(self) :
		self.helper_test_escapeString(
			u"hola",
			u"hola")

	def test_escapeString_localString(self) :
		self.helper_test_escapeString(
			"hola",
			u"hola")

	def test_escapeString_localStringWithUnicode(self) :
		self.helper_test_escapeString(
			"€¢ÇÑçñ,áéíóúàèìòùâêîôûäëïöüÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜ",
			u"€¢ÇÑçñ,áéíóúàèìòùâêîôûäëïöüÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜ")

	def test_escapeString_unicodeStringWithUtfChars(self) :
		self.helper_test_escapeString(
			u"€¢ÇÑçñ,áéíóúàèìòùâêîôûäëïöüÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜ",
			u"€¢ÇÑçñ,áéíóúàèìòùâêîôûäëïöüÀÈÌÒÙÁÉÍÓÚÂÊÎÔÛÄËÏÖÜ")

	def test_escapeString_gt(self) :
		self.helper_test_escapeString(
			u"a>b",
			u"a&gt;b")

	def test_escapeString_lt(self) :
		self.helper_test_escapeString(
			u"a<b",
			u"a&lt;b")

	def test_escapeString_amp(self) :
		self.helper_test_escapeString(
			u"a&b",
			u"a&amp;b")

	def helper_test_escapeDict(self, input, expected) :
		actual = HtmlEncoder().escapeDict(input)
		self.assertEquals(expected, actual)
		self.assertEquals(expected.__class__, actual.__class__)

	def test_escapeDict_withAllStrings(self) :
		self.helper_test_escapeDict(
				input = dict(
					key1="value1<",
					),
				expected = dict(
					key1="value1&lt;",
					)
				)
	def helper_test_escapeSeq(self, input, expected) :
		actual = HtmlEncoder().escapeSeq(input)
		self.assertEquals(expected, actual)
		self.assertEquals(expected.__class__, actual.__class__)


	def test_escapeSeq_turnsUnicode(self) :
		self.helper_test_escapeSeq(
					["value1","value2"],
					[u"value1",u"value2"],
				)

	def test_escapeSeq_turnsEscapesSpecial(self) :
		self.helper_test_escapeSeq(
					["value1<","one & other"],
					[u"value1&lt;",u"one &amp; other"],
				)

	def helper_test_escape(self, input, expected) :
		actual = HtmlEncoder().escape(input)
		self.assertEquals(expected, actual)
		self.assertEquals(expected.__class__, actual.__class__)

	def test_escape_whenGivenAString(self) :
		self.helper_test_escape(
					"value1<",
					u"value1&lt;",
				)

	def test_escape_whenGivenASequence(self) :
		self.helper_test_escape(
					["value1<","one & other"],
					[u"value1&lt;",u"one &amp; other"],
				)
	def test_escape_whenGivenADict(self) :
		self.helper_test_escape(
				input = dict(
					key1="value1<",
					),
				expected = dict(
					key1="value1&lt;",
					)
				)
	def test_escape_whenGivenASequenceOfSequence(self) :
		self.helper_test_escape(
					[["value1<","one & other"]],
					[[u"value1&lt;",u"one &amp; other"]],
				)

	def test_escape_whenGivenADictOfSeqs(self) :
		self.helper_test_escape(
				input = dict(
					key1=["value1<","one & other"],
					),
				expected = dict(
					key1=[u"value1&lt;",u"one &amp; other"],
					)
				)
	class DummyConstrained(ConstrainedDict) :
		def __init__(self, **params) :
			ConstrainedDict.__init__(self, params,
					requiredFields = "key1".split(),
					defaultValues = dict(key2='default'),
			)
	
	def test_escape_givenAConstrainedDict(self) :
		self.helper_test_escape(
			HtmlEncoderTest.DummyConstrained(key1="value<"),
			HtmlEncoderTest.DummyConstrained(key1="value&lt;"),
		)

if __name__ == "__main__" :
	unittest.main()



#!/usr/bin/env python

import unittest
from vitae import ConstrainedDict

class ConstrainedDictTest(unittest.TestCase) :
	def test_unexpectedParameterThrowsException(self) :
		try:
			ConstrainedDict(dict(
					unexpected="value",
					)
				)
			self.fail("Exception expected")
		except ConstrainedDict.UnsupportedParameter, e :
			self.assertEquals(
				"Unsuported parameter 'unexpected' in 'ConstrainedDict'"
				, str(e))

	def test_requiredParameter_notGivenThrows(self) :
		try:
			ConstrainedDict(dict(
					),
					requiredFields=[
						"required"
						],
				)
			self.fail("Exception expected")
		except ConstrainedDict.MissingRequiredParameter, e :
			self.assertEquals(
				"Missing required parameter 'required' in 'ConstrainedDict'"
				, str(e))
	def test_requiredParameter_given(self) :
		d = ConstrainedDict(
			dict(
				required = "a value",
				),
			requiredFields = ["required"]
			)
		self.assertEquals( dict(
				required="a value"
			), d)

	def test_requiredParameter_accessedAsAttribute(self) :
		d = ConstrainedDict(
			dict(
				required = "a value",
				),
			requiredFields = ["required"]
			)
		self.assertEquals( "a value", d.required)

	def test_optionalParameter_notGivenGetsDefault(self) :
		d = ConstrainedDict( 
			{},
			defaultValues = dict(
				defaultValuedParameter = "default value",
			))
		self.assertEquals(dict(
			defaultValuedParameter="default value",
			), d)

	def test_optionalParameter_givenGetsGiven(self) :
		d = ConstrainedDict( 
			dict(
				defaultValuedParameter = "given value",
				),
			defaultValues = dict(
				defaultValuedParameter = "default value",
			))
		self.assertEquals(dict(
			defaultValuedParameter="given value",
			), d)


class TestDict ( ConstrainedDict ) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self, params,
			requiredFields = "mandatory1 mandatory2".split(),
			defaultValues = dict(
				optional1="default1",
				optional2="default2",
				)
			)

class ConcreteConstrainedDictTest(unittest.TestCase) :
	def test_definingAllValues(self) :
		d = TestDict(
			mandatory1="value1",
			mandatory2="value2",
			optional1="value3",
			optional2="value4",
			)
		self.assertEquals(dict(
			mandatory1="value1",
			mandatory2="value2",
			optional1="value3",
			optional2="value4",
			), d)
	def test_notDefiningAnOptional(self) :
		d = TestDict(
			mandatory1="value1",
			mandatory2="value2",
			optional2="value4",
			)
		self.assertEquals(dict(
			mandatory1="value1",
			mandatory2="value2",
			optional1="default1",
			optional2="value4",
			), d)
	def test_notDefiningAMandatory_complains(self) :
		try:
			d = TestDict(
				mandatory1="value1",
				optional1="value3",
				optional2="value4",
				)
			self.fail("exception expected")
		except ConstrainedDict.MissingRequiredParameter, e :
			self.assertEquals(
				"Missing required parameter 'mandatory2' in 'TestDict'"
				, str(e))

	def test_definingAnUnexpected_complains(self) :
		try:
			TestDict(
				mandatory1="value1",
				mandatory2="value1",
				unexpected="value",
				optional1="value3",
				optional2="value4",
				)
			self.fail("exception expected")
		except ConstrainedDict.UnsupportedParameter, e :
			self.assertEquals(
				"Unsuported parameter 'unexpected' in 'TestDict'"
				, str(e))


if __name__ == "__main__" :
	unittest.main()



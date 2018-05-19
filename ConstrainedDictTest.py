#!/usr/bin/env python

import unittest
from vitae import ConstrainedDict

class ConstrainedDictTest(unittest.TestCase) :
	def test_unexpectedParameterThrowsException(self) :
		try:
			ConstrainedDict(
					unexpected="value",
				)
			self.fail("Exception expected")
		except ConstrainedDict.UnsupportedParameter as e :
			self.assertEqual(
				"Unsuported parameter 'unexpected' in 'ConstrainedDict'"
				, str(e))

	def test_requiredParameter_notGivenThrows(self) :
		try:
			ConstrainedDict(
				requiredFields = ["required"],
				)
			self.fail("Exception expected")
		except ConstrainedDict.MissingRequiredParameter as e :
			self.assertEqual(
				"Missing required parameter 'required' in 'ConstrainedDict'"
				, str(e))

	def test_requiredParameter_given(self) :
		d = ConstrainedDict(
			dict(
				),
			requiredFields = ["required"],
			required = "a value",
			)
		self.assertEqual( dict(
				required="a value"
			), d)

	def test_requiredParameter_accessedAsAttribute(self) :
		d = ConstrainedDict(
			dict(
				),
			requiredFields = ["required"],
			required = "a value",
			)
		self.assertEqual( "a value", d.required)

	def test_optionalParameter_notGivenGetsDefault(self) :
		d = ConstrainedDict( 
			{},
			defaultValues = dict(
				defaultValuedParameter = "default value",
			))
		self.assertEqual(dict(
			defaultValuedParameter="default value",
			), d)

	def test_optionalParameter_givenGetsGiven(self) :
		d = ConstrainedDict( 
			dict(
				),
			defaultValues = dict(
				defaultValuedParameter = "default value",
				),
			defaultValuedParameter = "given value",
			)
		self.assertEqual(dict(
			defaultValuedParameter="given value",
			), d)

	def test_gettingAttribute_failsIfAlien(self) :
		d = ConstrainedDict(dict(), dict())
		try:
			d.alien
			self.fail("Exception expected")
		except AttributeError as e :
			self.assertEqual(
				"'ConstrainedDict' object has no attribute 'alien'"
				, str(e))

	def test_gettingKey_failsIfAlien(self) :
		d = ConstrainedDict(dict(), dict())
		try:
			d['alien']
			self.fail("Exception expected")
		except KeyError as e :
			self.assertEqual(
				"'alien'"
				, str(e))

	@unittest.skip("Not so constrained, to implement")
	def test_settingAttribute_failsIfAlien(self) :
		d = ConstrainedDict(dict(), dict())
		try:
			d.alien = "value"
			self.fail("Exception expected")
		except AttributeError as e :
			self.assertEqual(
				"'ConstrainedDict' object has no attribute 'alien'"
				, str(e))

	@unittest.skip("Not so constrained, to implement")
	def test_settingKey_failsIfAlien(self) :
		d = ConstrainedDict(dict(), dict())
		try:
			d['alien'] = "value"
			self.fail("Exception expected")
		except KeyError as e :
			self.assertEqual(
				"'alien'"
				, str(e))

	@unittest.skip("Not implemented")
	def test_deletingAttribute_failsIfRequired(self) :
		d = ConstrainedDict(
			dict(
				),
			requiredFields = ["required"],
			required = "a value",
			)
		try:
			del d.required
			self.fail("Exception expected")
		except ConstrainedDict.MissingRequiredParameter as e :
			self.assertEqual(
				"Missing required parameter 'required' in 'ConstrainedDict'"
				, str(e))

	@unittest.skip("Not implemented")
	def test_deletingKey_failsIfRequired(self) :
		d = ConstrainedDict(
			dict(
				),
			requiredFields = ["required"],
			required = "a value",
			)
		try:
			del d['required']
			self.fail("Exception expected")
		except ConstrainedDict.MissingRequiredParameter as e :
			self.assertEqual(
				"Missing required parameter 'required' in 'ConstrainedDict'"
				, str(e))

	@unittest.skip("Not implemented")
	def test_deletingAttribute_setsToDefaultIfOptional(self) :
		d = ConstrainedDict( 
			dict(
				),
			defaultValues = dict(
				defaultValuedParameter = "default value",
				),
			defaultValuedParameter = "given value",
			)
		del d.defaultValuedParameter
		self.assertEqual(dict(
			defaultValuedParameter="default value",
			), d)

	@unittest.skip("Not implemented")
	def test_deletingKey_setsToDefaultIfOptional(self) :
		d = ConstrainedDict( 
			dict(
				),
			defaultValues = dict(
				defaultValuedParameter = "default value",
				),
			defaultValuedParameter = "given value",
			)
		del d['defaultValuedParameter']
		self.assertEqual(dict(
			defaultValuedParameter="default value",
			), d)


class TestDict ( ConstrainedDict ) :
	def __init__(self, **params) :
		ConstrainedDict.__init__(self,
			requiredFields = "mandatory1 mandatory2".split(),
			defaultValues = dict(
				optional1="default1",
				optional2="default2",
				),
			**params
			)

class ConcreteConstrainedDictTest(unittest.TestCase) :
	def test_definingAllValues(self) :
		d = TestDict(
			mandatory1="value1",
			mandatory2="value2",
			optional1="value3",
			optional2="value4",
			)
		self.assertEqual(dict(
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
		self.assertEqual(dict(
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
		except ConstrainedDict.MissingRequiredParameter as e :
			self.assertEqual(
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
		except ConstrainedDict.UnsupportedParameter as e :
			self.assertEqual(
				"Unsuported parameter 'unexpected' in 'TestDict'"
				, str(e))


# To test (and implement) if required by the implementation
# - deleting attributes and keys when optional
# - deleting attributes and keys when required

if __name__ == "__main__" :
	unittest.main()



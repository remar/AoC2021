ten = __import__("10")
import unittest

class IsCorruptTest(unittest.TestCase):
    def test_EmptyString_NotCorrupt(self):
        self.assertFalse(ten.is_corrupt(""))

    def test_StartingWithClosing_Corrupt(self):
        self.assertTrue(ten.is_corrupt(")"))

    def test_MatchingLeftAndRight_NotCorrupt(self):
        self.assertFalse(ten.is_corrupt("()"))

    def test_NonMatchingLeftAndRight_Corrupt(self):
        self.assertTrue(ten.is_corrupt("(}"))

    def test_SequenceOfMatchingPairs_NotCorrupt(self):
        self.assertFalse(ten.is_corrupt("(){}[]<>"))

    def test_NestedPairs_NotCorrupt(self):
        self.assertFalse(ten.is_corrupt("([]<>)"))

    def test_Incomplete_NotCorrupt(self):
        self.assertFalse(ten.is_corrupt("("))

class ResultingStackTest(unittest.TestCase):
    def test_EmptyString_EmptyStack(self):
        self.assertEqual(ten.resulting_stack(""), [])

    def test_OneLeftParent_IsReturned(self):
        self.assertEqual(ten.resulting_stack("("), ["("])

    def test_ABitMoreComplex_OnlyFirstParenReturned(self):
        self.assertEqual(ten.resulting_stack("([]"), ["("])

class ToCompleteTest(unittest.TestCase):
    def test_EmptyString_NothingToComplete(self):
        self.assertEqual(ten.to_complete([]), "")

    def test_OneLeftParen_OneRightParen(self):
        self.assertEqual(ten.to_complete(["("]), ")")

    def test_OneLeftParenOneLeftCurly_OneRightCurlyOneRightParen(self):
        self.assertEqual(ten.to_complete(["(", "{"]), "})")

class ScoreIncompleteLineTest(unittest.TestCase):
    def test_EmptyString_0(self):
        self.assertEqual(ten.score_incomplete(""), 0)

    def test_OneRightParen_1(self):
        self.assertEqual(ten.score_incomplete(")"), 1)

    def test_TwoRightParens_6(self):
        self.assertEqual(ten.score_incomplete("))"), 6)

    def test_LastCompletionExample_294(self):
        self.assertEqual(ten.score_incomplete("])}>"), 294)

unittest.main()

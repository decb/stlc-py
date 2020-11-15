import unittest
from nbe.generate import generate
from nbe.parser import parse_syntax, parse_type_syntax
from nbe.normalise import nbe

S = "(lambda a (lambda b (lambda c ((a c) (b c)))))"
K = "(lambda a (lambda b a))"
SKK = f"(({S} {K}) {K})"


class TestNBE(unittest.TestCase):
    def test_skk(self):
        term = parse_syntax(SKK)
        a_to_a = parse_type_syntax("(-> a a)")
        normal_form = nbe(a_to_a, term)
        self.assertEqual(str(normal_form), "(lambda a a)")

    def test_eta_long(self):
        term = parse_syntax(SKK)
        a_to_b_squared = parse_type_syntax("(-> (-> a b) (-> a b))")
        normal_form = nbe(a_to_b_squared, term)
        self.assertEqual(str(normal_form), "(lambda a (lambda b (a b)))")

    def test_swap(self):
        term = parse_syntax(
            f"((lambda x (pair (snd x) (fst x))) (pair (lambda x x) {K}))")
        swap_type = parse_type_syntax("(* (-> a (-> b a)) (-> a a))")
        normal_form = nbe(swap_type, term)
        self.assertEqual(
            str(normal_form),
            "(pair (lambda a (lambda b a)) (lambda c c))")


class TestGeneration(unittest.TestCase):
    def test_i(self):
        term = generate(parse_type_syntax("(-> a a)"))
        self.assertEqual(str(term), "(lambda a a)")

    def test_s(self):
        term = generate(parse_type_syntax(
            "(-> (-> a (-> b c)) (-> (-> a b) (-> a c)))"))
        self.assertEqual(str(term), S)

    def test_swap(self):
        term = generate(parse_type_syntax("(-> (* a b) (* b a))"))
        self.assertEqual(str(term), "(lambda a (pair (snd a) (fst a)))")


if __name__ == "__main__":
    unittest.main()

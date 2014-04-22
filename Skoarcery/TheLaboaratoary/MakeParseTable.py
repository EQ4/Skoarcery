import unittest
from Skoarcery import langoids, tokens, nonterminals
from Skoarcery.langoids import Terminal


class MakeParseTable(unittest.TestCase):

    def setUp(self):
        tokens.init()
        nonterminals.init()
        langoids.init()
        langoids.compute_firsts()
        langoids.compute_follows()
        pass

    def tearDown(self):
        pass

    def test_make_table(self):
        from collections import defaultdict
        from Skoarcery.langoids import FIRST, FOLLOW

        # M[ Nonterm, Term ] = Production
        M = defaultdict(dict)

        # (1) For each production A -> alpha
        #
        for A in nonterminals.nonterminals.values():
            for P in A.production_rules:

                alpha = P.production
                # (2)
                #
                for a in FIRST(alpha):
                    if isinstance(a, Terminal):

                        X = M[A, a]

                        if X:
                            print("Grammar is not LL(1). Fuck.")

                            print("X = {}\nP = {}\nA = {}\na = {}".format(str(X), str(P), str(A), str(a)))
                            raise AssertionError("Grammar is not LL(1). Fuck.")

                        print("M[{:>16}, {:<16}] = {}".format(A.name, a.name, str(P)))
                        M[A, a] = P

                # (3)




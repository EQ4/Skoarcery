import unittest
from Skoarcery import langoids, tokens, nonterminals, dragonsets
from Skoarcery.langoids import Terminal


class Not_LL_1(Exception):
    pass

M = None


#
# Dragon Spell: 4.4 Construction of a predictive parsing table
#
def init():
    from collections import defaultdict
    from Skoarcery.dragonsets import FIRST, FOLLOW
    from Skoarcery.tokens import Empty, EOF

    global M

    # M[ Nonterm, Term ] = Production
    M = defaultdict(dict)

    # (1) For each production A -> alpha
    #
    for A in nonterminals.nonterminals.values():
        for P in A.production_rules:

            alpha = P.production
            if P.derives_empty:
                continue

            # (2)
            #
            for a in FIRST(alpha):
                # (3)
                if a == Empty:

                    for b in FOLLOW(A):
                        if isinstance(b, Terminal) and b != Empty:

                            X = M[A, b]

                            if X and not X.derives_empty:
                                raise Not_LL_1

                            M[A, b] = P

                # (2')
                elif isinstance(a, Terminal):

                    X = M[A, a]

                    if X and not X.derives_empty:
                        raise Not_LL_1

                    M[A, a] = P


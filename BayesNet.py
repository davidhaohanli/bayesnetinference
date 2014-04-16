#!/usr/bin/env python3

import sys, re

class BayesNet:
    """
    Class for Bayesian Network.

    Data structures:
        list of variable names
        dictionary that maps variable names to a dictonary {
                parents -> list of parents
                children -> list of children
                prob -> probability of the variable if it's independent, else None
                condprob -> dictionary for the conditionary probability table {
                        tuple of values for parents -> probability
                    }
            }

        e.g. for ex2.bn
        ['A', B', 'C', 'D', 'E']
        {
            'A': {
                'parents': None,
                'children': ['C', 'D'],
                'prob': 0.3,
                'condprob': None
            },
            
            ...

            'D': {
                'parents': ['A', 'B'],
                'children': None,
                'prob': None,
                'condprob': {
                    (True, True): 0.7,
                    (True, False): 0.8,
                    ...
                }
            }
        }
    """
    def __init__(self, fname):
        pass

    def _parseline(self, line):
        pass

    def _parsetable(self, tabl):
        pass

def enum_ask(X, e, bn):
    """
    Calculate the distribution over the query variable X using enumeration.

    Args:
        X:  The query variable.
        e:  Dictionary of evidence variables and observed values.
        bn: Bayes net.

    Returns:
        Distribution over X as a tuple (t, f).
    """
    pass

def elim_ask(X, e, bn):
    """
    Calculate the distribution over the query variable X using elimination.

    Args:
        X:  The query variable.
        e:  Dictionary of evidence variables and observed values.
        bn: Bayes net.

    Returns:
        Distribution over X as a tuple (t, f).
    """

def query(net, alg, q):
    pass

def main():
    try:
        net = BayesNet(sys.argv[1])

        alg = sys.argv[2]
        assert(alg == 'enum' or alg == 'elim')

        q = sys.argv[3]

        query(net, alg, q)
    except SyntaxError:
        print('Invalid syntax for bayes net file %s' % sys.argv[1])
    except IndexError:
        print('Not enough argument.')
        print('Usage: %s <bayesnet> <enum|elim> <query>' % sys.argv[0])

if __name__=='__main__':
    main()
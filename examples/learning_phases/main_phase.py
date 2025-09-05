import openhtf as htf
import random


# Always pass
def phase_pass(test):
  return htf.PhaseResult.CONTINUE


def main():
  test = htf.Test(phase_pass)
  test.execute(lambda: "SN1234")

if __name__ == '__main__':
    main()
import openhtf as htf
import random

@htf.PhaseOptions(timeout_s=5)
def phase_pass(test):
  return htf.PhaseResult.CONTINUE

@htf.PhaseOptions(repeat_limit=5) # Retries up to 3 times in case of failure
def phase_retry(test):

  choice = random.choice([True, False])
  print(choice)
  if choice:
    return htf.PhaseResult.CONTINUE
  else:
    return htf.PhaseResult.REPEAT

def main():
  test = htf.Test(phase_pass, phase_retry)
  test.execute(lambda: "SN1234")

if __name__ == '__main__':
    main()
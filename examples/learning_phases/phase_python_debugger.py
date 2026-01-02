import openhtf as htf

"""
this will allow pdb but make sure timeout_s is set to longer to 
be able to do proper debugging.
"""
@htf.PhaseOptions(run_under_pdb=True, timeout_s=20)
def first_phase(test):
    return htf.PhaseResult.CONTINUE

def main():
    test = htf.Test(first_phase)
    test.execute(lambda: "SN1234")

if __name__ == "__main__":
    main()

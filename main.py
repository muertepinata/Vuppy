#Naming
def primernaming()-> int():
    strain1 = int(input("Hello, welcome to Vuppy. Please select your strain (use the corresponding number). "
                        "1.p4c2 \n 2.p3c2 \n 3.p2c2 \n 4.p3c2 \n 5.p2c3 \n 6. I don't know my strain."))

    if strain1 == 1:
        primernum = 4

    elif strain1 == 2 or strain1 == 4:
        primernum = 3

    elif strain1 == 6:
        primernum = int(input("What is your total number of primers? (max 4)"))

    else:
        primernum = 2

def ctrlnaming ()-> int():
    if strain1 == 4 or strain1 == 5 or strain1 == 7:
        ctrlnum = 3

    else:
        ctrlnum = 2
    return ctrlnum

def tailtubenaming() -> int():
    tailnum = int(input("What is your total number of tails?"))

    bonusnum = tailnum/10
    round(bonusnum)

    tubenum = tailnum ++ ctrlnum ++ bonusnum

    print("Your total number of tails is:", tailnum,
    "\n Your total number of ctrls is:", ctrlnum,
    "\n Your total number of bonus is:", bonusnum,
    "\n Your total number of tubes is:", tubenum,
            )

def allcalc() -> int():
    totalmix = tubenum * 50
    emerald = tubenum * 25
    dna = tubenum * 4
    primervol = (tubenum * .5) * primernum
    ddh20 = totamix - (emerald + dna + primervol)

def finalnums():
    # prints
    print("\nHere are your mastermix volumes:")
    print("Emerald:", tubenum, "ul.")
    print("DNA:", dna, "ul.")
    print("Primers:", primervol, "ul total,(", primervol / primernum, "ul per primer.)")
    print("ddH20:", ddh20, "ul.")
    print("Your total volume is:", totalmix, "ul.")
    print("\nThank you for using Vuppy.")


def main():
    primernaming()
    ctrlnaming()
    tailtubenaming()
    allcalc()
    finalnums()

main()

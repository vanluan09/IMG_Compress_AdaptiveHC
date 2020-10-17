import EncodeProcedure as Enp
if __name__ == "__main__":
    InputSourceSize = 26 # example the alphabet in english has 26 chacracters
    symbols = [1, 1, 18, 4, 22] # ~ [a, a, r, d, v]

    print("the encoded string is:", Enp.EncodeProcedure(InputSourceSize, symbols))
import hashlib
inp = open("inp.txt" , "r")
outputhash  = open("outputhashes.txt", "w")
for line in inp:            # Change this
    eachpwd = line.strip()  # Change this

    # Add this to understand the problem:
    print repr(line)

    sha_1 = hashlib.sha1()
    sha_1.update(eachpwd)
    outputhash.write(sha_1.hexdigest())
    outputhash.write("\n")

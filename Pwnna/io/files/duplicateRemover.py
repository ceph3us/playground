import hashlib
import os

def checksumfile(filename):
    fi = open(filename, "rb")
    content = fi.read()
    fi.close()
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()


def checksumdir(dirname):
    print "Checking for duplicates in directory %s" % dirname
    print "This might take a while."
    files = os.listdir(dirname)
    dups = []
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            if checksumfile(files[i]) == checksumfile(files[j]):
                print files[i], "==", files[j] 
                dups.append(files[j])
                
    if len(dups) > 0:
        choice = raw_input("delete duplicates? [Y/N]").lower()
        if choice == "y":
            for f in dups:
                os.remove(f)
                print f, "deleted."
    else:
        print "No duplicates found!"

    raw_input("Press enter to exit.")

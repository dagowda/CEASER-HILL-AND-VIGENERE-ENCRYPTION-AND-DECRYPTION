UID=119151556
Last_name="devaladakere arvind"
First_name="dhanush"
def caesar_str_enc(planetext,k):
    ciphertxt=""
    planetext=planetext.lower()
    a=int(len(planetext))
    for i in range(0,a):
     if ' ' not in planetext[i]:
        for j in range(97, 123):
            if planetext[i]==chr(j):
                a = (j - 97 + k) % 26
                ciphertxt+=chr(a+97)
     else:
         continue
    print("encrypted cipher :" +ciphertxt.upper())
def caesar_str_dec(enctxt,c):
    planetxt=""
    enctxt=enctxt.lower()
    a = int(len(enctxt))
    for i in range(0, a):
        if ' ' not in enctxt[i]:
         for j in range(97, 123):
            if enctxt[i]==chr(j):
                a=(j-97-c)%26
                planetxt+=chr(a+97)
        else:
            continue
    print("planetext :"+ planetxt.upper())
v=str(input("please enter the text to encrypt :"))
z=str(input("please enter the text to decrypt :"))
x=int(input("please enter the key :"))
caesar_str_enc(v,x)
caesar_str_dec(z,x)


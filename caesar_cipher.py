while True:
    print("-----Caesar Cipher-----")
    print("1.Encrypt\n2.Decrypt\n(Enter any other number to exit)")
    ch=int(input("Enter choice:"))
    if ch==1:
        string=input("Enter the string(lowercase): ")
        key=int(input("Enter the key code: "))
        encrypt_code=""
        for char in string:
            ordinal=ord(char)
            ordinal+=key
            if ordinal>ord('z'):
                ordinal=ord('a')+ordinal-ord('z')-1
            encrypt_code+=chr(ordinal)
        print("Encrypted Code :",encrypt_code)
    elif ch==2:
        code_string=input("Enter the coded string(lowercase): ")
        key=int(input("Enter the key code: "))
        decrypt_msg=""
        for char in code_string:
            ordinal=ord(char)
            ordinal-=key
            if ordinal<ord('a'):
                ordinal=ord('z')-ord('a')+ordinal+1
            decrypt_msg+=chr(ordinal)
        print("Decrypted Message :",decrypt_msg)
    else:
        break
s='Welcome to VScode'
# 1. lower()          make all characters into lower case
print("In Lower case :",s.lower())
# 2. upper()          make all characters into upper case(all in capital letters)
print("In Upper case :",s.upper())
# 3. title()          make first letter capital of ech sentance
print("In Title case:",s.title())
# 4. capitalise()     make first letter capital only
print("In Capitalise case :",s.capitalize())
# 5. find()           return index of the character that you find . the char is not exits in the sring then it returns :-1
print("Find : ",s.find('e'))
print("Find : ",s.find('e',2))     #start searching form index 2
# 6. index()          return index of the character that you find . the char is not exits in the sring then it returns: error
print("Index : ",s.index('e'))
# 7. isalpha()        returns true when string contain all alphabates.
w="welcome"
print("isalpha : ",w.isalpha())
# 8. isdigit()        returns true when string contain all digits(numbers). 
print("isdigit : ",w.isdigit())
# 9. isalnum()        returns true when string contain alphabates or digits(numbers) and combination of both.
w="welcome123" 
print("isalnum : ",w.isalnum())
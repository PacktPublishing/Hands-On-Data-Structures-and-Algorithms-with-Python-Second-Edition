
def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]                              # stores unicode value of each character in text 
    ord_pattern = [ord(j) for j in pattern]                        # stores unicode value of each character in pattern
    len_text = len(text)                                           # stores length of the text 
    len_pattern = len(pattern)                                     # stores length of the pattern
    len_hash_array = len_text - len_pattern + 1                    # stores the length of new array that will contain the hash values of text
    hash_text = [0]*(len_hash_array)                               # Initialize all the values in the array to 0.
    hash_pattern = sum(ord_pattern)                                                
    for i in range(0,len_hash_array):                              # step size of the loop will be the size of the pattern
        if i == 0:                                                 # Base condition
            hash_text[i] = sum(ord_text[:len_pattern])             # initial value of hash function
        else:
            hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord_text[i+len_pattern-1])   # calculating next hash value using previous value
    return [hash_text, hash_pattern]                               # return the hash values



def Rabin_Karp_Matcher(text, pattern):
    text = str(text)                                                     # convert text into string format
    pattern = str(pattern)                                               # convert pattern into string format
    hash_text, hash_pattern = generate_hash(text, pattern)               # generate hash values using generate_hash function
    len_text = len(text)                                                 # length of text
    len_pattern = len(pattern)                                           # length of pattern
    flag = False                                                         # checks if pattern is present atleast once or not at all
    for i in range(len(hash_text)):                         
        if hash_text[i] == hash_pattern:                                 # if the hash value matches
            count = 0                                                    # count stores the total characters upto which both are similar
            for j in range(len_pattern):                                 
                if pattern[j] == text[i+j]:                              # checking equality for each character
                    count += 1                                           # if value is equal, then update the count value
                else:
                    break
            if count == len_pattern:                                     # if count is equal to length of pattern, it means match has been found
                    flag = True                                          # update flag accordingly
                    print('Pattern occours at index',i)
    if not flag:                                                         # if pattern doesn't match even once, then this if statement is executed
        print('Pattern is not at all present in the text')

Rabin_Karp_Matcher("101110000011010010101101","10112")

# Works for numeric
Rabin_Karp_Matcher("101110000011010010101101","1011")

# Works for alphabets
Rabin_Karp_Matcher("ABBACCADABBACCEDF","ACCE")

# Works for alpha numeric
Rabin_Karp_Matcher("abc1-3klm890zsdoifjwej8cjv09wn vn09aej09jv 09wje09cj 09 j093j0 9j 092j3 09c09", "09w")


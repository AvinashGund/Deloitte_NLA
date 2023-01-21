#Consider String str, pick each integer from fibonacci series and insert one by one into str such that each character of str is followed by 
#   interger picked from the fibonacci series.Next, find the sum of all the integers picked and add it at the beginiing of str  
# Example: Input: abcde Output:12a1b1c2d3e5


def fibonacci(number : int)-> int:

    if number==1 or number ==2:
        return 1
    if number==0:
        return 0
    else:
        return ( fibonacci(number-2) + fibonacci(number-1))

def process_str(input_tokens : str)-> str:
    out= str
    #input_tokens=list(input)

    if(len(input_tokens)==1):
        out="1" + input_tokens[len(input_tokens)-1] + fibonacci(1)
    if(len(input_tokens)==2):
        out="2" + input_tokens[len(input_tokens)-1] + fibonacci(1) + input_tokens[len(input_tokens) + fibonacci(2)]
    
    out = input_tokens[len(input_tokens) - len(input_tokens)] + str(fibonacci(1)) + input_tokens[len(input_tokens) - (len(input_tokens) - 1)] + str(fibonacci(2))

    i = 3
    sum = 2

    while (i<len(input_tokens)):
        fib_out = fibonacci(i)
        sum = sum + fib_out
        out = out + str(input_tokens[i-1]) + str(fibonacci(i))
        i += 1

    out = str(sum) + out
    return out




if __name__ == "__main__":
    input="abcde"
    print(f"Result={process_str(input)}")
    
    


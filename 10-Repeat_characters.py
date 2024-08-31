# Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.


def repeat_char(string=""):
    return_str=""
    for i in range(len(string)):
        return_str= return_str+string[i]
        return_str= return_str+string[i]

        
    return return_str

n = "now"
print(repeat_char(n))

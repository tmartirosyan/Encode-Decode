def Decode(binary_from_user):  # DECODING
    def BinaryToText(simple_binary):  # DECODING 8 CHARACTERS
        number = 0
        exponentiation = 8
        for i in simple_binary:
            exponentiation -= 1
            number += int(i) * 2 ** exponentiation
        return number

    text = ""
    for i in range(0, len(binary_from_user), 8):
        text += chr(BinaryToText(binary_from_user[i:i + 8]))
    return text


def Encode(simple_text):  # ENCODING
    def NumberToBinary(number):  # ENCODING EVERY NUMBER
        binary = ""
        num = int(number)
        while num >= 1:
            binary += str(num % 2)
            num //= 2
        text_part = (8 - len(binary)) * '0'
        binary += text_part
        return binary[::-1]

    binary_text = ""
    for char in simple_text:
        binary_text += NumberToBinary(ord(char))
    return binary_text


def EncodeToHexadecimal(simple_text):
    def NumberToHexadecimal(number):
        number_more_than_10_value_in_char = ['A', 'B', 'C', 'D', 'E', 'F']
        text = ""
        while number >= 16:
            char = number % 16
            if (char >= 10):
                text += number_more_than_10_value_in_char[char - 10]
            else:
                text += str(char)
            number //= 16
        text += str(number)
        return text[::-1]

    text = ""
    for char in simple_text:
        text += NumberToHexadecimal(ord(char)) + " "
    return text


binary_string_from_user = "01011001011011110111010100100000011011010111010101110011011101000010000001110011011001010110111001100100001000000110000101101110011100110111011101100101011100100111001100100000011101000110111100100000011001010111100001100101011100100110001101101001011100110110010101110011001000000011010000100000011010000110111101110101011100100111001100100000011000100110010101100110011011110111001001100101001000000111010001101000011001010010000001101100011001010111001101110011011011110110111000101110"
string_to_binary_from_user = "You must send answers to exercises 4 hours before the lesson."

# print(Decode(binary_string_from_user))
# print(Encode(string_to_binary_from_user))
print(EncodeToHexadecimal(string_to_binary_from_user))

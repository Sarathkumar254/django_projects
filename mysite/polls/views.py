from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def convert(request):
    """Input and output value conversion"""
    if request.method == "GET":
        return render(request, "polls/index.html")
    else:
        input_type = request.POST["convert"]
        output_type = request.POST["convert1"]
        input_value = request.POST["num1"]
        conversion_type = input_type + "_" + output_type
        converted_value = ConversionDict(con_type=conversion_type, input_val=input_value)
        return render(request, "polls/result.html", {"converted_value": converted_value})


def decimalToBinary(n):
    return bin(eval(n)).replace("0b", "")


def binaryToDecimal(n):
    return int(n, 2)


def binaryToHex(binary):
    decimal_representation = int(binary, 2)
    return hex(decimal_representation)


def hexToBinary(hex_value):
    return bin(int(hex_value, 16)).zfill(8)


def binaryToOctal(bnum):
    return oct(int(bnum, 2))[2:]


def octToBinary(octal):
    return bin(int(octal, 8))


def decimalToHex(decimal):
    return hex(int(decimal))


def hexToDecimal(hex_val):
    return int(hex_val, 16)


def decToOctal(decimal):
    return oct(int(decimal))[2:]


def octalToDecimal(octal_num):
    return int(octal_num, 8)


def hexToOctal(hex_value):
    return oct(int(hex_value, 16))[2:]


def octalToHex(octal_num):
    return hex(int(octal_num, 8))[2:]


def ConversionDict(input_val, con_type):
    """Conversion list is used to convert the values
    from on format to another format based on the input"""
    if con_type == "binary_binary":
        return input_val
    elif con_type == "binary_decimal":
        return binaryToDecimal(input_val)
    elif con_type == "binary_hex":
        return binaryToHex(input_val)
    elif con_type == "binary_octal":
        return binaryToOctal(input_val)
    elif con_type == "decimal_binary":
        return decimalToBinary(input_val)
    elif con_type == "decimal_decimal":
        return input_val
    elif con_type == "decimal_hex":
        return decimalToHex(input_val)
    elif con_type == "decimal_octal":
        return decToOctal(input_val)
    elif con_type == "hex_binary":
        return hexToDecimal(input_val)
    elif con_type == "hex_decimal":
        return decimalToBinary(input_val)
    elif con_type == "hex_hex":
        return input_val
    elif con_type == "hex_octal":
        return hexToOctal(input_val)
    elif con_type == "octal_binary":
        return octToBinary(input_val)
    elif con_type == "octal_decimal":
        return octalToDecimal(input_val)
    elif con_type == "octal_decimal":
        return octalToDecimal(input_val)
    elif con_type == "octal_hex":
        return octalToHex(input_val)
    elif con_type == "octal_octal":
        return input_val

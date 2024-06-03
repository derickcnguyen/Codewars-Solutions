Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"

def kebabize(st):
    kebab = ''
    for i,char in enumerate(st):
        if char.isupper():
            if i != 0:
                kebab += '-' + char.lower()
            else:
                kebab += char.lower()
        elif char.isalpha():
            kebab += char
    return kebab.lstrip('-')

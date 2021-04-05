from mappings import Mappings

test = "Hקט צשמ ים' שרק טםו??"

if ord(test[0]) > 128 or test[0].isupper():
    print(test.translate(Mappings.heb_eng))
else:
    print(test.translate(Mappings.eng_heb)[::-1])
import sys
import translator.kor_to_braille as kor_to_braille


def to_braille(json):
    return json["braille"]


def braille_str(json):
    json_format_braille = json
    return "".join(list(map(to_braille, json_format_braille)))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("You should input text.")
    else:
        var1 = sys.argv[1]
        result_json = kor_to_braille.translate(var1)
        print (braille_str(result_json))

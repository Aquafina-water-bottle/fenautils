import json
import unittest

from fenautils import JsonStruct, to_json, pop, items, values, keys

nested_json = """
{
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML"
        }
      }
    }
  }
}
"""

nested_json_final = """
{
  "glossary": {
    "title": "memes",
    "GlossDiv": {
      "GlossList": {
        "GlossEntry": {
          "TEST1": "TEST1",
          "TEST2": "TEST2"
        }
      }
    }
  }
}
"""


nested_list_json = """
{
  "outer_list": [
    {
      "attr": 5
    },
    [
      "this",
      "is",
      "a",
      "nested",
      "list"
    ]
  ]
}
"""

def hello(string):
    """
    djb2 hash algorithm lol
    """
    hash_int = 5381

    for char in string:
        char = ord(char)
        hash_int = ((hash_int << 5) + hash_int) + char

    return hash_int % ((1<<31)-1)


class TestJsonObjectUtils(unittest.TestCase):
    def test_json_object(self):
        a = JsonStruct({"x": 1})
        self.assertEqual(repr(a), "JsonStruct[x=1]")

        b = JsonStruct(json.loads(nested_json))
        self.assertEqual(repr(b),
            "JsonStruct[glossary=JsonStruct[title='example glossary', GlossDiv=JsonStruct[title='S', GlossList=JsonStruct[GlossEntry=JsonStruct[ID='SGML']]]]]")

        self.assertTrue(hasattr(b.glossary.GlossDiv.GlossList.GlossEntry, "ID"))

        # checks getting attributes using the index method or the regular attribute method
        self.assertEqual(b.glossary.GlossDiv.GlossList.GlossEntry.ID, "SGML")
        self.assertEqual(b["glossary"].GlossDiv["GlossList"].GlossEntry["ID"], "SGML")
        self.assertEqual(b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["ID"], "SGML")

        # sets the attribute using regular attributes
        b.glossary.title = "a title"
        self.assertEqual(b["glossary"]["title"], "a title")

        # sets the attribute using dictionary indexing
        b["glossary"]["title"] = "memes"
        self.assertEqual(b.glossary.title, "memes")

        # sets new attributes using regular attributes
        b.glossary.GlossDiv.GlossList.GlossEntry.TEST1 = "TEST1"
        self.assertEqual(b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["TEST1"], "TEST1")

        # sets new attributes using dictionary indexing
        b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["TEST2"] = "TEST2"
        self.assertEqual(b.glossary.GlossDiv.GlossList.GlossEntry.TEST2, "TEST2")

        self.assertEqual(repr(b),
            "JsonStruct[glossary=JsonStruct[title='memes', GlossDiv=JsonStruct[title='S', GlossList=JsonStruct[GlossEntry=JsonStruct[ID='SGML', TEST1='TEST1', TEST2='TEST2']]]]]")

        # displays the keys and values of the json struct
        self.assertListEqual(list(keys(b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"])), ["ID", "TEST1", "TEST2"])
        self.assertListEqual(list(values(b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"])), ["SGML", "TEST1", "TEST2"])
        self.assertListEqual(
            list(items(b["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"])),
            [("ID", "SGML"), ("TEST1", "TEST1"), ("TEST2", "TEST2")]
            )


        # removes values
        self.assertEqual(pop(b["glossary"].GlossDiv["GlossList"].GlossEntry, "ID"), "SGML")
        self.assertEqual(pop(b.glossary["GlossDiv"], "title"), "S")

        self.assertEqual(repr(b),
            "JsonStruct[glossary=JsonStruct[title='memes', GlossDiv=JsonStruct[GlossList=JsonStruct[GlossEntry=JsonStruct[TEST1='TEST1', TEST2='TEST2']]]]]")

        # checks for valid json
        b_json_str = json.dumps(to_json(b), indent=2)
        self.assertEqual(b_json_str, nested_json_final.strip())


        c = JsonStruct(json.loads(nested_list_json))
        self.assertEqual(repr(c), "JsonStruct[outer_list=[JsonStruct[attr=5], ['this', 'is', 'a', 'nested', 'list']]]")


        c_json_str = json.dumps(to_json(c), indent=2)
        self.assertEqual(c_json_str, nested_list_json.strip())


        d = JsonStruct({
            # uses list comprehension to see if python code executes properly
            "list_comp": "$([x**2 for x in range(4)])",

            # uses function `hello` defined in this file to see if globals work
            "using_func": "$(hello('there'))"
        }, globals=globals())

        self.assertEqual(repr(d), "JsonStruct[list_comp=[0, 1, 4, 9], using_func=275570463]")






import json
import unittest

from fenautils import JsonStruct

some_fantastic_json = """
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
  },
  "some_list": [
    {
      "idk": 5
    },
    [
      "nested_list",
      "a",
      "b",
      "c"
    ]
  ]
}
"""

result_json = """
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
  },
  "some_list": [
    {
      "idk": "changed var"
    },
    [
      "nested_list",
      "a",
      "b",
      "c"
    ]
  ]
}
"""

class TestJsonObjectUtils(unittest.TestCase):
    def test_json_object(self):
        x = JsonStruct({"x": 1})
        self.assertEqual(repr(x), "JsonStruct[x=1]")

        y = JsonStruct(json.loads(some_fantastic_json))
        self.assertEqual(repr(y), "JsonStruct[glossary=JsonStruct[title='example glossary', GlossDiv=JsonStruct[title='S', GlossList=JsonStruct[GlossEntry=JsonStruct[ID='SGML']]]], some_list=[JsonStruct[idk=5], ['nested_list', 'a', 'b', 'c']]]")

        # pylint: disable=no-member
        self.assertEqual(y.glossary.GlossDiv.GlossList.GlossEntry.ID, "SGML")
        self.assertEqual(y.some_list[0].idk, 5)

        y.some_list[0].idk = "changed var"
        self.assertEqual(y.some_list[0].idk, "changed var")

        # print(y.to_json())
        self.assertEqual(json.dumps(y.to_json(), indent=2), result_json.strip())



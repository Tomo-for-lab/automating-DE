import os
from openai import OpenAI

# 環境変数からAPIキーを取得
api_key = os.environ.get("OPENAI_API")
client = OpenAI(api_key=api_key)

response = client.responses.create(
  model="o4-mini", #o3にするのは状況によりあとで
  input=[
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "what color do you like?"
        }
      ]
    }
  ],
  text={ #これは入力のテキストを指定するためのもの
    "format": {
      "type": "text"
    }
  },
  reasoning={ #これは推論のためのもの highの方が精度高い（が消費トークン多い）
    "effort": "high"
  },
  tools=[ #これはツールの指定 かわりなし
    {
      "type": "function",
      "name": "set_favourite_color",
      "description": "Assign a favourite color to a user",
      "parameters": {
        "type": "object",
        "required": [
          "user_id",
          "color"
        ],
        "properties": {
          "user_id": {
            "type": "string",
            "description": "Unique identifier for the user"
          },
          "color": {
            "type": "string",
            "description": "The user's favourite color"
          }
        },
        "additionalProperties": False
      },
      "strict": True
    }
  ],
  tool_choice={
    "type": "function",
    "name": "set_favourite_color"
  },
  store=False #なんども同じやり取りをする場合、ストレージに保存した方がトークン数が減る、今回は1回聞くだけなら関係ない
)

print(response)
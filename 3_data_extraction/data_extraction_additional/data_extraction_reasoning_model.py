import os
import re
import json
import copy
import glob
from openai import OpenAI

# 環境変数からAPIキーを取得
api_key = os.environ.get("OPENAI_API")
client = OpenAI(api_key=api_key)

# GPT関数呼び出し用の関数
def GPT_function_calling(tools, messages, tools_name):
    # メッセージの処理
    input_messages = []
    for message in messages:
        content_list = []
        if isinstance(message["content"], list):
            # 既にリスト形式の場合はそのまま使用
            content_list = message["content"]
        else:
            # テキストのみの場合はテキストオブジェクトに変換
            content_list = [{"type": "text", "text": message["content"]}]
        
        input_messages.append({
            "role": message["role"],
            "content": content_list
        })
    
    # tools_nameからtool_choiceを構築
    tool_choice = {
        "type": "function",
        "name": tools_name
    }
    
    response = client.responses.create(
        model="o4-mini", #o3にするのは状況によりあとで
        input=input_messages,
        text={ #これは入力のテキストを指定するためのもの
            "format": {
                "type": "text"
            }
        },
        reasoning={ #これは推論のためのもの highの方が精度高い（が消費トークン多い）
            "effort": "high"
        },
        tools=tools, #これはツールの指定 かわりなし
        tool_choice=tool_choice,
        store=False #なんども同じやり取りをする場合、ストレージに保存した方がトークン数が減る、今回は1回聞くだけなら関係ない
    )
    
    return response

# GPTチャット用の関数
def GPT_chat(tools, messages, tools_name):
    # メッセージの処理
    input_messages = []
    for message in messages:
        content_list = []
        if isinstance(message["content"], list):
            # 既にリスト形式の場合はそのまま使用
            content_list = message["content"]
        else:
            # テキストのみの場合はテキストオブジェクトに変換
            content_list = [{"type": "text", "text": message["content"]}]
        
        input_messages.append({
            "role": message["role"],
            "content": content_list
        })
    
    # tools_nameからtool_choiceを構築
    tool_choice = {
        "type": "function",
        "name": tools_name
    }
    
    response = client.responses.create(
        model="o4-mini", #o3にするのは状況によりあとで
        input=input_messages,
        text={ #これは入力のテキストを指定するためのもの
            "format": {
                "type": "text"
            }
        },
        reasoning={ #これは推論のためのもの highの方が精度高い（が消費トークン多い）
            "effort": "high"
        },
        tools=tools, #これはツールの指定 かわりなし
        tool_choice=tool_choice,
        store=False #なんども同じやり取りをする場合、ストレージに保存した方がトークン数が減る、今回は1回聞くだけなら関係ない
    )
    
    return response

# データ抽出のためのツール作成関数
def make_tools_DE(optimized_all_fields):
    properties_dict = {item['name']: {k: v for k, v in item.items() if k != 'name'} for item in optimized_all_fields}
    name_list = [item['name'] for item in optimized_all_fields]

    tools = [{
        'type': 'function',
        'name': 'extract_study_features',
        'description': """Extracts key features from a user-inputted research article for systematic review purposes.
        The primary paper is named AuthorYYYY, the registry ULR AuthorYYYY_NCT1234, the protocol AuthorYYYY_pr, the appendix/supplement files AuthorYYY_app or AuthorYYY_supp, and the secondary papers AuthorYYYY_s1,2,…
        You can mainly extract data from primary paper.""",
        'parameters': {
            'type': 'object',
            'properties': {key: properties_dict[key] for key in name_list if key in properties_dict},
            'required': name_list
        },
        'strict': True
    }]

    return tools

# 再チェックのためのツール作成関数
def make_tools_recheck(all_fields, Non_DE_name_list):
    check_optimized_all_fields = copy.deepcopy(all_fields)
    for item in check_optimized_all_fields:
        # Output with True or False
        item['type'] = 'boolean'
    check_properties_dict = {item['name']: {k: v for k, v in item.items() if k != 'name'} for item in check_optimized_all_fields}

    description_tools = [{
        'type': 'function',
        'name': 'determine_data_presence',
        'description': """You have to determine whether you can extract the data corresponding to each variable from the inputted paper of a randomized controlled trial. True if the data to be extracted can be found, False if not.""",
        'parameters': {
            'type': 'object',
            'properties': {key: check_properties_dict[key] for key in Non_DE_name_list if key in check_properties_dict},
            'required': Non_DE_name_list
        },
        'strict': True
    }]

    return description_tools

# 再抽出のためのツール作成関数
def make_tools_DE_reextract(optimized_all_fields, name_list, start, end):
    properties_dict = {item['name']: {k: v for k, v in item.items() if k != 'name'} for item in optimized_all_fields}

    splitted_name_list = copy.deepcopy(name_list[start:end])
    
    tools = [{
        'type': 'function',
        'name': 'extract_study_features',
        'description': """Extracts key features from a user-inputted research article for systematic review purposes.
        The primary paper is named AuthorYYYY, the registry ULR AuthorYYYY_NCT1234, the protocol AuthorYYYY_pr, the appendix/supplement files AuthorYYY_app or AuthorYYY_supp, and the secondary papers AuthorYYYY_s1,2,…
        You can mainly extract data from primary paper.""",
        'parameters': {
            'type': 'object',
            'properties': {key: properties_dict[key] for key in splitted_name_list if key in properties_dict},
            'required': splitted_name_list
        },
        'strict': True
    }]

    return tools

# ツール作成関数（バッチデータ抽出用）
def make_tools_DE_recheck(optimized_all_fields, DE_name_list, start, end):
    properties_dict = {item['name']: {k: v for k, v in item.items() if k != 'name'} for item in optimized_all_fields}

    splitted_name_list = copy.deepcopy(DE_name_list[start:end])
    
    tools = [{
        'type': 'function',
        'name': 'extract_study_features',
        'description': """Extracts key features from a user-inputted research article for systematic review purposes.
        The primary paper is named AuthorYYYY, the registry ULR AuthorYYYY_NCT1234, the protocol AuthorYYYY_pr, the appendix/supplement files AuthorYYY_app or AuthorYYY_supp, and the secondary papers AuthorYYYY_s1,2,…
        You can mainly extract data from primary paper.""",
        'parameters': {
            'type': 'object',
            'properties': {key: properties_dict[key] for key in splitted_name_list if key in properties_dict},
            'required': splitted_name_list
        },
        'strict': True
    }]

    return tools

# テスト関数
if __name__ == "__main__":
    # 簡単なテスト
    test_tool = [{
        'type': 'function',
        'name': 'set_favourite_color',
        'description': 'Assign a favourite color to a user',
        'parameters': {
            'type': 'object',
            'required': ['user_id', 'color'],
            'properties': {
                'user_id': {
                    'type': 'string',
                    'description': 'Unique identifier for the user'
                },
                'color': {
                    'type': 'string',
                    'description': 'The user\'s favourite color'
                }
            }
        },
        'strict': True
    }]
    
    test_messages = [{
        'role': 'user',
        'content': 'what color do you like?'
    }]
    
    response = GPT_function_calling(test_tool, test_messages, 'set_favourite_color')
    print(response)

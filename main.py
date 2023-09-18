import requests, json

URL = 'https://leetcode.com/problems/linked-list-cycle-ii/'

MARKDOWN = {
    "<div>": "",
    "</div>": "",
    "<u>": "",
    "</u>": "",
    "<p>": "",
    "</p>": "",
    "<ol>": "",
    "</ol>": "",
    "<ul>": "",
    "</ul>": "",
    "<li>": "- ",
    "</li>": "",
    "&nbsp;": "",
    "&#39;": "'",
    "&quot;": "\"",
    "&rsquo;": "'",
    "&lsquo;": "'",
    "<em>": "",
    "</em>": "",
    "<b>": "<strong>",
    "</b>": "</strong>",
    "<strong>Explanation: </strong>": "Explanation: ",
    "<strong>Explanation:</strong>": "Explanation:",
    "<strong>Explanation</strong>": "Explanation",
    "<strong>Input: </strong>": "Input: ",
    "<strong>Input:</strong>": "Input:",
    "<strong>Input</strong>": "Input",
    "<strong>Output: </strong>": "Output: ",
    "<strong>Output:</strong>": "Output:",
    "<strong>Output</strong>": "Output",
    '<strong class="example">Example': "**Example",
    "<strong>": " **",
    "</strong>": "** ",
    "\n</pre>":"</pre>",
    "<pre>": "```",
    "</pre>": "\n```",
    # "<code>": "`",
    # "</code>": "`",
    "&lt;": "<",
    "&gt;": ">",
    # "<sup>": "^",
    # "</sup>": "",
    "	": "", # special tab
    "<span.*?>": "",
    "</span>": "",
    "\u200b": "",
    "\n\n\n": "\n\n",
}

class Question:
    def __init__(self, url: str, markdown: dict):
        self.url = url
        self.slug = ''
        for paging in ['description', 'editorial', 'solutions', 'submissions']:
            if paging in url:
                self.url = url[:url.index(paging)]
                break
        self.slug = self.url.split('/')[-2]
        self.md = markdown
        
    def get_question_info(self) -> dict:
        '''
        question_info:
        ['questionFrontendId'] = question number.
        ['questionTitle'] = question title.
        ['difficulty'] = question difficulty.
        ['content'] = quesion's description.
        '''
        session = requests.Session()
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Referer': self.url}
        
        url = "https://leetcode.com/graphql"
        params = {'operationName': "getQuestionDetail",
            'variables': {'titleSlug': self.slug},
            'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionFrontendId
                    questionTitle
                    difficulty
                    content
                }
            }'''
        }

        json_data = json.dumps(params).encode('utf8')
        resp = session.post(url, data = json_data, headers = headers, timeout = 10)
        content = resp.json()

        question_info = content['data']['question']
        
        return question_info
    
    def write_heading(self, file, id: str, title: str):
        heading = f'# LC {id}. {title}\n\n'
        link = f'### [Problem link]({self.url})\n'
        file.write(heading)
        file.write(link)
        file.write('\n')
        
    def write_tag(self, file, difficulty: str):
        tag = f'###### tags: `leedcode` `{difficulty.lower()}` `python`'
        file.write(tag)
        file.write('\n\n')
        
    def write_description(self, file, content: str):
        content = "\n".join(content.splitlines())
        for old, new in self.md.items():
            content = content.replace(old, new)
        file.write(content)
        # file.write('\n\n')
        file.write('\n')
        
    def write_solution(self, file):
        file.write('## Solution 1\n')
        file.write('#### Python\n')
        file.write('```python=\n\n```\n')
        file.write('#### C++\n')
        file.write('```cpp=\n\n```\n')
        file.write('\n')
        
    def write_complexity(self, file):
        file.write('>### Complexity\n')
        file.write('>|             | Time Complexity | Space Complexity |\n')
        file.write('>| ----------- | --------------- | ---------------- |\n')
        file.write('>| Solution 1  | O(n)            | O(1)             |\n')
        file.write('\n')
        
    def write_note(self, file):
        file.write('## Note\n')
        file.write('x\n')
        file.write('[](https://)\n')
    
    def question2md(self):
        question_info = self.get_question_info()
        id = question_info['questionFrontendId']
        title = question_info['questionTitle']
        difficulty = question_info['difficulty']
        content = question_info['content']
        
        # start write markdown file
        file_name = 'tmp.md'
        with open(file_name, 'w') as f:
            self.write_heading(f, id, title)
            self.write_tag(f, difficulty)
            self.write_description(f, content)
            self.write_solution(f)
            self.write_complexity(f)
            self.write_note(f)

if __name__ == '__main__':
    q = Question(URL, MARKDOWN)
    q.question2md()

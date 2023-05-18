# https://gcyml.github.io/2019/03/03/Python%E7%88%AC%E5%8F%96Leetcode%E9%A2%98%E7%9B%AE%E5%8F%8AAC%E4%BB%A3%E7%A0%81/
# https://github.com/eddgr/clip-leetcode/blob/master/source/main.js#L105
import requests, json

URL = 'https://leetcode.com/problems/two-sum/'

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
    "<em>": "",
    "</em>": "",
    "<b>": "<strong>",
    "</b>": "</strong>",
    "<strong>Input</strong>": "Input\n",
    "<strong>Output</strong>": "Output\n",
    "<strong>Explanation</strong>": "Explanation\n",
    "<strong>Input:</strong>": "Input:",
    "<strong>Output:</strong>": "Output:",
    "<strong>Explanation:</strong>": "Explanation:",
    "<strong>Input: </strong>": "Input: ",
    "<strong>Output: </strong>": "Output: ",
    "<strong>Explanation: </strong>": "Explanation: ",
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
    "<sup>": "^",
    "</sup>": "",
    "	": "", # special tab
    "<span.*?>": "",
    "</span>": "",
    "\n\n\n": "\n\n",
}

class Question:
    def __init__(self, url: str, markdown: dict):
        self.url = url
        self.slug = ''
        if url.split('/')[-1] in ['description', 'editorial', 'solutions', 'submissions']:
            self.slug = url.split('/')[-3]
        else:
            self.slug = url.split('/')[-2]
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
        heading = f'# [{id}. {title}]({self.url})'
        file.write(heading)
        file.write('\n\n')
        
    def write_tag(self, file, difficulty: str):
        tag = f'###### tags: `leedcode` `{difficulty.lower()}`'
        file.write(tag)
        file.write('\n\n')
        
    def write_description(self, file, content: str):
        content = "\n".join(content.splitlines())
        for old, new in self.md.items():
            content = content.replace(old, new)
        file.write(content)
        file.write('\n')
        
    def write_solution(self, file):
        file.write('## Solution 1\n')
        file.write('```python=\n\n```')
        file.write('\n\n')
        
    def write_complexity(self, file):
        file.write('>### Complexity\n')
        file.write('>|             | Time Complexity | Space Complexity |\n')
        file.write('>| ----------- | --------------- | ---------------- |\n')
        file.write('>| Solution 1  | O(n)            | O(1)             |\n')
        file.write('\n\n')
        
    def write_note(self, file):
        file.write('## Note\n')
        file.write('x\n')
        file.write('\n\n')
    
    def question2md(self):
        question_info = self.get_question_info()
        id = question_info['questionFrontendId']
        title = question_info['questionTitle']
        difficulty = question_info['difficulty']
        content = question_info['content']
        
        # start write markdown file
        with open(f'{id}-{title}.md', 'w') as f:
            self.write_heading(f, id, title)
            self.write_tag(f, difficulty)
            self.write_description(f, content)
            self.write_solution(f)
            self.write_complexity(f)
            self.write_note(f)

if __name__ == '__main__':
    q = Question(URL, MARKDOWN)
    q.question2md()

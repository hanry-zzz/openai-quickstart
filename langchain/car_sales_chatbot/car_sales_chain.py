from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

class CarSalesChain:
    def __init__(self, model_name: str = "gpt-3.5-turbo", verbose: bool = True):
        
        # 翻译任务指令始终由 System 角色承担
        template = (
            """你是中国顶级的汽车销售, 你将为客户解决提出的问题\n
            不要暴露你是人工智能，尽可能以人类的话术回答客户的问题\n
            问答历史 {question_history}"""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # 待回答文本由 Human 角色输入
        human_template = "{question_content}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # 使用 System 和 Human 角色的提示模板构造 ChatPromptTemplate
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chat = ChatOpenAI(model_name=model_name, temperature=0.5, verbose=verbose)

        self.chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=verbose)

    def run(self, question_content: str, question_history: str) -> (str, bool):
        result = ""
        try:
            result = self.chain.run({
                "question_content": question_content,
                "question_history": question_history,
            })
        except Exception as e:
            print(f"An error occurred during translation: {e}")
            return result, False

        return result, True
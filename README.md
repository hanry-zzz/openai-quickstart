# Day 1 作业

## 1. 基于ChatGPT的课程总结 [作业链接🔗](https://chatgpt.com/share/02e3f40d-dbe1-4e9a-8932-42b274f08dc7)

# Day 2 作业

## 1. GPT-4V的使用 [作业链接🔗](https://github.com/hanry-zzz/openai-quickstart/blob/main/openai_api/gpt-4v.ipynb)

- 上传自己手写的图片到images文件夹，可命名为gpt-4v.jpg；
- 修改query_base64_image_description的方法描述，分析gpt-4v.jpg图片；
- 输出分析结果，并使用函数对输出进行渲染，渲染成Markdown格式使结果更易读；

## 2. ai translator的使用 [作业链接🔗](https://github.com/hanry-zzz/openai-quickstart/tree/main/langchain/openai-translator/ai_translator) [翻译后的markdown链接🔗](https://github.com/hanry-zzz/openai-quickstart/tree/main/langchain/openai-translator/tests)

- ai translator中，添加2种以上的其他语言对翻译

## 3. 扩展langchain chains [作业链接🔗](https://github.com/hanry-zzz/openai-quickstart/blob/main/langchain/jupyter/chains/router_chain.ipynb)

- 扩展chains，使其支持生物、计算机和汉语文学老师等学科的提示词模板及对应 Chains问答。

# Day 3 作业：

## 1. 实战sales chatbot [作业链接🔗](https://github.com/hanry-zzz/openai-quickstart/tree/main/langchain/car_sales_chatbot)（readme有截图）

- 自行生成一个新的产品介绍知识库，可搜索使用一个产品的行业数据，也可自建一个产品的真实数据。参考“房产销售聊天机器人”，开发一个“**销售聊天机器人”；
- 在"**销售聊天机器人"中，使用向量数据库进行检索回答，如果向量数据库检索不到问题答案时，能够通过一个prompt来回答这个问题，而不是直接告诉用户我是一个AI机器人。
- 请在openai-quickstart/langchain/sales_chatbot同级目录，新建一个"**_sales_chatbot"
  文件夹，并以这个文件夹作为该实战项目的目录。
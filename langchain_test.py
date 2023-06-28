from langchain.llms import OpenAI
openai_api_key = "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"
llm = OpenAI(temperature=0.9, openai_api_key = openai_api_key)

result = llm.predict("What would be a good company name for a company that makes colorful socks?")
print(result)
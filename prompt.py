from langchain import PromptTemplate

multi_var_prompt = PromptTemplate(
    input_variables=["customerName", "feedbackFromCustomer"],
    template="""
Human: Create an email to {customerName} in response to the following customer service feedback:

<customer_feedback>
{feedbackFromCustomer}
</customer_feedback>

Assistant:
"""
)

prompt = multi_var_prompt.format(
    customerName="John Doe",
    feedbackFromCustomer="""Hello AnyCompany,
I am very pleased with the recent experience I had when I called your customer support.
I got an immediate call back, and the representative was very knowledgeable in fixing the problem.
We are very happy with the response provided and will consider recommending it to other businesses.
"""
)

# Answer Generation

The selected documents are combined into a short context and fed into a text generation model. This example uses `google/flan-t5-small` to produce a concise answer.

The final result is retrieval-augmented generation: the model only answers from the retrieved knowledge, which improves accuracy and reduces hallucinations.

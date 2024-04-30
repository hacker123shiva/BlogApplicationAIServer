from ai import need_model

model=need_model()
response = model.generate_content("What is Love")
print((response))
print((response.text))


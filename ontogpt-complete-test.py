import ontogpt

def execute_ontogpt(input):
	try:
		result = ontogpt.complete(input)
		print("resultado")
		print(result)
	except Exception as e:
		print(f"Ocorreu um erro: {e}")

input = "example.txt"

execute_ontogpt(input)

from fastapi import FastAPI, Query

app = FastAPI()

# Пример: возвращает приветственное сообщение
@app.get("/")
def read_root():
    response = {"message": "Welcome to the FastAPI server!"}
    print("GET / - Response:", response)
    return response

# Пример: возвращает квадрат числа, переданного как query parameter
@app.get("/square")
def get_square(number: int = Query(..., description="Number to square")):
    result = {"number": number, "square": number ** 2}
    print(f"GET /square?number={number} - Response:", result)
    return result

# Пример: принимает строковый параметр и возвращает его длину
@app.get("/length")
def get_length(text: str = Query(..., description="Text to measure")):
    result = {"text": text, "length": len(text)}
    print(f"GET /length?text={text} - Response:", result)
    return result

# Пример: передает параметры в main
@app.post("/process")
def process_data(arg1: int, arg2: str):
    result = main_function(arg1, arg2)
    print(f"POST /process - Input: arg1={arg1}, arg2={arg2}, Response:", result)
    return {"input": {"arg1": arg1, "arg2": arg2}, "result": result}

# Главная функция, которая обрабатывает данные
def main_function(arg1: int, arg2: str):
    processed = {"processed_value": arg1 * 2, "reversed_string": arg2[::-1]}
    print(f"main_function - arg1={arg1}, arg2={arg2}, Result:", processed)
    return processed

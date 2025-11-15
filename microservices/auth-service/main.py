from fastapi import FastAPI, HTTPException
import pymysql

app = FastAPI()


def get_connection():
    return pymysql.connect(
        host="mysql",
        user="root",
        password="root",
        database="sghss",
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.get("/health")
def health():
    return {"status": "auth-service ok"}


@app.post("/login")
def login(cpf: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    VULNERABLE_MODE = True

    if VULNERABLE_MODE:
        query = f"SELECT * FROM users WHERE cpf='{cpf}' AND password='{password}'"
        cursor.execute(query)
    else:
        cursor.execute("SELECT * FROM users WHERE cpf=%s AND password=%s", (cpf, password))


    cursor.execute(query)
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "message": "Login realizado",
        "user": {"cpf": user["cpf"], "role": user["role"]},
    }

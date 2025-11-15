from fastapi import FastAPI, HTTPException
import pymysql

app = FastAPI()

def get_connection():
    return pymysql.connect(
        host="mysql",
        user="root",
        password="root",
        database="sghss",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/health")
def health():
    return {"status": "patient-service ok"}

@app.get("/patients")
def list_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()

@app.post("/patients")
def create_patient(name: str, cpf: str, birth_date: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO patients (name, cpf, birth_date) VALUES (%s, %s, %s)",
            (name, cpf, birth_date)
        )
        conn.commit()
    except pymysql.err.IntegrityError:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    return {"message": "Paciente criado com sucesso", "cpf": cpf}

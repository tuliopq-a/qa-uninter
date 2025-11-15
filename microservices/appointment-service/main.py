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
    return {"status": "appointment-service ok"}


@app.get("/appointments")
def list_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT appointments.id, patients.name AS patient,
               doctor_name, appointment_date
        FROM appointments
        INNER JOIN patients ON patients.id = appointments.patient_id
    """
    )
    return cursor.fetchall()


@app.post("/appointments")
def create_appointment(patient_id: int, doctor_name: str, appointment_date: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE id=%s", (patient_id,))
    patient = cursor.fetchone()

    if not patient:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")

    cursor.execute(
        "INSERT INTO appointments (patient_id, doctor_name, appointment_date) VALUES (%s, %s, %s)",
        (patient_id, doctor_name, appointment_date),
    )
    conn.commit()

    return {"message": "Consulta agendada", "patient": patient["name"]}

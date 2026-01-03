# Mini Project 1 – Breaking the Code  
## Automatic Cryptanalysis of a Mono-Alphabetic (Caesar) Cipher

---

## 1. Project Overview

This project is part of **Mini Project 1 – Breaking the Code** in the *Computer Security* course.  
The objective is to design an **automatic cryptanalysis system** capable of analyzing a message encrypted with a **mono-alphabetic Caesar cipher**, **without any prior knowledge of the key**, and to automatically recover the **most plausible plaintext**.

The project places the student in the role of a **cybersecurity analyst**, whose task is to test, evaluate, and compare multiple decryption hypotheses in order to make an automatic and justified decision.

---

## 2. Educational Objectives

The project aims to demonstrate the ability to:

- analyze an encrypted message without knowing the key,
- generate multiple decryption hypotheses,
- evaluate the linguistic quality of each hypothesis,
- automatically select the most credible plaintext,
- structure and document code clearly,
- explain the system and its logic in a concise way.

---

## 3. Scope and Constraints

- The project strictly follows the **mini-project specifications**.
- No encryption mechanism is exposed to the user.
- The decryption key is **never provided by the user**.
- All experiments are **local and pedagogical**.
- The web application is used **only as a demonstration interface**.

---

## 4. Working Principle

The system operates according to the following steps:

1. The user provides a ciphertext.
2. All possible Caesar cipher shifts (keys 0 to 25) are tested automatically.
3. Each candidate plaintext is evaluated using linguistic criteria.
4. The hypotheses are ranked according to their plausibility.
5. The most credible plaintext is selected and returned.

---

## 5. Project Architecture

project/
│
├── cryptanalyse.py # Decryption hypothesis generation
├── evaluation.py # Linguistic evaluation of hypotheses
├── main.py # Orchestration and local API (Flask)
│
└── web-app/ # User interface (React)


### Component Roles

- **cryptanalyse.py**  
  Generates all possible decryption hypotheses by testing every Caesar shift without prior knowledge of the key.

- **evaluation.py**  
  Evaluates the linguistic plausibility of each hypothesis using heuristic scoring.

- **main.py**  
  Coordinates the cryptanalysis process and exposes a local HTTP endpoint for the web interface.

- **web-app (React)**  
  Serves only as an input/output interface for demonstration purposes.

---

## 6. Technologies Used

- Python 3  
- Flask  
- Flask-CORS  
- React  

---

## 7. Running the Project

### Backend (Python)

pip install flask flask-cors
python main.py

The server runs locally at:

http://localhost:5000

Frontend (React)
npm install
npm start


The web application is available at:

http://localhost:3000

8. Example Test

Ciphertext input:

oh vhfxulwh lqirupdwltxh hvw lpsruwdqwh gdqv oh prqgh prghuqh.


Expected behavior:

Correct plaintext recovery

Automatic key detection

High linguistic score

9. Delivered Work

The submission includes:

Structured and commented source code

An explanatory video (3–6 minutes) presenting:

the project objective,

a live demonstration,

the cryptanalysis logic.

## 10. Conclusion

This project demonstrates an automated approach to breaking a mono-alphabetic Caesar cipher.
It highlights the role of linguistic analysis and automated decision-making in computer security, while strictly respecting the pedagogical and ethical framework of the course.

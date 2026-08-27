# Class Notes – Introduction to APIs

## 1. Introduction to API
- **API** stands for **Application Programming Interface**.
- It is a set of rules and protocols that allows different software applications to communicate with each other.
- APIs act as a bridge between the client (frontend/app) and the server (backend/database).
- Example: When you use a weather app, it calls a weather API to fetch live data.

---

## 2. API & Its Types
**Based on Architecture:**
- REST
- GraphQL
- SOAP
- gRPC (less common in beginners)

---

## 3. REST API vs GraphQL vs SOAP

| Feature          | **REST**                          | **GraphQL**                        | **SOAP**                              |
|------------------|-----------------------------------|------------------------------------|---------------------------------------|
| Style            | Architectural style               | Query language                     | Protocol                              |
| Data Format      | JSON (mostly), XML                | JSON                               | XML only                              |
| Flexibility      | Fixed endpoints                   | Client decides what data to fetch  | Strict contract                       |
| Performance      | Multiple requests may be needed   | Single request for exact data      | Heavier due to XML                    |
| Ease of Use      | Simple & widely used              | Powerful but steeper learning curve| Complex                               |
| Best For         | Most web & mobile apps            | Complex data requirements          | Enterprise & high-security systems    |

---

## 4. REST API and Methods
**REST** = Representational State Transfer  
It uses standard HTTP methods to perform operations on resources.

| HTTP Method | Purpose                  | Example Use Case                  |
|-------------|--------------------------|-----------------------------------|
| **GET**     | Retrieve data            | Get list of users                 |
| **POST**    | Create new data          | Add a new user                    |
| **PUT**     | Update entire resource   | Replace user details              |
| **PATCH**   | Partial update           | Update only user email            |
| **DELETE**  | Remove data              | Delete a user                     |

**Key REST Principles:**
- Stateless
- Client-Server architecture
- Resource-based URLs (e.g., `/users/1`)
- Uses HTTP status codes (200, 201, 404, 500, etc.)

---

## 5. Postman Installation
**Postman** is a popular tool used to test, develop, and document APIs.

### Steps to Install:
1. Go to the official website: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
2. Download the version for your OS (Windows / Mac / Linux).
3. Run the installer and follow the setup instructions.
4. Create a free Postman account (recommended) or continue without signing in.
5. Open Postman → Create a new request → Start testing APIs.

**Why use Postman?**
- Easy to send GET, POST, PUT, DELETE requests
- View response body, headers, and status codes
- Save collections and environments
- Generate code snippets in different languages

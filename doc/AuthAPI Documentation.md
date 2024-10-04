# AuthAPI - Documentation
# What is the product
The AuthAPI product is an API for creating and managing sessions on websites that choose to use it. It receives a username and a password, and if they are valid, it returns a JWT token. AuthAPI also stores some data from each session and some data about people (users).


# Brief usage context
When the user wants to create an account in the API, they must access the /person endpoint with the POST method, and in the header, they must provide the create token. The create person method receives the following data: first name, last name, username, birth date, and password. With the account created, the user must access the /auth/login endpoint and provide the username and password. If they are valid, the endpoint returns the JWT token, the type of Token (Bearer), and the id of the person responsible for the session. When the information is validated, before the function returns the token data, it stores some session data in the Session table of the database. The data in question are: user-agent, IP address, person id, and last_login (current date).

# Availabled resources
The API stores data in a PostgreSQL database, keeps the most logged-in users in a Redis cache to speed up the login process, saves and serves user photos through static files, encrypts the password in a hash, and compares the saved password hash with the hash of the password received at the login endpoint.
The API provides a password reset endpoint where a random reset code is sent to the user’s email, and with this code, they can update the password.

# Purpose and target audience
AuthAPI is ideal for those who are building an application and do not want to develop the authentication logic. With the resources mentioned above, AuthAPI facilitates session management and user authentication, allowing you to focus on developing the core functionalities of your application.

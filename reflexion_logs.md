# 🧠 Agent Reflexion Memory Logs

This file logs all the rules the agent has learned over time.

---
### 📅 2026-06-23 01:25:36
**Task Attempted:** Write a python function to fetch user data from an external REST API.

**Failure Reason:** **Code Review Result**
--------------------

After reviewing the code, I found that it does not include a 'timeout' parameter in the HTTP request. 

Therefore, I output:

 Missing timeout parameter in HTTP request.

**✅ Distilled Rule Learned:**
> Always include a 'timeout' parameter in HTTP requests to external REST APIs.

---
### 📅 2026-06-23 01:46:13
**Task Attempted:** Write a very minimal (under 10 lines) python function to fetch user data from an external REST API. Do not include error handling or extra parameters.

**Failure Reason:** Missing timeout parameter in HTTP request.

**✅ Distilled Rule Learned:**
> Always include a timeout parameter in HTTP requests to prevent indefinite waiting. Set a reasonable timeout value, such as 10 seconds, to ensure timely responses.

---
### 📅 2026-06-23 04:29:35
**Task Attempted:** string

**Failure Reason:** string

**✅ Distilled Rule Learned:**
> Always provide a specific task description when attempting a task. Never attempt a task with the same name as the task description.

---
### 📅 2026-06-23 04:30:01
**Task Attempted:** Write a python scraper

**Failure Reason:** Forgot to handle 404 errors

**✅ Distilled Rule Learned:**
> Always handle 404 errors in web scraping scripts. Implement try-except blocks to catch and handle HTTP errors, such as the 404 status code.

---
### 📅 2026-06-23 04:30:08
**Task Attempted:** Write a python scraper

**Failure Reason:** Forgot to handle 404 errors

**✅ Distilled Rule Learned:**
> Always handle 404 errors in web scraping scripts. Implement try-except blocks to catch and handle HTTP errors, such as requests.exceptions.HTTPError.

---
### 📅 2026-06-23 04:47:56
**Task Attempted:** Write a python function to query a user by name from Postgres

**Failure Reason:** Used string concatenation for the SQL query, vulnerable to SQL injection.

**✅ Distilled Rule Learned:**
> Always use parameterized queries or prepared statements to prevent SQL injection attacks. Never use string concatenation to build SQL queries.

---
### 📅 2026-06-23 04:48:09
**Task Attempted:** Write a script to download 1000 images from an API

**Failure Reason:** Did not implement rate limiting or sleep intervals, causing the API to block the IP.

**✅ Distilled Rule Learned:**
> Always implement rate limiting or sleep intervals when downloading data from an API to prevent IP blocking.

---
### 📅 2026-06-23 04:48:22
**Task Attempted:** Write a python script to process a 10GB CSV file

**Failure Reason:** Loaded the entire file into memory at once, causing an Out of Memory crash.

**✅ Distilled Rule Learned:**
> Always process large CSV files in chunks, using a buffer size that fits within available memory. Never load the entire CSV file into memory at once.

---
### 📅 2026-06-23 04:48:35
**Task Attempted:** Write a python script to parse an XML API response

**Failure Reason:** Did not check if the XML node existed before accessing it, causing AttributeError.

**✅ Distilled Rule Learned:**
> Always check if an XML node exists before attempting to access it. Use the 'if node is not None' condition before accessing the node's attributes or children.

---
### 📅 2026-06-23 04:53:33
**Task Attempted:** Fetch transaction data from Stripe API

**Failure Reason:** The HTTP request timed out after 60 seconds because no timeout parameter was set in the requests.get() call.

**✅ Distilled Rule Learned:**
> Always set a timeout parameter in the requests.get() call to prevent HTTP requests from timing out. Set the timeout parameter to a value greater than 0, such as requests.get(url, timeout=30).

---
### 📅 2026-06-23 04:53:47
**Task Attempted:** Fetch transaction data from Stripe API

**Failure Reason:** The HTTP request timed out after 60 seconds because no timeout parameter was set in the requests.get() call.

**✅ Distilled Rule Learned:**
> Always set a timeout parameter in the requests.get() call to prevent HTTP requests from timing out indefinitely. Set the timeout parameter to a value greater than 0, such as 60 seconds, to allow the request to timeout after a specified duration.

---
### 📅 2026-06-23 05:08:11
**Task Attempted:** Fetch transaction data from Stripe API

**Failure Reason:** The HTTP request timed out after 60 seconds because no timeout parameter was set in the requests.get() call.

**✅ Distilled Rule Learned:**
> Always set a timeout parameter in the requests.get() call to prevent HTTP requests from timing out indefinitely. Set the timeout parameter to a value that balances request completion speed with the risk of request failure due to network issues.

---
### 📅 2026-06-23 05:08:26
**Task Attempted:** Sync webhooks from GitHub API

**Failure Reason:** Hit GitHub rate limits (HTTP 403) but the script did not implement exponential backoff or retry logic.

**✅ Distilled Rule Learned:**
> Always implement exponential backoff or retry logic when interacting with APIs that have rate limits. Never fail silently when encountering API rate limits, instead, implement a retry mechanism with increasing delay.

---
### 📅 2026-06-23 05:08:41
**Task Attempted:** Scrape product prices from Amazon

**Failure Reason:** Blocked by Cloudflare because the requests did not include a valid User-Agent header.

**✅ Distilled Rule Learned:**
> Always include a valid User-Agent header in HTTP requests to avoid being blocked by Cloudflare.

---
### 📅 2026-06-23 05:08:54
**Task Attempted:** Write a script to search users by name in Postgres

**Failure Reason:** Used Python f-strings to format the SQL query, exposing the database to SQL Injection attacks.

**✅ Distilled Rule Learned:**
> Always use parameterized queries or prepared statements to prevent SQL Injection attacks when executing dynamic SQL queries. Never use string formatting or concatenation to build SQL queries.

---
### 📅 2026-06-23 05:09:10
**Task Attempted:** Write a script to connect to the production MongoDB database

**Failure Reason:** Hardcoded the database password directly in the Python script instead of using environment variables.

**✅ Distilled Rule Learned:**
> Always store sensitive database credentials, such as passwords, in environment variables instead of hardcoding them directly in the script.

---
### 📅 2026-06-23 05:09:25
**Task Attempted:** Parse a JSON payload from an external vendor

**Failure Reason:** Used a bare 'except:' block which silently swallowed a KeyError and caused the script to write corrupt data.

**✅ Distilled Rule Learned:**
> Always use specific exception types (e.g., 'except KeyError:') to prevent silent failures and ensure timely error handling.

---
### 📅 2026-06-23 05:09:29
**Task Attempted:** Parse a JSON payload from an external vendor

**Failure Reason:** Used a bare 'except:' block which silently swallowed a KeyError and caused the script to write corrupt data.

**✅ Distilled Rule Learned:**
> Always use specific exception types (e.g., 'except KeyError:') to avoid silently swallowing errors and ensure data integrity.

---
### 📅 2026-06-23 05:09:41
**Task Attempted:** Ingest user registration data into the database

**Failure Reason:** Did not validate the email format before insertion, causing the database to crash on invalid string types.

**✅ Distilled Rule Learned:**
> Always validate the email format before inserting user registration data into the database.

---
### 📅 2026-06-23 05:09:43
**Task Attempted:** Ingest user registration data into the database

**Failure Reason:** Did not validate the email format before insertion, causing the database to crash on invalid string types.

**✅ Distilled Rule Learned:**
> Always validate the email format before ingesting user registration data into the database.

---

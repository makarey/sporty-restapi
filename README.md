# PoetryDB API Testing

## Overview
This project tests the [PoetryDB API](https://github.com/thundercomb/poetrydb) using `pytest`. The API allows users to retrieve information about poets and their works through HTTP GET requests. This test suite ensures that API endpoints return expected responses and validate the data structure.

**NOTE:** According to the API documentation on [GitHub](https://github.com/thundercomb/poetrydb?tab=readme-ov-file#readme), PoetryDB supports only HTTPS GET requests. There is no mention of POST, PUT, UPDATE, or DELETE methods in the documentation, indicating that the API is read-only and does not allow modifying or deleting data.

## Technologies Used
- Python 3.x
- `pytest` for testing
- `requests` library for making API calls

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/makarey/sporty-restapi.git
    ```
2. Navigate to the project directory:
    ```
    cd sporty-restapi
    ```
3. Create a virtual environment:
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment (on macOS/Linux):
    ```
    source .venv/bin/activate
    ```
5. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

## How to Run Tests
   ```
   pytest -m poetry
   ```

## Test Scenarios
The following test cases validate different API functionalities:

| Test Case ID | Description | Steps | Expected Result | Validation |
|-------------|-------------|-------|----------------|------------|
| TC_01 | Retrieve all authors | 1. Send GET request to `/author` endpoint. <br> 2. Verify response status code. <br> 3. Validate JSON response structure. | A JSON object containing a list of authors. | Status code 200. <br> JSON response contains `authors` key and a non-empty list. |
| TC_02 | Retrieve all poems by a specific author | 1. Send GET request to `/author/William Shakespeare` endpoint. <br> 2. Verify response status code. <br> 3. Validate JSON response structure. | JSON list of poems by William Shakespeare. | Status code 200. <br> Each object in the response contains `title`, `author`, `lines`, and `linecount` fields. |
| TC_03 | Retrieve a random poem | 1. Send GET request to `/random` endpoint. <br> 2. Verify response status code. <br> 3. Validate JSON response structure. | A JSON list with one random poem. | Status code 200. <br> The response contains exactly one poem with valid fields. |
| TC_04 | Retrieve a poem by title | 1. Send GET request to `/title/Ozymandias`. <br> 2. Verify response status code. <br> 3. Validate JSON response structure. | JSON list with poem titled "Ozymandias". | Status code 200. <br> The response contains one or more poems with `title` field matching "Ozymandias". |
| TC_05 | Retrieve poems by line count | 1. Send GET request to `/linecount/14`. <br> 2. Verify response status code. <br> 3. Validate JSON response structure. | JSON list of poems with exactly 14 lines. | Status code 200. <br> Each poem in the response has `linecount` field equal to 14. |

## Validation Techniques
### 1. Status Code Validation
- Ensures that the request is successfully processed (`200 OK`).
- Prevents unexpected errors or unauthorized access (`403`, `404`, `500`).

### 2. JSON Structure Validation
- Confirms that the response is a valid JSON.
- Ensures expected keys (`title`, `author`, `lines`, `linecount`) are present.
- Prevents incorrect or malformed data.

### 3. Data Consistency Validation
- Validates that author names match the queried author.
- Ensures `linecount` values match the expected number of lines.
- Guarantees that random poem responses contain only one entry.

These validations ensure reliable and accurate API behavior, preventing unexpected failures in production applications.

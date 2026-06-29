# Test Cases for Login Page

| Test Case ID | Test Case                     | Input                          | Expected Result                                 |
|--------------|-------------------------------|--------------------------------|-------------------------------------------------|
| TC01         | Valid Login                   | username: student; password: Password123 | User is redirected to dashboard; success message |
| TC02         | Invalid Credentials           | username: wrong; password: wrong | Error message displayed; login rejected         |
| TC03         | Empty Username                | username: (empty); password: Password123 | Validation prevents submission; error shown     |
| TC04         | Empty Password                | username: student; password: (empty) | Validation prevents submission; error shown     |
| TC05         | Missing Both Fields           | username: (empty); password: (empty) | Validation prevents submission; error shown     |
| TC06         | SQL Injection attempt         | username: ' OR '1'='1; password: anything | Login rejected; input sanitized                 |

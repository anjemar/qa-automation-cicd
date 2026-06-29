# Test Cases

| Test Case ID | Test Case        | Input                          | Expected Output             |
|--------------|------------------|--------------------------------|-----------------------------|
| TC01         | Valid Login      | student / Password123          | User login successfully     |
| TC02         | Invalid Login    | wronguser / wrongpass          | Error message displayed     |
| TC03         | Empty Fields     | "" / ""                        | Error message displayed     |
| TC04         | Missing Password | student / ""                   | Error message displayed     |
| TC05         | Missing Username | "" / Password123               | Error message displayed     |

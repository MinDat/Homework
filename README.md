# Build full REST API
```
Build 1 source use Django, 1 source use Flask FW
  Simple source has CRUD
      Create (status code: 201 and data)
      Get (status code: 200 and data)
      Update (status code: 200 and data)
      Delete (status code: 204)
      Bulk Create (status code 201)
  Handle Exceptiop
      Bad request: status code 400
  On Flask: using class for define dto, SQLAlchemy for connecting DB, create controller, service, repository
  DB: using postgresql (using DBeaver for connecting and checking data)
```
***
## Setup project Django
Sample code:
> https://www.django-rest-framework.org/tutorial/quickstart/#quickstart
- Adding database connection 
- Write Unit Test
***


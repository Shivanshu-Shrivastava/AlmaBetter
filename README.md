# AlmaBetter
- ## BACKEND FOR THE PROJECT:
```diff

- Django == 3.1.3
+ Python ==3.9.0
! Html
# css and Bootstrap
```
**I was deploying my code on the platform Heroku, but somehow
  The error is visible and I am a student and my exam is going on and I have to study for it and the time for submitting the project was also running out, so I decided that I will not deploy the code in Heroku.**
  
 - ## STEPS:--
 1. I've created my _Virtual Environment_ called **Venv**.
  
 2. Created my _APP_ called **mark**.
 3. In the file **urls.py** I've used **INCLUDE libraie**.
 4. There are four **TEMPLATES**:--
    - **base.html**
    - **Entermarks.html**
    - **home.html**
    - **leaderboard.html**
 5. **In the MODEL created a clss model named Mark_Class  Inside a class there are ModelFields name as**:--
    - Roll_no
    - Name
    - Mark_Math
    - Mark_Chemistry
    - Mark_physics
 6. And then I've registred my model into **Admin**.
 7. **In the VIEWS**:--
    - **def Mark_View()**
      - mark_view() render to template **home.html**.
    - **def enter_page_view()**:--
      - In this view you can write your **Roll no**,**Name**,**MOM**,**MOP**,**MOC** and see your **Result**.
      - enter page view render to template **EnterMarks.html**
    - **def view_leaderboard()**:--
      - You can see all the studnets percentage and Rank.
      - This view render to **leaderboards.html**
          
          

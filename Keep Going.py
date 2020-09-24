import os 
import time



User_Name = ""
Year = "2020/2021"
Intro = """
\t\t\t\t  _  __                  _____       _             
\t\t\t\t | |/ /                 / ____|     (_)            
\t\t\t\t | ' / ___  ___ _ __   | |  __  ___  _ _ __   __ _ 
\t\t\t\t |  < / _ \/ _ \ '_ \  | | |_ |/ _ \| | '_ \ / _` |
\t\t\t\t | . \  __/  __/ |_) | | |__| | (_) | | | | | (_| |
\t\t\t\t |_|\_\___|\___| .__/   \_____|\___/|_|_| |_|\__, | By: Hossam Hamdy
\t\t\t\t               | |                            __/ | 
\t\t\t\t               |_|                           |___/ 

\t\t <[ Believe in yourself, Believe in your dreams, It have been given to you for a reasons ]>

 [~] Add New Achievements:
 =========================\n
 \t[01] Add Books.
 \t[02] Add Courses.
 \t[03] Add Quora Answers.
 \t[04] Add Network.
 \t[05] Add Scripts
 \t[06] Add Skills.
 \t[07] Add Programming Language.
 \t[08] Add Problem Solving.
 \t[09] Add Blogs.
 \t[10] Exit.\n """




def add_new():

  global Intro

  query = ""
  print(Intro)

  # new choice 
  choice = int(input("Enter Choice~# "))
  while choice > 11 or choice < 1:
    print("\n[!] I can't handel the empty commands!\n")
    choice = int(input("Enter Choice~# "))


  # add new book
  if choice == 1:
    book_name = str(input("Enter Book Name: "))
    while book_name == "":
      book_name = str(input("Enter Book Name: "))
    query = f"{book_name}\n"
    with open("Books.txt","a") as new_book:
      new_book.write(query)
      print(f"\n[+] A New Book [ {book_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new Course
  elif choice == 2: 
    course_name = str(input("Enter Course Name: "))
    while course_name == "":
      course_name = str(input("Enter Course Name: "))
    query = f"{course_name}\n"
    with open("Courses.txt","a") as new_course:
      new_course.write(query)
      print(f"\n[+] A New Course [ {course_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new quora answer
  elif choice == 3:
    answer_name = str(input("Enter Answer Name: "))
    while answer_name == "":
      answer_name = str(input("Enter Answer Name: "))
    query = f"{answer_name}\n"
    with open("Quora Answers.txt","a") as new_quora:
      new_quora.write(query)
      print(f"\n[+] A New Answer  [ {answer_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new friend
  elif choice == 4:
    friend_name = str(input("Enter Friend Name: "))
    while friend_name == "":
      friend_name = str(input("Enter Friend Name: "))
    query = f"{friend_name}\n"
    with open("Network.txt","a") as new_friend:
      new_friend.write(query)
      print(f"\n[+] A New Friend [ {friend_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add nwe Script
  elif choice == 5:
    script_name = str(input("Enter Script Name: "))
    while script_name == "":
      script_name = str(input("Enter Script Name: "))
    query = f"{script_name}\n"
    with open("Scripts.txt","a") as new_script:
      new_script.write(query)
      print(f"\n[+] A New Scrips [ {script_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new skill
  elif choice == 6:
    skill_name = str(input("Enter Skill Name: "))
    while skill_name == "":
      skill_name = str(input("Enter Skill Name: "))
    query = f"{skill_name}\n"
    with open("Skills.txt","a") as new_skill:
      new_skill.write(query)
      print(f"\n[+] A New Skill [ {skill_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new programming language
  elif choice == 7:
    pl_name = str(input("Enter Programming Language Name: "))
    while pl_name == "":
      pl_name = str(input("Enter Programming Language Name: "))
    query = f"{pl_name}\n"
    with open("Programming Language.txt","a") as new_pl:
      new_pl.write(query)
      print(f"\n[+] A New Programming Language [ {pl_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new problem solving (submation)
  elif choice == 8:
    ps_name = str(input("Enter Problem Name: "))
    while ps_name == "":
      ps_name = str(input("Enter Problem Name: "))
    query = f"{ps_name}\n"
    with open("Problem Solving.txt","a") as new_ps:
      new_ps.write(query)
      print(f"\n[+] A New Problem Solving Submation [ {ps_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")


  # add new Posts or Blogs.
  elif choice == 9:
    blog_name = str(input("Enter Blog Name: "))
    while blog_name == "":
      blog_name = str(input("Enter Blog Name: "))
    query = f"{blog_name}\n"
    with open("Blogs.txt","a") as new_blog:
      new_blog.write(query)
      print(f"\n[+] A New Blog [ {blog_name} ] Has Been Added Successfully.\n")
      time.sleep(2)
      os.system("cls")

  elif choice == 10:
    exit()



while True:
  add_new()


os.system("pause")

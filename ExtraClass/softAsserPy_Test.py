from selenium import webdriver
import pytest_check  as check

def test_student_details():
    studentName="nara"
    student_age=31
    student_city="Hyd"

    check.equal(studentName,"nara","invalid name")
    check.equal(student_age,20,"Age validation failed")
    check.equal(student_city,"vija","Invalid city selected")
    
    print("Test executed even validation failed")

#test_student_details()

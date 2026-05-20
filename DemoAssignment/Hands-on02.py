test_Cases=[
    ["Login test","ENABLED"],
    ["Payment Test","ENABLED"],
    ["Camera Validation","DISABLED"],
    ["GPU Stress Test","ENABLED"],
    ["Critical ECU Test","FAILED"],
    ["Bluetooth","ENABLED"]
]

print("==============Automation Execution Started=====")

for test in test_Cases:
    test_name=test[0]
    status=test[1]

    #skip disabled tests
    if status=="DISABLED":
        print("\n skipping :", test_name)
        continue

    #stop execution on critical failure
    if status=="FAILED":
        print("\nCritival test cases failure foud")
        print("Stopped exection :",test_name)
        break

    print("\n Executing : ",test_name)
    print("Execution successful")

print("\n =============Execution Finished==========")
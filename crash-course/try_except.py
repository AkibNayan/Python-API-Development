def adult(something):
    #print("Age is "+something)
    try:
        print("Age is "+something)
    except:
        print("Failed to concat")
    finally:
        print("End of program")
        
adult(20)